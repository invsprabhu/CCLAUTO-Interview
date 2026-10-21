output "results" {
  description = "JSON response from the NetworkCalc subnet API"
  value       = jsondecode(data.http.api_url.response_body)
}
