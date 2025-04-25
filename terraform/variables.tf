variable "databricks_host" {
  description = "URL do workspace Databricks"
  type        = string
}

variable "databricks_token" {
  description = "Token de acesso ao Databricks"
  type        = string
}

variable "gcs_service_account_email" {
  description = "Email da service account que o Databricks usará"
  type        = string
}

variable "external_locations" {
  description = "Lista de external locations com nome e GCS bucket URL"
  type = list(object({
    name = string
    gcs_bucket_url = string
  }))
}
