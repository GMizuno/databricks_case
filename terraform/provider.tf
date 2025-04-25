terraform {
  required_providers {
    databricks = {
      source  = "databricks/databricks"
      version = "~> 1.71.0" # ou a versão mais recente
    }
  }

  required_version = ">= 1.2.0"
}

provider "databricks" {
  host  = var.databricks_host
  token = var.databricks_token
}
