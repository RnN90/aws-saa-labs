output "vpc_id" {
  description = "ID of the lab VPC."
  value       = aws_vpc.lab.id
}

output "public_subnet_ids" {
  description = "Public subnet IDs in availability_zones order."
  value       = aws_subnet.public[*].id
}

output "private_subnet_ids" {
  description = "Private subnet IDs in availability_zones order."
  value       = aws_subnet.private[*].id
}

output "internet_gateway_id" {
  description = "ID of the Internet Gateway attached to the lab VPC."
  value       = aws_internet_gateway.lab.id
}

output "public_route_table_id" {
  description = "ID of the route table with the Internet Gateway default route."
  value       = aws_route_table.public.id
}

output "private_route_table_id" {
  description = "ID of the route table containing only the VPC local route."
  value       = aws_route_table.private.id
}
