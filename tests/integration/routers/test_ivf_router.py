
from fastapi.testclient import TestClient

from src.app import app

class TestIVFEndpoint:
    """Testing IVF Endpoint."""

    def test_endpoint(self):
        """Testing IVF endpoint."""

        client = TestClient(app)
        response = client.post(
                "/ivf/estimator",
                json = {
                    "background_history": {
                        "height_feet": 5,
                        "height_inches": 7,
                        "weight": 130,
                        "age": 25,
                        "use_own_eggs": True,
                        "used_ivf_in_past":True,
                        "know_reason_for_infertility": True,
                        "number_of_live_births": 1,
                        "number_of_prior_pregnancies": 1
                    },
                    "diagnosis_and_plan": {
                        "male_factor_infertility": False,
                        "endometriosis": False,
                        "tubal_factor": False,
                        "ovulatory_disorder": False,
                        "diminished_ovarian_reserve": False,
                        "uterine_factor": False,
                        "other_reason_unexplained": False
                    }
                }
        )

        assert response.status_code == 200
        response_json = response.json()

        assert response_json["success_rate"] is not None
