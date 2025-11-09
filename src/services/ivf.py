import csv
import math


class IvfService:

    @staticmethod
    def _get_formulas() -> dict:
        """Get formulas from CSV."""
        formulas={}

        with open('ivf_success_formulas.csv', mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row_dict in csv_reader:                
                
                key = (
                    f"param_using_own_eggs:{row_dict['param_using_own_eggs']}|"
                    f"param_attempted_ivf_previously:{row_dict['param_attempted_ivf_previously']}|"
                    f"param_is_reason_for_infertility_known:{row_dict['param_is_reason_for_infertility_known']}"
                )

                # delete the three keys from dictionary as they are not needed anymore
                del row_dict['param_using_own_eggs']
                del row_dict['param_attempted_ivf_previously']
                del row_dict['param_is_reason_for_infertility_known']
                formulas[key] = row_dict

        return formulas

    @staticmethod
    def _generate_key_based_on_input(
            use_own_eggs:bool,
            used_ivf_in_past:bool,
            know_reason_for_infertility:bool,
    )-> str:

        use_own_eggs_str = "TRUE" if use_own_eggs else "FALSE"

        if used_ivf_in_past is None:
            used_ivf_in_past_str = "N/A"
        else:
            used_ivf_in_past_str = "TRUE" if used_ivf_in_past else "FALSE"
        
        know_reason_for_infertility_str = "TRUE" if know_reason_for_infertility else "FALSE"

        key = (
                f"param_using_own_eggs:{use_own_eggs_str}|"
                f"param_attempted_ivf_previously:{used_ivf_in_past_str}|"
                f"param_is_reason_for_infertility_known:{know_reason_for_infertility_str}"
        )

        return key

    @staticmethod
    def _calculate_bmi(height_feet, height_inches, weight):
        bmi = weight /pow((height_feet * 12 + height_inches),2)  * 703
        return bmi

    @staticmethod
    def calculate_ivf_estimator_success_rate(
            height_feet: int,
            height_inches: int,
            weight: int,
            age: int,
            use_own_eggs: bool,
            used_ivf_in_past: bool,
            know_reason_for_infertility: bool,
            number_of_live_births: int,
            number_of_prior_pregnancies: int,
            male_factor_infertility: bool,
            endometriosis: bool,
            tubal_factor: bool,
            ovulatory_disorder: bool,
            diminished_ovarian_reserve: bool,
            uterine_factor: bool,
            other_reason_unexplained: bool,
            ):
        """Calculate the success rate based on user input."""
        formulas = IvfService._get_formulas()

        key = IvfService._generate_key_based_on_input(
                use_own_eggs,
                used_ivf_in_past,
                know_reason_for_infertility,
        )

        formulas_for_calculation = formulas[key]
        user_bmi = IvfService._calculate_bmi(height_feet, height_inches, weight)

        formula_intercept = float(formulas_for_calculation['formula_intercept'])
        formula_age_linear_coefficient = float(formulas_for_calculation['formula_age_linear_coefficient'])
        formula_age_power_coefficient = float(formulas_for_calculation['formula_age_power_coefficient'])
        formula_age_power_factor = float(formulas_for_calculation['formula_age_power_factor'])
        formula_bmi_linear_coefficient = float(formulas_for_calculation['formula_bmi_linear_coefficient'])
        formula_bmi_power_coefficient = float(formulas_for_calculation['formula_bmi_power_coefficient'])
        formula_bmi_power_factor = float(formulas_for_calculation['formula_bmi_power_factor'])
        formula_tubal_factor_value = float(formulas_for_calculation[f'formula_tubal_factor_{str(tubal_factor).lower()}_value'])
        formula_male_factor_infertility_value = float(formulas_for_calculation[f'formula_male_factor_infertility_{str(male_factor_infertility).lower()}_value'])
        formula_endometriosis_value = float(formulas_for_calculation[f'formula_endometriosis_{str(endometriosis).lower()}_value'])
        formula_ovulatory_disorder_value = float(formulas_for_calculation[f'formula_ovulatory_disorder_{str(ovulatory_disorder).lower()}_value'])
        formula_diminished_ovarian_reserve_value = float(formulas_for_calculation[f'formula_diminished_ovarian_reserve_{str(diminished_ovarian_reserve).lower()}_value'])
        formula_uterine_factor_value = float(formulas_for_calculation[f'formula_uterine_factor_{str(uterine_factor).lower()}_value'])
        formula_other_reason_value = float(formulas_for_calculation[f'formula_other_reason_{str(know_reason_for_infertility).lower()}_value'])
        formula_unexplained_infertility_value = float(formulas_for_calculation[f'formula_unexplained_infertility_{str(other_reason_unexplained).lower()}_value'])

        number_of_prior_pregnancies_key = "2+" if number_of_prior_pregnancies >=2 else str(number_of_prior_pregnancies)
        formula_prior_pregnancies_value = float(formulas_for_calculation[f'formula_prior_pregnancies_{str(number_of_prior_pregnancies_key)}_value'])

        number_of_live_births_key = "2+" if number_of_live_births >=2 else str(number_of_live_births)
        formula_prior_live_births_value = float(formulas_for_calculation[f'formula_prior_live_births_{str(number_of_live_births_key)}_value'])


        score =(
            formula_intercept +
            formula_age_linear_coefficient * age + formula_age_power_coefficient * math.pow(age,formula_age_power_factor) +
            formula_bmi_linear_coefficient * user_bmi + formula_bmi_power_coefficient * math.pow(user_bmi,formula_bmi_power_factor) +
            formula_tubal_factor_value +
            formula_male_factor_infertility_value +
            formula_endometriosis_value +
            formula_ovulatory_disorder_value +
            formula_diminished_ovarian_reserve_value +
            formula_uterine_factor_value +
            formula_other_reason_value +
            formula_unexplained_infertility_value +
            formula_prior_pregnancies_value +
            formula_prior_live_births_value
        )

        exp_calculation = math.exp(score)
        success_rate = exp_calculation/(1 + exp_calculation)
        return success_rate