# Instruções permanentes — AWS Certification & Engineering Program

## Objetivo e fonte de verdade

- Desenvolva uma plataforma reutilizável de competências para todas as trilhas AWS, Cloud Architecture, IaC, Platform Engineering, DevSecOps, SRE, Security, FinOps e Knowledge Engineering. O nome do repositório permanece aws-saa-labs.
- Antes de editar, confira estado Git, histórico, instruções, README, manifests, Terraform e workflows reais. Preserve alterações do usuário e a engenharia validada em PRs anteriores.
- Use mudanças incrementais e justificadas; não antecipe módulos, ferramentas, infraestrutura ou abstrações sem necessidade concreta.
- Consulte [roadmap](docs/roadmap/README.md), [catálogo](catalog/README.md), [contratos](docs/architecture/dependencies.md), [certificações](certifications/README.md) e [ADRs](docs/adr/README.md). Não duplique essas fontes nos LABs.

## Estrutura, reutilização e Terraform

- LABs usam `labs/labNN-topic/README.md` e `lab.yaml`; schema versionado em `shared/schemas/`. IDs estáveis não dependem da numeração. LABs 00 e 01 são implementados; 02–06 são planejados. Só crie diretórios com conteúdo de planejamento real; nunca Terraform fictício.
- Sequência: identidade, VPC, EC2/conectividade, S3, Lambda/API Gateway, SQS/SNS, CloudWatch. Não renumere LAB publicado/implementado sem aprovação.
- Reutilize capacidades entre certificações; crie LAB apenas para nova aprendizagem/lacuna. A numeração não cria dependência. Declare tipo, cenário opcional, capacidade, contrato e ownership no manifesto.
- Mantenha nomes Terraform em snake_case, tipos/descrições/validações úteis, dependências por referências, tags comuns e outputs estáveis. Preserve CIDRs, AZs, tags, endereços e versões/lock do LAB 01 salvo autorização específica.
- Mantenha os arquivos convencionais em `terraform/`; versione lock gerado, nunca hashes editados manualmente. CI usa init sem backend e lock somente leitura. Migração de count/for_each ou alteração capaz de substituir recursos exige plano de impacto e migração revisados.
- Cada recurso pertence a um único Terraform State e LAB. Consumidores referenciam IDs autorizados; não redefinem nem importam recursos de produtores. Isolar execuções/estados e impedir processos concorrentes é pré-condição para execução, não função do validador estático.
- Preserve conta autorizada configurável e credenciais federadas temporárias. Não fixar IDs reais nem ampliar a política IAM validada do LAB 00. Políticas experimentais locais nunca são entregas validadas.

## Padrões de idioma e documentação

- Toda documentação, LAB atual/futuro, relatório, comentário explicativo, descrição Terraform e texto de Mermaid deve ser pt-BR, educacional e profissional. Todos os agentes devem aplicar essa diretriz.
- Preserve termos técnicos consolidados: Infrastructure as Code, Cloud Computing, Pull Request, Internet Gateway, NAT Gateway, Route Table, Availability Zone, Terraform State, CI/CD, DevSecOps e FinOps. Preserve nomes canônicos de serviços e trilhas.
- Identificadores de código, variáveis, funções, outputs, arquivos, diretórios, branches, configurações e identificadores técnicos dos workflows permanecem em inglês. Conventional Commits e títulos de Pull Requests em inglês; descrições dos PRs em pt-BR.
- Separe proposta, implementação, execução histórica, simulação e resultado realmente observado. Não invente recursos, saídas, datas, cobertura oficial ou testes Data Plane. LAB 01 teve 12 recursos provisionados/destruídos e somente validação de Control Plane informada.
- Use referências oficiais com data para certificações; código e disponibilidade podem divergir. Registre fontes inacessíveis/mapeamentos pendentes e preserve competências de exames aposentados. Nunca declarar cobertura integral pela presença de serviços.
- Aplique [metodologia/publicação](docs/standards/learning-publication.md) e [template de LAB](shared/templates/lab-readme.md). Três entregáveis por LAB: GitHub, artigo e hands-on no portal, com estados verdadeiros e sem duplicação extensa. Não usar dumps.
- ChatGPT/Codex apoiam o fluxo Git/PR/revisão humana. Lovable não é dependência obrigatória. Não modificar o portal nesta atividade; eventual renomeação do repositório exige decisão separada.

## Segurança, custos e lifecycle

- Uma tarefa documental/CI não autoriza nenhuma operação AWS, login/logout, mudança IAM/Organizations, apply, destroy ou import. Execute operações AWS somente com autorização explícita para a operação e alvos. Nunca leia credenciais, tokens, caches SSO ou arquivos privados.
- Não versione state, planos, tfvars locais, segredos, IDs reais, ARNs de sessão, URLs privadas ou evidências brutas. Não apague arquivos locais não versionados. Revise caminhos e conteúdo explicitamente antes de staging.
- Não recomende AdministratorAccess nem edite roles AWSReservedSSO diretamente; use IAM Identity Center. SCPs não restringem a conta de gerenciamento. Conta-membro dedicada para workloads permanece recomendação/proposta, sem alegar criação.
- Avalie custo antes de qualquer execução; Free Tier não garante gratuidade. Use [FinOps e segurança](docs/standards/finops-security.md) para conta/região, responsável, inventário, orçamento, prazo de retenção e verificação de remanescentes.
- Reutilização não exige infraestrutura permanentemente ativa. Cleanup exige revisão de ownership, inventário real, consumidores ativos e aprovação; remover consumidores antes de produtores. Preservar identidade/governança compartilhadas e state em falhas para reconciliação.
- Bloqueie remoção de dependências usadas por outro consumidor. O inventário é privado e manual nesta fase; não afirme proteção automatizada por labctl, backend remoto ou locking distribuído ainda inexistentes.

## Git, qualidade e aceite

- Trabalhe em branch dedicada a partir da main remota atual. Não altere main diretamente. Conventional Commits em inglês; commit/push/PR quando autorizados pela tarefa. Nunca fazer merge automático.
- Preserve o CI sem credenciais/deploy, permissões mínimas, actions fixadas por SHA, checkout sem persistência de credenciais, concurrency e timeouts. Mudanças de pipeline devem ser estritamente necessárias às validações.
- Execute fmt, init sem backend/lock somente leitura e validate para roots implementados; actionlint; testes de descoberta e de catálogo; schema, DAG, links e Mermaid estrutural; Gitleaks e revisão de diff. Instale só as dependências fixadas de validação. Documente indisponibilidades e diferencie validação visual de estrutural.
- Siga [Quality Gates e Definition of Done](docs/standards/quality-gates.md): meta 90/100 com evidências, normalização justificada e impeditivos não compensáveis. Não transformar planejamento ou score estimado em implementação validada.
- Entregue diagnóstico, decisões, arquivos, verificações reais, limitações, dívidas e link do PR para revisão humana. Novas decisões devem usar [template de ADR](shared/templates/adr.md), distinguindo aceito, proposto e substituído.
