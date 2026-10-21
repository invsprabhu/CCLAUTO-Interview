terraform {
  required_providers {
    http = {
      source  = "hashicorp/http"
      version = "~> 3.0"
    }
  }
}

data "http" "api_url" {
  url    = "${trimsuffix(var.base, "/")}/${var.subnet}/${var.mask}"
  method = "GET"

  request_headers = {
    Accept = "application/json"
  }
}
