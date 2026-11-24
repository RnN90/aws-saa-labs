variable "aws_account_id" {
  description = "Authorized AWS account ID. Set locally; the provider rejects any other account."
  type        = string
  nullable    = false

  validation {
    condition     = can(regex("^[0-9]{12}$", var.aws_account_id))
    error_message = "aws_account_id must contain exactly 12 digits."
  }
}

variable "aws_region" {
  description = "AWS Region for the lab; keep sa-east-1 for the validated architecture."
  type        = string
  default     = "sa-east-1"
  nullable    = false

  validation {
    condition     = can(regex("^[a-z]{2}(-[a-z]+)+-[0-9]+$", var.aws_region))
    error_message = "aws_region must be a valid AWS Region name."
  }
}

variable "aws_profile" {
  description = "AWS CLI SSO profile. Set null to use the standard AWS credential chain."
  type        = string
  default     = "aws-saa-labs"

  validation {
    condition     = var.aws_profile == null ? true : length(trimspace(var.aws_profile)) > 0
    error_message = "aws_profile must be null or a non-empty profile name."
  }
}

variable "vpc_cidr" {
  description = "IPv4 CIDR of the VPC; keep 10.10.0.0/16 for the validated architecture."
  type        = string
  default     = "10.10.0.0/16"
  nullable    = false

  validation {
    condition     = can(cidrnetmask(var.vpc_cidr))
    error_message = "vpc_cidr must be a valid IPv4 CIDR."
  }
}

variable "availability_zones" {
  description = "Two distinct AZ names in aws_region, ordered to match the subnet CIDR lists."
  type        = list(string)
  default     = ["sa-east-1a", "sa-east-1b"]
  nullable    = false

  validation {
    condition = length(var.availability_zones) == 2 && length(distinct(var.availability_zones)) == 2 && alltrue([
      for az in var.availability_zones : can(regex("^${var.aws_region}[a-z]$", az))
    ])
    error_message = "Provide two distinct AZ names belonging to aws_region."
  }
}

variable "public_subnet_cidrs" {
  description = "Two distinct public IPv4 subnet CIDRs, indexed in availability_zones order."
  type        = list(string)
  default     = ["10.10.1.0/24", "10.10.2.0/24"]
  nullable    = false

  validation {
    condition = length(var.public_subnet_cidrs) == length(var.availability_zones) && length(distinct(var.public_subnet_cidrs)) == 2 && alltrue([
      for cidr in var.public_subnet_cidrs : can(cidrnetmask(cidr))
    ])
    error_message = "Provide two distinct IPv4 CIDRs matching the AZ list length."
  }
}

variable "private_subnet_cidrs" {
  description = "Two distinct private IPv4 subnet CIDRs, indexed in availability_zones order."
  type        = list(string)
  default     = ["10.10.11.0/24", "10.10.12.0/24"]
  nullable    = false

  validation {
    condition = length(var.private_subnet_cidrs) == length(var.availability_zones) && length(distinct(var.private_subnet_cidrs)) == 2 && alltrue([
      for cidr in var.private_subnet_cidrs : can(cidrnetmask(cidr))
    ])
    error_message = "Provide two distinct IPv4 CIDRs matching the AZ list length."
  }
}
