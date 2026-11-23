# Validação — LAB 00

## Origem e limites do registro

Os resultados abaixo são o **histórico confirmado pelo responsável**, fornecido para esta documentação. Não são resultados obtidos pelo agente. Não foram disponibilizadas saídas brutas, capturas, timestamps, versão exata da CLI ou trilhas de auditoria; nenhum desses elementos foi inventado.

Os comandos a seguir são sugestões de reprodução. Flags, filtros e formatos foram escolhidos para esta documentação e não comprovam a sintaxe exata utilizada na execução original. Nesta entrega não foram feitas chamadas AWS, autenticação SSO ou alterações de configuração local.

## Resultados confirmados

| Item | Resultado histórico |
| --- | --- |
| Organizations | Habilitado com todas as funcionalidades; conta de gerenciamento existente |
| Identity Center | Instância organizacional em `sa-east-1`, diretório integrado |
| RBAC | Usuário configurado, grupo `AWS-SAA-Labs` e Permission Set atribuído ao grupo na conta |
| MFA | Exigido em todos os logins |
| Permission Set | `SAA-Lab-Operator`, sessão de uma hora, política publicada validada |
| CLI | AWS CLI v2 no Ubuntu, perfil `aws-saa-labs`, região padrão `sa-east-1` |
| Federação | Autenticação SSO e credenciais temporárias AWS STS |
| STS | `sts get-caller-identity` executado com sucesso |
| Organizations | `organizations describe-organization` executado com sucesso |
| EC2 | Operações de leitura autorizadas; não há transcrição individual de cada ação |
| Limpeza | VPC personalizada legada removida manualmente; VPC padrão preservada |
| Auditoria regional final | Zero NAT Gateways, zero Elastic IPs alocados e zero VPC Endpoints em `sa-east-1` |

## Reprodução CLI — somente leitura

Execução futura por pessoa autorizada, com sessão SSO válida. Os filtros evitam imprimir identificadores nas respostas normais; erros, modo debug e saídas sem filtro podem revelar dados. Não publique logs brutos.

### Identidade federada e organização

```bash
aws sts get-caller-identity \
  --profile aws-saa-labs --region sa-east-1 \
  --query '{RoleOperacional: contains(Arn, `":assumed-role/AWSReservedSSO_SAA-Lab-Operator_"`)}' \
  --output json --no-cli-pager

aws organizations describe-organization \
  --profile aws-saa-labs --region sa-east-1 \
  --query 'Organization.FeatureSet' \
  --output json --no-cli-pager
```

