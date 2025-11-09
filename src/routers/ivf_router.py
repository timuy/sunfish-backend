

from fastapi import APIRouter

from src.schemas.ivf import IvfEstimatorRequest, IvfEstimatorResponse
from src.services.ivf import IvfService


router = APIRouter(prefix="/ivf", tags=["IVF"])


@router.post("/estimator",
    summary="Get Score for IVF Success Estimator",
    description="Get Score for IVF Success Estimator",
)
async def get_ivf_success_rate(request: IvfEstimatorRequest) -> IvfEstimatorResponse:


    success_rate = IvfService.calculate_ivf_estimator_success_rate(
            height_feet = request.background_history.height_feet,
            height_inches = request.background_history.height_inches,
            weight = request.background_history.weight,
            age = request.background_history.age,
            use_own_eggs = request.background_history.use_own_eggs,
            used_ivf_in_past = request.background_history.used_ivf_in_past,
            know_reason_for_infertility = request.background_history.know_reason_for_infertility,
            number_of_live_births = request.background_history.number_of_live_births,
            number_of_prior_pregnancies = request.background_history.number_of_prior_pregnancies,
            male_factor_infertility = request.diagnosis_and_plan.male_factor_infertility,
            endometriosis = request.diagnosis_and_plan.endometriosis,
            tubal_factor = request.diagnosis_and_plan.tubal_factor,
            ovulatory_disorder = request.diagnosis_and_plan.ovulatory_disorder,
            diminished_ovarian_reserve = request.diagnosis_and_plan.diminished_ovarian_reserve,
            uterine_factor = request.diagnosis_and_plan.uterine_factor,
            other_reason_unexplained = request.diagnosis_and_plan.other_reason_unexplained,
        )
    return IvfEstimatorResponse(success_rate=success_rate)
