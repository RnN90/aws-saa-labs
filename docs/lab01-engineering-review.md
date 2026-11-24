# LAB 01 — Revisão de engenharia

## Escopo e referência inicial

A estrutura do repositório, todos os arquivos Terraform versionados, as regras de exclusão, a documentação, o workflow e o histórico de commits foram revisados antes das alterações. Referência inicial: `d8e041b` (merge da implementação do LAB 01, `c58ce1d`); a documentação anterior do LAB 00 teve origem em `bd1b972` e foi refinada em `f0f0391` / PR #1. A branch de trabalho é `chore/lab01-engineering-review`.

O responsável confirmou o provisionamento histórico, a inspeção pela AWS CLI e pelo Terraform State e a destruição de 12 recursos. Não foram realizados testes de conectividade entre workloads. Esta revisão não executou chamadas à API AWS, apply, destroy ou alterações em IAM ou Organizations. Não foi adicionada pipeline de provisionamento.

Um diretório IAM preexistente e não versionado do LAB 01 foi preservado localmente e excluído desta entrega. Sua política não é apresentada como completa ou validada. Os arquivos do LAB 00 e sua política IAM aprovada permanecem preservados; eventuais ajustes de idioma não alteram sua configuração.

## Constatações e decisões

| Constatação | Solução e impacto |
| --- | --- |
| O provider continha um ID real de conta | Parâmetro local obrigatório `aws_account_id`, com validação de 12 dígitos e restrição mantida por `allowed_account_ids`. Não há ID real público no provider atual. Usuários existentes precisam definir a nova variável antes de gerar planos. |
| Variáveis sem descrições ou validações suficientes | Descrições em pt-BR, parâmetros obrigatórios não nulos, validação de sintaxe IPv4, correspondência entre listas de duas entradas, unicidade dentro das listas, consistência entre AZ e região e perfil não vazio ou nulo. Valores padrão preservados. A verificação de sobreposição e contenção de CIDRs continua sob responsabilidade do operador. |
| Alguns outputs não tinham descrição | Descrições para os seis outputs existentes, sem renomeá-los ou alterar seus valores. |
| Possível impacto de uma mudança de count para for_each | Manutenção de count, ordem das listas, tags e endereços de recursos. Não há justificativa para extrair módulos ou migrar o estado. |
| CI funcional com tags mutáveis de actions e runtimes descontinuados | Fixação dos SHAs verificados de checkout v7.0.1 e setup-terraform v4.0.1; ambos declaram Node.js 24. Manutenção do Terraform 1.15.8 e do lock do provider AWS em 6.74.0. |
| A descoberta dependia somente de arquivos chamados versions.tf | Descoberta dos arquivos diretos dos diretórios raiz Terraform versionados no padrão documentado, exigência de versions e lock versionados, ordenação e deduplicação, registro de descoberta vazia e rejeição de matrizes com mais de 256 jobs. Adição de sete testes unitários com a biblioteca padrão, executados no CI. |
| Faltavam limites operacionais | Desabilitação da persistência de credenciais do checkout; manutenção de contents:read, cancelamento por concorrência e fail-fast:false. Adição de limites de tempo, max-parallel:4, versão explícita do runner e gatilhos de push para chore/fix. |
| A documentação descrevia o LAB 01 implementado como planejado | Atualização da navegação e do estado na raiz, README técnico com 19 seções, guia de contribuição e instruções permanentes no AGENTS. O ajuste complementar estabelece pt-BR em toda a documentação. Conteúdo técnico do LAB 00 preservado. |
| Risco de exposição de artefatos locais | Manutenção das exclusões de estado, tfvars, planos e credenciais; adição de exclusões na raiz para relatórios de falha e variantes de planos. Lock files continuam versionados. |

## Preservação da arquitetura e compatibilidade

