terraform {
  required_version = ">= 1.0"
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
}

provider "google" {
  project = var.project_id
  region  = var.region
}

# Enable required APIs
resource "google_project_service" "cloud_run_api" {
  service = "run.googleapis.com"
}

resource "google_project_service" "container_registry_api" {
  service = "containerregistry.googleapis.com"
}

resource "google_project_service" "cloud_build_api" {
  service = "cloudbuild.googleapis.com"
}

# Actual config for service
resource "google_cloud_run_service" "a_proper_one" {
  name     = "a-proper-one-plugin"
  location = var.region

  template {
    spec {
      containers {
        image = var.container_image

        ports {
          container_port = 8000
        }

        env {
          name  = "PORT"
          value = "8000"
        }

        resources {
          limits = {
            cpu    = "1000m"
            memory = "512Mi"
          }
        }
      }

      container_concurrency = 100
      timeout_seconds      = 300
    }

    metadata {
      annotations = {
        "autoscaling.knative.dev/minScale" = "0"
        "autoscaling.knative.dev/maxScale" = "10"
        "run.googleapis.com/execution-environment" = "gen2"
      }
    }
  }

  traffic {
    percent         = 100
    latest_revision = true
  }

  depends_on = [google_project_service.cloud_run_api]
}

# IAM policy to allow unauthenticated access
# Not setting up proper auth in this example (for now)
resource "google_cloud_run_service_iam_member" "public_access" {
  location = google_cloud_run_service.a_proper_one.location
  project  = google_cloud_run_service.a_proper_one.project
  service  = google_cloud_run_service.a_proper_one.name
  role     = "roles/run.invoker"
  member   = "allUsers"
}
