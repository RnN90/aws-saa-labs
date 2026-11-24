provider "aws" {
  region              = var.aws_region
  profile             = var.aws_profile
  allowed_account_ids = [var.aws_account_id]

  default_tags {
    tags = {
      Project     = "aws-saa-labs"
      Lab         = "lab01"
      Environment = "lab"
      ManagedBy   = "Terraform"
    }
  }
}
