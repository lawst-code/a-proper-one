import pytest
import requests
import yaml


# Really only to be run in the pipeline
class TestAPIIntegration:
    """Basic endpoint checking"""

    # Base URL for the running container (set by CI/CD pipeline)
    BASE_URL = "http://localhost:8000"

    def test_node_endpoint(self):
        """Test the main node endpoint"""
        test_data = {"inputs": {"input_text": "SSss"}}
        response = requests.post(
            f"{self.BASE_URL}/nodes/a_proper_one-node/run", json=test_data
        )
        assert response.status_code == 200

        result = response.json()
        assert "result" in result
        assert result["result"] == "ayo"