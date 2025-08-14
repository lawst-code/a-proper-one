# Infrastructure

This directory contains the Terraform configuration for deploying the 'A Proper One' infra to Google Cloud Platform (on Cloud Run).


## Validating changes:

1. Mind the variables file (optional for now, really):
   ```bash
   cp terraform.tfvars.example terraform.tfvars
   ```

2. Set the `terraform.tfvars` variables file (optional, really) with project details. Defaults are mostly sensible right now:
   ```hcl
   project_id = "your-gcp-project-id"
   region     = "some-place"
   environment = "dev"
   ```

3. Initialize Terraform:
   ```bash
   terraform init
   ```

4. Plan the deployment:
   ```bash
   terraform plan
   ```

5. Apply the configuration. Shouldn't apply locally - pipeline will run this for all pushed commits. Also means the 'latest' tag logic should really be implemented (see `terraform.tfvars`):
   ```bash
   terraform apply
   ```