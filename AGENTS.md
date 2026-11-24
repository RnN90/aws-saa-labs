# Instruções de engenharia — aws-saa-labs

## Objetivo e escopo

- Desenvolva laboratórios práticos de arquitetura SAA-C03 com Terraform, segurança, governança, FinOps e documentação reproduzível para aprendizado profissional e portfólio.
- Trabalhe somente neste repositório. Preserve alterações do usuário, funcionalidades existentes e as políticas e o conteúdo validados do LAB 00.
- Prefira melhorias pequenas e justificadas. Não introduza módulos, dependências ou serviços sem necessidade concreta. Diferencie implementações existentes, validações históricas e trabalhos planejados.
- Os LABs 00 e 01 já foram executados. A infraestrutura do LAB 01 foi destruída após a validação. Os LABs 02–05 permanecem planejados; não invente implementações nem crie diretórios de preenchimento.

## Estrutura e Terraform

- Use `labs/labNN-topic/`, com dois dígitos e kebab-case. Cada LAB implementado deve ter `README.md`; os diretórios raiz Terraform ficam em `terraform/`. Adicione `docs/`, `diagrams/` ou `iam/policies/` somente quando necessário.
- Mantenha `main.tf`, `providers.tf`, `versions.tf`, `variables.tf`, `outputs.tf`, `.terraform.lock.hcl` e um `terraform.tfvars.example` sanitizado em cada diretório raiz Terraform.
- Use nomes Terraform em snake_case, tipos explícitos, descrições úteis, validações adequadas e tags determinísticas. Preserve as tags comuns Project, Lab, Environment e ManagedBy.
- Fixe a versão do Terraform no CI, restrinja versões de providers e versione o lock file gerado. Não edite hashes manualmente. Revise atualizações separadamente; o CI inicializa com `-backend=false -input=false -lockfile=readonly`.
- Expresse dependências por referências aos recursos. Use count para recursos com ordem estável; prefira for_each quando forem necessárias chaves semânticas estáveis. Alterar endereços existentes exige migração explícita e análise de impacto.
- Preserve CIDRs, AZs, rotas, tags e endereços de recursos validados, salvo autorização para mudanças arquiteturais. Documente o risco de substituição ao alterar parâmetros de rede, ordem das listas ou identidades de recursos.
- Exija que o ID da conta AWS autorizada seja informado localmente em cada provider AWS. Nunca fixe um ID real no código. Use credenciais federadas temporárias e permita que cada usuário escolha seu perfil.

## Git e contribuições

- Trabalhe em uma branch dedicada, nunca diretamente na main. Use `feat/`, `fix/`, `docs/` ou `chore/` e Conventional Commits, por exemplo `chore(lab01): improve validation`.
- Faça commit e push somente quando autorizados pela tarefa. Abra Pull Requests quando solicitado; a revisão final e o merge são humanos. Nunca habilite merge automático.
- Inspecione arquivos versionados e não versionados antes de adicioná-los à área de preparação. Selecione caminhos explícitos; não inclua arquivos locais alheios à tarefa nem políticas IAM experimentais.
- Preserve a política validada do LAB 00. Nunca apresente políticas experimentais como completas, validadas ou como garantia de menor privilégio.

## Padrões de idioma e documentação

