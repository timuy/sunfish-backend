from typing import Optional

from pydantic import BaseModel, Field, ValidationError, model_validator


class IvfBackground(BaseModel):
    """Background information."""
    age: int = Field(..., ge=20, le=50) # age is greater than or equal to 20 but less than or equal to 50
    weight: int = Field(..., ge=80, le=300) # weight is greater than or equal to 80 but less than or equal to 300
    height_feet: int
    height_inches: int
    number_of_live_births: int = Field(..., ge=0) # must be greater than or equal to zero
    number_of_prior_pregnancies: int = Field(..., ge=0) # must be greater than or equal to zero
    use_own_eggs: bool
    used_ivf_in_past: Optional[bool] = None
    know_reason_for_infertility: bool

    @model_validator(mode='after')
    def validate_live_births(self):
        if self.number_of_live_births > self.number_of_prior_pregnancies:
            raise ValidationError("Number of live births can not exceed number of prior pregnancies")
        return self

    @model_validator(mode='after')
    def validate_used_ivf_in_past(self):
        if self.used_ivf_in_past and not self.use_own_eggs:
            raise ValidationError("Used IVF in the past is None if member is not want to use own eggs")
        return self


class IvfDiagnosisAndPlan(BaseModel):
    """Diagnosis and Plan information."""
    male_factor_infertility: bool
    endometriosis: bool
    tubal_factor: bool
    ovulatory_disorder: bool
    diminished_ovarian_reserve: bool
    uterine_factor: bool
    other_reason_unexplained: bool


class IvfEstimatorRequest(BaseModel):
    """IVF Estimator Request."""
    background_history: IvfBackground
    diagnosis_and_plan: IvfDiagnosisAndPlan


class IvfEstimatorResponse(BaseModel):
    """IVF Estimator Response."""
    success_rate: float
