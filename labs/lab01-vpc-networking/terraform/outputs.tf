output "vpc_id" {
  description = "ID da VPC do laboratório."
  value       = aws_vpc.lab.id
}

output "public_subnet_ids" {
  description = "IDs das subnets públicas, na ordem de availability_zones."
  value       = aws_subnet.public[*].id
}

output "private_subnet_ids" {
  description = "IDs das subnets privadas, na ordem de availability_zones."
  value       = aws_subnet.private[*].id
}

output "internet_gateway_id" {
  description = "ID do Internet Gateway anexado à VPC do laboratório."
  value       = aws_internet_gateway.lab.id
}

output "public_route_table_id" {
  description = "ID da Route Table com a rota padrão para o Internet Gateway."
  value       = aws_route_table.public.id
}

output "private_route_table_id" {
  description = "ID da Route Table que contém somente a rota local da VPC."
  value       = aws_route_table.private.id
}