Critérios esperados na reprodução: primeira consulta bem-sucedida com `RoleOperacional` igual a `true`; segunda com `ALL`. São expectativas, não saídas coletadas. O primeiro filtro verifica o padrão da role assumida no ARN STS, incluindo o delimitador `:assumed-role/` para evitar correspondência apenas no nome da sessão de outra role. A consulta não comprova isoladamente a conta de destino, as permissões efetivas ou a configuração de MFA; a conferência privada desses aspectos continua necessária. `GetCallerIdentity` não exige um `Allow` próprio nessa política, conforme a [referência STS](https://docs.aws.amazon.com/STS/latest/APIReference/API_GetCallerIdentity.html).

### VPC padrão e inventário regional

```bash
aws ec2 describe-vpcs \
  --profile aws-saa-labs --region sa-east-1 \
  --query 'length(Vpcs[?IsDefault == `true`])' \
  --output json --no-cli-pager

aws ec2 describe-nat-gateways \
  --profile aws-saa-labs --region sa-east-1 \
  --query 'length(NatGateways)' \
  --output json --no-cli-pager

aws ec2 describe-addresses \
  --profile aws-saa-labs --region sa-east-1 \
  --query 'length(Addresses)' \
  --output json --no-cli-pager

aws ec2 describe-vpc-endpoints \
  --profile aws-saa-labs --region sa-east-1 \
  --query 'length(VpcEndpoints)' \
  --output json --no-cli-pager
```

Critérios esperados na reprodução do estado documentado: VPC padrão presente e contagens de NAT Gateways, Elastic IPs e VPC Endpoints iguais a zero. As consultas cobrem a conta selecionada e `sa-east-1`, no momento da execução. NAT Gateways recentemente excluídos podem permanecer visíveis temporariamente; uma contagem não nula exige conferir o estado e as dependências, sem inferir automaticamente cobrança ou falha de exclusão.

Não utilize `--no-paginate` para inventários completos. Não filtre NAT Gateways somente por `available`, pois estados transitórios também merecem revisão.

### Consultas complementares previstas pela política

Os comandos abaixo ajudam a reproduzir a verificação de permissões, mas **não possuem resultados individuais registrados no histórico**. Os totais não são critérios de custo nem valores esperados fixos.

```bash
aws organizations list-accounts \
  --profile aws-saa-labs --region sa-east-1 \
  --query 'length(Accounts)' --output json --no-cli-pager

aws ec2 describe-subnets \
  --profile aws-saa-labs --region sa-east-1 \
  --query 'length(Subnets)' --output json --no-cli-pager

aws ec2 describe-route-tables \
  --profile aws-saa-labs --region sa-east-1 \
  --query 'length(RouteTables)' --output json --no-cli-pager

aws ec2 describe-internet-gateways \
  --profile aws-saa-labs --region sa-east-1 \
  --query 'length(InternetGateways)' --output json --no-cli-pager

aws ec2 describe-security-groups \
  --profile aws-saa-labs --region sa-east-1 \
  --query 'length(SecurityGroups)' --output json --no-cli-pager

aws ec2 describe-availability-zones \
  --profile aws-saa-labs --region sa-east-1 \
  --query 'length(AvailabilityZones)' --output json --no-cli-pager
```

## Conferência humana no Console

O operador não tem ações administrativas de leitura do IAM Identity Center na política publicada. Um administrador deve conferir privadamente:

- Instância organizacional e diretório integrado em `sa-east-1`.
- Associação do usuário ao grupo e atribuição do grupo à conta correta.
- MFA em todos os logins e ausência de alternativa de acesso sem dispositivo registrado.
- Permission Set com uma hora de sessão, política correspondente ao arquivo e provisionamento concluído.
- Ausência de políticas adicionais que ampliem o acesso efetivo além do necessário.

Essa lista orienta uma revisão; não representa um novo teste realizado. Não há teste negativo de criação/exclusão nem análise completa de permissões efetivas registrado. Não tente criar ou excluir um recurso para demonstrar uma negativa de acesso.

## Critérios de aceite

| Critério | Situação e forma de comprovação |
| --- | --- |
| Organizations e Identity Center conforme arquitetura | Confirmado no histórico; detalhes verificáveis no Console pelo administrador |
| MFA, RBAC e sessão de uma hora | Confirmados no histórico; opções detalhadas e políticas adicionais exigem revisão humana |
| STS e DescribeOrganization funcionais | Sucesso histórico confirmado; comandos filtrados permitem reprodução futura |
| EC2 de leitura autorizado | Confirmado no histórico em termos gerais; consultas complementares sem evidência individual |
| Política operacional de leitura | Conteúdo validado fornecido; conferir correspondência com o Permission Set em revisão humana |
| Limpeza regional | Estado final confirmado para os três tipos de recurso e preservação da VPC padrão |
| Publicação sem dados sensíveis | Revisão local dos arquivos e revisão humana antes de publicar |
| Ausência de cobranças na conta | Fora do escopo; não comprovada |

## Validações locais da documentação

Parse JSON, conferência da lista de ações, links relativos e revisão estrutural de Markdown podem ser realizados sem AWS. Eles não substituem IAM Access Analyzer, renderização Mermaid, teste de permissões na conta ou auditoria de custos. A entrega informa separadamente quais verificações locais foram realmente executadas.
