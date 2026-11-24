# AWS SAA-C03 — Laboratórios práticos

Programa de estudos com laboratórios práticos para a certificação **AWS Certified Solutions Architect – Associate (SAA-C03)**. O objetivo é relacionar decisões de arquitetura à operação dos serviços AWS, com atenção a segurança, resiliência, desempenho e custos.

Este repositório combina arquitetura AWS, Terraform, CI/CD, segurança, governança, FinOps e documentação técnica. Os LABs 00 e 01 foram executados e validados pelo responsável; a infraestrutura do LAB 01 foi destruída após a validação. O repositório contém código provisionável, mas o CI executa somente verificações estáticas, sem acesso à AWS.

## Plataforma evolutiva

Os laboratórios formam uma **plataforma AWS evolutiva e cumulativa**, organizada em uma sequência lógica de evolução arquitetural. Recursos e configurações de um LAB podem ser reutilizados por LABs posteriores quando houver uma relação técnica real, inclusive em estudos para outras certificações AWS. A fundação deve permitir essa evolução sem reconstrução desnecessária.

Cada LAB deve identificar seus pré-requisitos, recursos herdados, recursos novos, dependências e possibilidades de reutilização futura, com referências ao LAB de origem. Recursos compartilhados devem registrar sua origem, consumidores conhecidos e responsabilidade por manutenção e ciclo de vida. A documentação deve distinguir recursos existentes e confirmados, recursos planejados e opções ainda não adotadas, sem presumir dependências ou provisionamento futuro.

O cleanup deve preservar recursos necessários aos LABs posteriores. Recursos temporários devem ser removidos quando deixarem de ser necessários, após revisão das dependências e aprovação humana, para controlar custos. Recursos legados, treinamentos externos, incidentes históricos e configurações particulares que não pertençam à plataforma ficam fora da documentação. As regras completas estão em [AGENTS.md](AGENTS.md).

O LAB 00 fornece a base de identidade e governança. O LAB 01 implementa a fundação de rede em duas AZs; sua reutilização depende de novo provisionamento autorizado. Os LABs 02–05 permanecem planejados.

## Objetivos

- Utilizar acesso federado, MFA e credenciais temporárias.
- Aplicar menor privilégio e separar administração de operação.
- Registrar procedimentos reproduzíveis, critérios de aceite e limites das validações.
- Evoluir os próximos laboratórios sem antecipar recursos ou implementações.

## Pré-requisitos

- Conta AWS sob responsabilidade do participante e acesso administrativo autorizado para a configuração inicial.
- Conhecimentos básicos de IAM, redes e terminal Linux.
- AWS CLI v2 no ambiente de estudo.
- Navegador e dispositivo MFA compatível com IAM Identity Center.
- Revisão de custos e do escopo de cada laboratório antes de qualquer execução futura.

Não use a identidade operacional do LAB 00 para administrar Organizations ou IAM Identity Center: sua política permite apenas as consultas especificadas.

## Índice dos laboratórios

| Laboratório | Tema | Situação |
| --- | --- | --- |
| [LAB 00](labs/lab00-identity-governance/README.md) | Organizations, IAM Identity Center, SSO, MFA e governança | Executado; documentado a partir do histórico confirmado |
| [LAB 01](labs/lab01-vpc-networking/README.md) | VPC e networking com Terraform | Executado, validado e destruído; sem testes entre workloads |
| LAB 02 — `lab02-s3-security` | Segurança no Amazon S3 | Planejado |
| LAB 03 — `lab03-lambda-api-gateway` | AWS Lambda e Amazon API Gateway | Planejado |
| LAB 04 — `lab04-sqs-sns` | Amazon SQS e Amazon SNS | Planejado |
| LAB 05 — `lab05-cloudwatch` | Amazon CloudWatch | Planejado |

Os LABs implementados ficam em `labs/labNN-tema/`, com README e subdiretórios conforme a necessidade. O LAB 01 mantém seu diretório raiz Terraform em `terraform/`; `shared/scripts/` contém a descoberta de diretórios raiz e `.github/workflows/` contém o [Terraform CI](.github/workflows/terraform-ci.yml). Não criamos diretórios de preenchimento para LABs futuros.

## Convenções

- Toda a documentação em português brasileiro (pt-BR), incluindo os LABs atuais e futuros, relatórios, diagramas e comentários explicativos. Preserve termos técnicos consolidados e identificadores de código em inglês; commits seguem Conventional Commits em inglês.
- Diretórios em `kebab-case`, laboratórios em `labNN-tema` e documentos Markdown com nomes descritivos.
- Região de referência do LAB 00: `sa-east-1`; perfil CLI: `aws-saa-labs`.
- Comandos publicados são instruções para execução humana, não prova de execução. Resultados históricos ficam identificados em [validação](labs/lab00-identity-governance/docs/validation.md).
- Identificadores de conta, usuários, URLs privadas do portal, ARNs reais, tokens, credenciais e capturas sem sanitização não devem ser publicados.
- Branches dedicadas, Conventional Commits e PRs com revisão humana. Commit e push de agentes dependem de autorização da tarefa; merge permanece humano. Veja [CONTRIBUTING.md](CONTRIBUTING.md) e [AGENTS.md](AGENTS.md).

## Segurança e custos

A política do LAB 00 é de leitura e não autoriza a criação ou remoção de infraestrutura. O Permission Set foi atribuído na conta de gerenciamento por simplificação educacional; para workloads, recomenda-se utilizar contas-membro dedicadas.

As validações de identidade e acesso **não comprovam ausência de cobranças na conta**. Consulte as [orientações de reversão do LAB 00](labs/lab00-identity-governance/docs/cleanup.md) antes de desativar acessos ou configurações.

## Validação de engenharia

O CI descobre os diretórios raiz Terraform versionados, executa `fmt`, `init -backend=false -lockfile=readonly` e `validate` em matriz, sem credenciais AWS e sem provisionamento. Actions são fixadas por SHA; Terraform permanece na versão 1.15.8 e o provider AWS está travado em 6.74.0. Consulte os procedimentos em [CONTRIBUTING.md](CONTRIBUTING.md) e as decisões e limitações da [revisão de engenharia](docs/lab01-engineering-review.md).

Para reproduzir o LAB 01, use seu próprio perfil temporário e configure o ID da conta autorizada apenas em arquivo local ignorado. Consulte os pré-requisitos e as instruções completas no README do LAB.
