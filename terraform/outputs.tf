output "external_location_names" {
  value = [for loc in databricks_external_location.gcs_external_location : loc.name]
}

output "external_location_url" {
  value = [for loc in databricks_external_location.gcs_external_location : loc.url]
}
