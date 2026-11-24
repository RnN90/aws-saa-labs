variable "aws_account_id" {
  description = "ID da conta AWS autorizada. Informe localmente; o provider rejeita qualquer outra conta."
  type        = string
  nullable    = false

  validation {
    condition     = can(regex("^[0-9]{12}$", var.aws_account_id))
    error_message = "aws_account_id deve conter exatamente 12 dígitos."
  }
}

variable "aws_region" {
  description = "Região AWS do laboratório; mantenha sa-east-1 para reproduzir a arquitetura validada."
  type        = string
  default     = "sa-east-1"
  nullable    = false

  validation {
    condition     = can(regex("^[a-z]{2}(-[a-z]+)+-[0-9]+$", var.aws_region))
    error_message = "aws_region deve ser um nome válido de região AWS."
  }
}

variable "aws_profile" {
  description = "Perfil SSO da AWS CLI. Defina null para usar a cadeia padrão de credenciais AWS."
  type        = string
  default     = "aws-saa-labs"

  validation {
    condition     = var.aws_profile == null ? true : length(trimspace(var.aws_profile)) > 0
    error_message = "aws_profile deve ser null ou um nome de perfil não vazio."
  }
}

variable "vpc_cidr" {
  description = "CIDR IPv4 da VPC; mantenha 10.10.0.0/16 para reproduzir a arquitetura validada."
  type        = string
  default     = "10.10.0.0/16"
  nullable    = false

  validation {
    condition     = can(cidrnetmask(var.vpc_cidr))
    error_message = "vpc_cidr deve ser um CIDR IPv4 válido."
  }
}

variable "availability_zones" {
  description = "Nomes de duas AZs distintas em aws_region, na mesma ordem das listas de CIDRs das subnets."
  type        = list(string)
  default     = ["sa-east-1a", "sa-east-1b"]
  nullable    = false

  validation {
    condition = length(var.availability_zones) == 2 && length(distinct(var.availability_zones)) == 2 && alltrue([
      for az in var.availability_zones : can(regex("^${var.aws_region}[a-z]$", az))
    ])
    error_message = "Informe nomes de duas AZs distintas pertencentes a aws_region."
  }
}

variable "public_subnet_cidrs" {
  description = "Dois CIDRs IPv4 distintos para subnets públicas, na ordem de availability_zones."
  type        = list(string)
  default     = ["10.10.1.0/24", "10.10.2.0/24"]
  nullable    = false

  validation {
    condition = length(var.public_subnet_cidrs) == length(var.availability_zones) && length(distinct(var.public_subnet_cidrs)) == 2 && alltrue([
      for cidr in var.public_subnet_cidrs : can(cidrnetmask(cidr))
    ])
    error_message = "Informe dois CIDRs IPv4 distintos, com a mesma quantidade de entradas da lista de AZs."
  }
}

variable "private_subnet_cidrs" {
  description = "Dois CIDRs IPv4 distintos para subnets privadas, na ordem de availability_zones."
  type        = list(string)
  default     = ["10.10.11.0/24", "10.10.12.0/24"]
  nullable    = false

  validation {
    condition = length(var.private_subnet_cidrs) == length(var.availability_zones) && length(distinct(var.private_subnet_cidrs)) == 2 && alltrue([
      for cidr in var.private_subnet_cidrs : can(cidrnetmask(cidr))
    ])
    error_message = "Informe dois CIDRs IPv4 distintos, com a mesma quantidade de entradas da lista de AZs."
  }
}
