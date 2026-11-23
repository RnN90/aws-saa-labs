# LAB 00 — Governança de identidades

**Situação:** executado e validado conforme histórico fornecido pelo responsável. Esta documentação não representa nova execução ou auditoria da conta.

## Objetivos

- Centralizar identidades no IAM Identity Center integrado ao AWS Organizations.
- Exigir MFA em todos os logins e conceder acesso por grupo (RBAC).
- Utilizar SSO na AWS CLI v2 e credenciais temporárias AWS STS.
- Conceder somente as leituras de Organizations e networking necessárias nesta etapa.
- Registrar a limpeza histórica e os limites da verificação de custos.

## Arquitetura e serviços

| Componente | Configuração confirmada |
| --- | --- |
| AWS Organizations | Todas as funcionalidades habilitadas; conta de gerenciamento existente |
| IAM Identity Center | Instância organizacional em `sa-east-1` |
| Fonte de identidades | Diretório integrado do IAM Identity Center |
| Identidade e grupo | Usuário configurado; grupo `AWS-SAA-Labs` |
| MFA | Exigido em todos os logins |
| Permission Set | `SAA-Lab-Operator`, atribuído ao grupo na conta AWS |
| Sessão da conta AWS | Uma hora, definida no Permission Set |
| Cliente | AWS CLI v2 no Ubuntu; perfil `aws-saa-labs`, região padrão `sa-east-1` |
| Acesso a serviços | AWS STS, consultas Organizations e operações EC2 de leitura |

O nome do usuário, identificadores da conta e URL do portal não são publicados. Não há conta membro adicional, OU ou SCP documentada como implementada.

## Fluxo de autenticação

O usuário inicia SSO, autentica-se no diretório integrado com MFA e recebe acesso conforme a associação ao grupo. A atribuição do Permission Set à conta provisiona uma role controlada pelo IAM Identity Center, com prefixo `AWSReservedSSO`. Console e CLI utilizam sessões temporárias dessa role; as chamadas aos serviços são autorizadas pela política correspondente.

A sessão de uma hora limita as credenciais da conta AWS. A sessão de autenticação do portal/SSO tem configuração própria; uma nova chamada CLI não implica novo desafio MFA. Veja [arquitetura](docs/architecture.md) e [diagramas](diagrams/identity-architecture.md).

## Etapas e documentação

1. [Arquitetura e limites de segurança](docs/architecture.md).
2. [Procedimento de implementação: Console e CLI](docs/implementation.md).
3. [Política IAM validada](iam/policies/saa-lab-operator.json).
4. [Validação: histórico, comandos e critérios de aceite](docs/validation.md).
5. [Limpeza, preservação de acesso e custos](docs/cleanup.md).

Os comandos publicados são para reprodução humana. O agente não os executou na AWS nem alterou configurações locais ou sessões SSO.

## Resultado e limites

Foram confirmados acesso STS, consulta da organização e autorização de leitura EC2. Uma VPC personalizada legada foi removida manualmente e a VPC padrão foi preservada. A auditoria final encontrou zero NAT Gateways, zero Elastic IPs alocados e zero VPC Endpoints em `sa-east-1`.

Não há saídas brutas ou capturas anexadas. O histórico não comprova uma auditoria de todos os serviços/regiões nem ausência de cobranças. A remoção da VPC não foi realizada com a política operacional publicada, que não permite exclusão; a identidade utilizada nessa limpeza não foi informada.
