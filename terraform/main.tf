resource "databricks_external_location" "gcs_external_location" {
  for_each        = {for loc in var.external_locations : loc.name => loc}
  name            = each.value.name
  url             = each.value.gcs_bucket_url
  credential_name = "databricks-study"
  comment         = "External location apontando para GCS: ${each.value.gcs_bucket_url}"
}
