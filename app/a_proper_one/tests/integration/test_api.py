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
        test_data = {"input_text": "ayo"}
        response = requests.post(
            f"{self.BASE_URL}/nodes/a_proper_one-node", json=test_data
        )
        assert response.status_code == 200

        result = response.json()
        assert "result" in result
        assert result["result"] == "ayo"

    def check_yaml_config(self):
        """Check that the yaml config is valid"""
        with open("a_proper_one.yaml", "r") as f:
            config = yaml.safe_load(f)
        assert config is not None
        assert (
            config["important_nuclear_code_which_should_fail_the_build_if_wrong"] == "n"
        )
