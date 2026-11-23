# LAB 00 — Governança de identidades

**Situação:** executado e validado conforme histórico fornecido pelo responsável. Esta documentação não representa nova execução ou auditoria da conta.

## Objetivos

- Centralizar identidades no IAM Identity Center integrado ao AWS Organizations.
- Exigir MFA em todos os logins e conceder acesso por grupo (RBAC).
- Utilizar SSO na AWS CLI v2 e credenciais temporárias AWS STS.
- Aplicar a política IAM aprovada de leitura e documentar seus limites de autorização.
- Documentar a reversão das configurações do LAB e as dependências de acesso.

## Arquitetura e serviços

| Componente | Configuração confirmada |
| --- | --- |
| AWS Organizations | Todas as funcionalidades habilitadas; conta de gerenciamento existente |
| IAM Identity Center | Instância organizacional em `sa-east-1` |
| Fonte de identidades | Diretório integrado do IAM Identity Center |
| Identidade e grupo | Usuário configurado; grupo `AWS-SAA-Labs` |
| MFA | Exigido em todos os logins |
| Permission Set | `SAA-Lab-Operator`, atribuído ao grupo na conta de gerenciamento, por simplificação educacional |
| Sessão da conta AWS | Uma hora, definida no Permission Set |
| Cliente | AWS CLI v2; perfil `aws-saa-labs`, região padrão `sa-east-1` |
| Acesso a serviços | AWS STS, consultas Organizations e operações EC2 de leitura |

O nome do usuário, identificadores da conta e URL do portal não são publicados. Não há conta membro adicional, OU ou SCP documentada como implementada.

Para workloads, recomenda-se utilizar contas-membro dedicadas e restringir a conta de gerenciamento às responsabilidades administrativas. Veja as [decisões de arquitetura](docs/architecture.md).

## Fluxo de autenticação

O usuário inicia SSO, autentica-se no diretório integrado com MFA e recebe acesso conforme a associação ao grupo. A atribuição do Permission Set à conta provisiona uma role controlada pelo IAM Identity Center, com prefixo `AWSReservedSSO`. Console e CLI utilizam sessões temporárias dessa role; as chamadas aos serviços são autorizadas pela política correspondente.

A sessão de uma hora limita as credenciais da conta AWS. A sessão de autenticação do portal/SSO tem configuração própria; uma nova chamada CLI não implica novo desafio MFA. Veja [arquitetura](docs/architecture.md) e [diagramas](diagrams/identity-architecture.md).

## Etapas e documentação

1. [Arquitetura e limites de segurança](docs/architecture.md).
2. [Procedimento de implementação: Console e CLI](docs/implementation.md).
3. [Política IAM validada](iam/policies/saa-lab-operator.json).
4. [Validação: histórico, comandos e critérios de aceite](docs/validation.md).
5. [Reversão das configurações e preservação de acesso](docs/cleanup.md).

Os comandos publicados são para reprodução humana. O agente não os executou na AWS nem alterou configurações locais ou sessões SSO.

## Resultado e limites

Foram confirmados acesso STS, consulta da organização e autorização de leitura EC2 pela política aprovada. As permissões EC2 são preservadas como parte dessa política; inventários de rede não são requisitos de validação deste LAB.

Não há saídas brutas ou capturas anexadas. As validações documentadas não comprovam ausência de cobranças nem uma análise completa de permissões efetivas.
