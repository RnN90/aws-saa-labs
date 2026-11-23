# AWS SAA-C03 — Laboratórios práticos

Programa de estudos com laboratórios hands-on para a certificação **AWS Certified Solutions Architect – Associate (SAA-C03)**. O objetivo é relacionar decisões de arquitetura à operação dos serviços AWS, com atenção a segurança, resiliência, desempenho e custos.

Este repositório começa pela governança de identidades. O LAB 00 já foi executado e validado; esta entrega documenta o histórico informado pelo responsável. Nenhum recurso AWS é provisionado pelos arquivos desta etapa.

## Objetivos

- Utilizar acesso federado, MFA e credenciais temporárias.
- Aplicar menor privilégio e separar administração de operação.
- Registrar procedimentos reproduzíveis, critérios de aceite e limites das validações.
- Evoluir os próximos laboratórios sem antecipar recursos ou implementações.

## Pré-requisitos

- Conta AWS sob responsabilidade do participante e acesso administrativo autorizado para a configuração inicial.
- Conhecimentos básicos de IAM, redes e terminal Linux.
- AWS CLI v2 no ambiente de estudo; a execução histórica ocorreu no Ubuntu.
- Navegador e dispositivo MFA compatível com IAM Identity Center.
- Revisão de custos e do escopo de cada laboratório antes de qualquer execução futura.

Não use a identidade operacional do LAB 00 para administrar Organizations ou IAM Identity Center: sua política permite apenas as consultas especificadas.

## Índice dos laboratórios

| Laboratório | Tema | Situação |
| --- | --- | --- |
| [LAB 00](labs/lab00-identity-governance/README.md) | Organizations, IAM Identity Center, SSO, MFA e governança | Executado; documentado a partir do histórico confirmado |
| LAB 01 — `lab01-vpc-networking` | VPC e networking | Planejado |
| LAB 02 — `lab02-s3-security` | Segurança no Amazon S3 | Planejado |
| LAB 03 — `lab03-lambda-api-gateway` | AWS Lambda e Amazon API Gateway | Planejado |
| LAB 04 — `lab04-sqs-sns` | Amazon SQS e Amazon SNS | Planejado |
| LAB 05 — `lab05-cloudwatch` | Amazon CloudWatch | Planejado |

Os diretórios dos LABs 01–05, `shared/scripts`, `shared/templates` e `.github/workflows` são reservados para uso futuro. Diretórios vazios não são versionados pelo Git; não há implementação, scripts ou workflows nesses espaços nesta etapa.

## Convenções

- Documentação em português brasileiro; nomes de serviços e campos do Console em inglês quando necessário.
- Diretórios em `kebab-case`, laboratórios em `labNN-tema` e documentos Markdown com nomes descritivos.
- Região de referência do LAB 00: `sa-east-1`; perfil CLI: `aws-saa-labs`.
- Comandos publicados são instruções para execução humana, não prova de execução. Resultados históricos ficam identificados em [validação](labs/lab00-identity-governance/docs/validation.md).
- Identificadores de conta, usuários, URLs privadas do portal, ARNs reais, tokens, credenciais e capturas sem sanitização não devem ser publicados.
- Alterações devem passar por revisão humana; agentes não fazem commit, push ou Pull Request automaticamente. Veja [AGENTS.md](AGENTS.md).

## Segurança e custos

A política do LAB 00 é de leitura e não autoriza a criação ou remoção de infraestrutura. A VPC personalizada legada foi removida manualmente; a VPC padrão foi preservada. A auditoria histórica identificou zero NAT Gateways, zero Elastic IPs alocados e zero VPC Endpoints em `sa-east-1`.

Esse resultado é restrito aos recursos e à região consultados. **Não comprova ausência de cobranças na conta**, pois não houve auditoria completa de todos os serviços e regiões. Consulte as [orientações de limpeza e custos](labs/lab00-identity-governance/docs/cleanup.md).