- Toda a documentação do repositório deve ser escrita em português brasileiro (pt-BR), incluindo READMEs, relatórios, guias, textos explicativos de diagramas Mermaid, comentários no código e descrições de variáveis e outputs.
- Todos os futuros LABs devem seguir esse padrão, assim como a manutenção dos LABs existentes. Esta diretriz deve ser aplicada por todos os agentes que realizarem futuras contribuições ao repositório.
- Preserve termos técnicos consolidados em inglês, como Infrastructure as Code (IaC), Cloud Computing, Pull Request, Internet Gateway, NAT Gateway, Route Table, Availability Zone, Terraform State, CI/CD, DevSecOps e FinOps. Evite traduções literais que prejudiquem a compreensão.
- Mantenha em inglês os identificadores de código, recursos, variáveis, funções e outputs, nomes de arquivos e diretórios, branches, títulos de Pull Requests, serviços AWS e identificadores técnicos dos workflows. Preserve comandos, parâmetros e configurações.
- Mensagens de commits devem seguir Conventional Commits em inglês. Descrições de Pull Requests devem ser escritas em pt-BR.
- A documentação deve ter caráter educacional e profissional, com linguagem técnica natural e adequada à comunidade brasileira de tecnologia.
- Explique cenário, arquitetura, diagrama Mermaid, endereçamento, decisões, pré-requisitos, provisionamento, validação, segurança, custos, conceitos da certificação, cleanup, resultados e referências oficiais.
- Separe evidências históricas, resultados esperados, comandos para execução humana e verificações realmente executadas. Nunca invente saídas, IDs de recursos, datas, testes de conectividade ou validações bem-sucedidas.
- Use links internos relativos e referências externas oficiais. Não publique IDs reais de contas ou recursos, ARNs de sessões, URLs privadas, e-mails, credenciais ou evidências sem sanitização.
- Documente recursos herdados, LAB de origem, consumidores conhecidos, responsável pela manutenção e ciclo de vida. Não presuma que um LAB futuro consome um recurso apenas porque sua reutilização é possível.

## Segurança AWS, governança e custos

- Não execute apply, destroy, import ou qualquer comando que modifique recursos AWS sem autorização explícita para a operação. Uma revisão de repositório não autoriza provisionamento, consultas AWS, login/logout nem alterações em IAM ou Organizations.
- Não leia arquivos de credenciais, caches SSO, tokens ou arquivos de ambiente privados. Não altere configurações da CLI nem sessões de autenticação.
- Nunca versione Terraform State, planos, segredos ou tfvars locais. Regras de exclusão são controles preventivos e não substituem a revisão dos arquivos preparados para commit. Proteja o estado local com permissões restritas; proponha um backend remoto criptografado e com controle de acesso separadamente, se a colaboração exigir.
- Não recomende AdministratorAccess para falhas do operador nem edite roles AWSReservedSSO diretamente. Gerencie essas roles pelo IAM Identity Center. SCPs não restringem a conta de gerenciamento.
- Prefira contas-membro dedicadas para workloads. O operador de leitura do LAB 00 é insuficiente para o ciclo de vida do LAB 01; exija um Permission Set revisado separadamente, sem ampliar a política do LAB 00.
- Não introduza serviços pagos durante revisões. Documente premissas de preços e não garanta ausência de cobranças em toda a conta AWS.
- Classifique recursos como fundação compartilhada ou temporários. Documente consumidores e revise dependências antes de remover recursos. O cleanup exige confirmação humana da conta, região, recursos e dependências. Preserve Organizations, Identity Center, MFA e acessos compartilhados.

## Validação e critérios de aceite

- Antes de editar, leia o estado do repositório, histórico, instruções aplicáveis, Terraform e configuração do CI.
- Execute `terraform fmt -check -recursive`, init sem backend e com lock file somente leitura e `terraform validate` em cada diretório raiz, quando possível. Essas verificações não exigem credenciais AWS. Nunca execute um plano real apenas para validar a configuração.
- Execute actionlint, teste a descoberta sem LABs, com múltiplos LABs e sem lock file, e revise links relativos, estrutura Mermaid, JSON e arquivos preparados para commit em busca de dados sensíveis. Informe precisamente ferramentas indisponíveis e restrições de rede.
- O CI deve permanecer sem credenciais, somente leitura e sem provisionamento. Fixe actions por SHA completo verificado, desabilite a persistência de credenciais do checkout, defina limites de tempo e mantenha a descoberta determinística dos LABs. Não use pull_request_target com código não confiável.
- O aceite exige preservação de funcionalidades e do LAB 00, ausência de alterações na AWS ou exposição de credenciais, documentação reproduzível, mudanças incrementais justificadas, aprovação nas verificações disponíveis e diff/Pull Request para revisão humana quando solicitado.
- Informe arquivos alterados, decisões técnicas, verificações executadas, limitações e recomendações futuras. Validar sintaxe não testa autorização AWS; inspecionar rotas não testa conectividade entre workloads.
