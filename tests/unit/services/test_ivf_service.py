
from src.services.ivf import IvfService

class TestIvfService:

    def test_ivf_service(self):
        score = IvfService.calculate_ivf_estimator_success_rate(
            height_feet = 5,
            height_inches = 3,
            weight = 100,
            age = 40,
            use_own_eggs = True,
            used_ivf_in_past = False,
            know_reason_for_infertility = True,
            number_of_live_births = 1,
            number_of_prior_pregnancies = 1,
            male_factor_infertility = True,
            endometriosis = True,
            tubal_factor = True,
            ovulatory_disorder = True,
            diminished_ovarian_reserve = True,
            uterine_factor = True,
            other_reason_unexplained = True,
        )

        print(score)
