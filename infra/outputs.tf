output "cloud_run_url" {
  description = "URL of the Cloud Run service"
  value       = google_cloud_run_service.a_proper_one.status[0].url
}

output "service_name" {
  description = "Name of the Cloud Run service"
  value       = google_cloud_run_service.a_proper_one.name
}

output "project_id" {
  description = "GCP Project ID"
  value       = var.project_id
}