`main.tf`, `versions.tf` e `.terraform.lock.hcl` permanecem idênticos, byte a byte, à referência inicial. Foram preservados os 12 recursos gerenciados originais, os quatro CIDRs de subnets, duas AZs, roteamento, DNS e opções de IP público. Tags e dependências implícitas por referências permanecem intactas. Objetos padrão da VPC criados pela AWS não são recursos adicionais gerenciados pelo Terraform.

O novo parâmetro de conta é uma mudança intencional de interface da revisão de engenharia. Use a mesma conta autorizada de uma infraestrutura existente; alterar a lista de autorização para outra conta não migra recursos. Essas melhorias não exigem substituição intencional de recursos, mas nenhum plano real na AWS foi executado para comprovar ausência de mudanças sobre um estado provisionado. Alterar CIDRs da VPC ou subnets, AZs, ordem de parâmetros indexados por count ou chaves de recursos pode causar substituições e exige plano ou migração revisados separadamente.

A restrição do provider `~> 6.0` permanece limitada à versão principal 6, e o lock seleciona 6.74.0. Os hashes de pacotes `zh` existentes permitem verificação em diferentes plataformas; a inicialização em Linux amd64 foi exercitada. Outras plataformas não foram testadas. Não houve edição manual de hashes nem atualização de provider.

## Evidências do CI anterior

