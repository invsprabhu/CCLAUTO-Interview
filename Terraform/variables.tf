variable "base" {
  description = "Base URL for the NetworkCalc API"
  type        = string
}

variable "subnet" {
  description = "IPv4 subnet address"
  type        = string
}

variable "mask" {
  description = "IPv4 CIDR prefix length (0 through 32)"
  type        = number
  validation {
    condition     = var.mask >= 0 && var.mask <= 32 && floor(var.mask) == var.mask
    error_message = "mask must be a whole number between 0 and 32."
  }
}
