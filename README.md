# A Proper One - Noxus Plugin

A sample Noxus plugin demonstrating the framework's capabilities with full CI/CD and infrastructure setup on GCP via terraform.

## Project Structure

```
TestN/
├── app/
│   └── a_proper_one/               # Main plugin directory
│       ├── a_proper_one.py         # Plugin implementation
│       ├── a_proper_one.yaml       # Plugin configuration
│       ├── Dockerfile              # Container definition (artifact, deployed images are built on the pipeline)
│       ├── pyproject.toml          # Python dependencies (cli still being installed via git)
│       ├── docker-compose.*.yml    # Local deployment
│       └── tests/  
│           ├── unit                # Tests for actual business plugin logic
│           └── integration         # To run on CI/CD pipeline - basic endpoint and config checks against image to be deployed   
|   
├── infra/                          # Terraform infrastructure
│   ├── main.tf                     # Main Terraform config
│   ├── variables.tf                # Input variables
│   ├── outputs.tf                  # Output values
│   └── terraform.tfvars            # Default variable values for local `terraform run` runs
|
├── .github/
│   └── workflows/
│       └── deploy.yml        # CI/CD pipeline
```

## Quick Start

### Prerequisites

- Python 3.9+
- Docker
- Terraform (for infrastructure)
- GCP account (for cloud deployment)

### Local Development

1. **Install dependencies:**
   ```bash
   pip install git+https://github.com/lawst-code/Noxus.git
   pip install -e .
   ```

2. **Run locally:**
   ```bash
   noxus serve --plugin a_proper_one.yaml
   ```

3. **Build and run with Docker:**
   ```bash
   noxus build
   cd app/a_proper_one
   docker-compose -f docker-compose.a_proper_one.standalone.yml up --build
   ```

4. **Test the API:**
   - Swagger UI: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc


## Infrastructure

The infrastructure is defined using Terraform and deploys to Google Cloud Platform:

- **Cloud Run**: Serverless container hosting
- **Container Registry**: Docker image storage
- **IAM**: Access control and permissions


## CI/CD Pipeline

The GitHub Actions workflow automatically:

1. **On Pull Requests:**
   - Runs tests
   - Builds Docker image (for immediate local running/testing/etc)

2. **On Push to Main:**
   - Runs full test suite
   - Builds and pushes Docker image
   - Deploys to Cloud Run
   - Updates infrastructure via Terraform