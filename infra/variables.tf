variable "project_id" {
  description = "The GCP project ID"
  type        = string
}

variable "repository_id" {
  description = "The Artifact Registry repository ID"
  type        = string
}

variable "region" {
  description = "The GCP region for resources"
  type        = string
  default     = "europe-west1"
}

variable "container_image" {
  description = "The container image URL for the Cloud Run service"
  type        = string
  default     = "gcr.io/PROJECT_ID/a-proper-one:latest"
}
