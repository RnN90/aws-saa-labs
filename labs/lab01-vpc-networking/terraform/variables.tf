variable "aws_region" {
  description = "Regiao AWS do laboratorio"
  type        = string
  default     = "sa-east-1"
}

variable "aws_profile" {
  description = "Perfil AWS CLI autenticado via SSO"
  type        = string
  default     = "aws-saa-labs"
}

variable "vpc_cidr" {
  description = "CIDR da VPC"
  type        = string
  default     = "10.10.0.0/16"
}

variable "availability_zones" {
  description = "Availability Zones do laboratorio"
  type        = list(string)
  default     = ["sa-east-1a", "sa-east-1b"]
}

variable "public_subnet_cidrs" {
  type    = list(string)
  default = ["10.10.1.0/24", "10.10.2.0/24"]
}

variable "private_subnet_cidrs" {
  type    = list(string)
  default = ["10.10.11.0/24", "10.10.12.0/24"]
}