A [execução 45296126457 da branch main](https://github.com/RnN90/aws-saa-labs/actions/runs/45296126457) concluiu com sucesso para a referência inicial. Os endpoints de annotations dos dois checks puderam ser consultados pela GitHub CLI. O job Discover registrou um aviso de Node.js 20 para checkout v4; o job Validate registrou o mesmo aviso para checkout v4 e setup-terraform v3. As annotations informam que essas actions foram forçadas a executar em Node.js 24. A revisão atualiza os runtimes das duas actions e fixa suas versões.

A ferramenta conectada de consulta ao GitHub rejeitou a URL da coleção de execuções de workflows; por isso, a GitHub CLI foi utilizada para metadados das execuções, annotations e verificação das referências das actions. Logs brutos não foram usados como evidência de testes de infraestrutura.

## Registro de validação da revisão inicial

- Terraform 1.15.8: `terraform fmt -check -recursive` aprovado em todo o repositório.
- A execução direta de `terraform init -backend=false -input=false -lockfile=readonly` falhou inicialmente porque o ambiente isolado não conseguia acessar registry.terraform.io.
- O pacote oficial do provider AWS 6.74.0 para Linux amd64 foi baixado de releases.hashicorp.com. Seu SHA-256 correspondeu a uma entrada `zh` existente no lock versionado. O init sem backend e com lock somente leitura passou com mirror de sistema de arquivos e configuração CLI temporários em `/tmp`; nenhum deles integra o repositório ou o CI.
- `terraform validate` passou quando executado diretamente no diretório Terraform do LAB 01. Uma tentativa anterior no ambiente isolado falhou ao iniciar o plugin do provider; a execução direta bem-sucedida resolveu essa limitação.
- actionlint 1.7.7: sintaxe do workflow e verificações estáticas aprovadas.
- Sete testes de descoberta aprovados: entrada vazia, múltiplos LABs ordenados e sem duplicação, exclusão de caches e módulos aninhados, ausência de lock, ausência de versions, estrutura inválida e limite da matriz.
- Cercas de código Markdown, 39 links relativos da documentação e sintaxe JSON IAM versionada aprovados; as 19 seções do LAB 01 estão presentes. As referências externas oficiais foram abertas com sucesso; a página do registry do provider exige JavaScript para exibir seu conteúdo.
- Arquitetura Mermaid e quatro subgrafos com fechamentos correspondentes verificados estruturalmente e por revisão manual. Não há renderizador Mermaid instalado; a aparência renderizada não foi validada.
- Verificação de espaços em branco do diff preparado para commit aprovada. O Gitleaks 8.24.3 analisou as alterações preparadas com ocultação de valores sensíveis e não encontrou vazamentos. As verificações de caminhos versionados e identificadores estão registradas no resumo final de validação do PR.
- O CI remoto da revisão inicial foi aprovado após a publicação da branch dedicada; os resultados estão no PR e nas [execuções de push](https://github.com/RnN90/aws-saa-labs/actions/runs/45298501935) e [Pull Request](https://github.com/RnN90/aws-saa-labs/actions/runs/45298557546), ambas sem annotations.

## Limitações e próximos passos

Não foram realizadas consultas ou alterações na AWS. A configuração revisada não foi provisionada, e nenhum plano real, teste de conectividade, failover ou autorização foi executado. A execução histórica é atribuída ao responsável, sem recriação de evidências. Ignorar arquivos não protege estados existentes nem apaga o identificador original da conta do histórico Git; não houve reescrita de histórico. IDs de conta são identificadores, não segredos de autenticação.

A imagem do runner e os downloads não são imutáveis, mesmo com actions e Terraform fixados. Revise atualizações de actions e providers separadamente. Se o CI passar a ser uma verificação obrigatória da branch, revise o comportamento dos filtros de caminhos para Pull Requests exclusivamente documentais antes de habilitar proteção de branch. Nenhuma configuração administrativa do repositório foi alterada.

Para o LAB 02 (segurança no S3, ainda planejado), defina primeiro responsabilidade e cleanup; um bucket não depende, por si só, da rede do LAB 01. Documente explicitamente qualquer dependência real. Planeje criptografia, Block Public Access, controles de propriedade, acesso temporário de menor privilégio e testes com escopo restrito. Revise versionamento, retenção e custos de cleanup antes de habilitar funcionalidades. VPC endpoint, observabilidade paga, infraestrutura de estado remoto ou automação de provisionamento exigem revisão de arquitetura e autorização próprias; nenhum desses itens é introduzido aqui.

## Ajuste complementar de idioma

O português brasileiro (pt-BR) passa a ser o idioma oficial de toda a documentação, incluindo LABs atuais e futuros, relatórios, diagramas, comentários e descrições Terraform. Termos técnicos consolidados e identificadores permanecem em inglês; mensagens de commits seguem Conventional Commits em inglês. A seção “Padrões de idioma e documentação” do AGENTS aplica essa diretriz a todos os agentes.

A tradução preserva os comandos, identificadores, condições de validação, arquitetura, tags e lock file. Mensagens explicativas de validação Terraform foram traduzidas sem alterar seus critérios. Os nomes e a lógica dos workflows permanecem intactos; os scripts Python tiveram somente suas docstrings traduzidas.

O PR #3 foi mesclado em 24/11/2026, às 00:43 UTC, antes deste ajuste complementar. Um PR mesclado não pode ser reaberto. O novo commit permanece na branch `chore/lab01-engineering-review`, sem criação de outro PR ou novo merge; a descrição do PR #3 será atualizada para registrar a entrega e essa limitação. Neste ajuste, passaram novamente Terraform Format e Validate, actionlint, os sete testes de descoberta, 39 links relativos, análise de sintaxe JSON, cercas Markdown, estrutura dos três diagramas Mermaid e Gitleaks nas alterações preparadas e no histórico disponível. A comparação de preservação confirmou condições Terraform, identificadores, comandos documentados, AST funcional Python, workflow, lock e política IAM intactos. Não houve operação na AWS. A renderização Mermaid continua indisponível. O resultado da pipeline do novo commit é informado separadamente na descrição do PR.

## Referências

- [Boas práticas de segurança do Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html)
- [Route Tables da AWS](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html)
- [Configuração de providers Terraform](https://developer.hashicorp.com/terraform/language/providers/configuration)
- [Lock file de dependências](https://developer.hashicorp.com/terraform/language/files/dependency-lock)
- [Uso seguro do GitHub Actions](https://docs.github.com/en/actions/reference/security/secure-use)
- [checkout v7.0.1](https://github.com/actions/checkout/releases/tag/v7.0.1)
- [setup-terraform v4.0.1](https://github.com/hashicorp/setup-terraform/releases/tag/v4.0.1)
