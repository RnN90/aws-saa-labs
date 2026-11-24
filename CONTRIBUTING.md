# Contribuindo

Leia [AGENTS.md](AGENTS.md) e o README do LAB antes de alterar código. Preserve o LAB 00 e as arquiteturas já validadas.

1. Crie uma branch `feat/tema`, `fix/tema`, `docs/tema` ou `chore/tema` a partir de `main` atualizado.
2. Faça alterações incrementais e documente o motivo, riscos e eventual migração de state. Use `labs/labNN-tema/terraform` para novos diretórios raiz; inclua `versions.tf` e `.terraform.lock.hcl` para descoberta no CI.
3. Use Conventional Commits com mensagens em inglês: `feat(lab02): ...`, `fix(ci): ...`, `docs(lab01): ...` ou `chore(repo): ...`.
4. Execute, na raiz, `terraform fmt -check -recursive`, `python3 shared/scripts/discover-terraform.py` e `actionlint`. Em cada diretório raiz, execute `terraform init -backend=false -input=false -lockfile=readonly` e `terraform validate`.
5. Revise `git diff --check`, os links, os diagramas e cada arquivo preparado para commit. Nunca adicione state, planos, credenciais, tfvars locais ou evidências sem sanitização. Atualize lock files somente em upgrades revisados; não use `init -upgrade` no CI.
6. Abra um PR para revisão humana, descrevendo problema, solução, validações realmente executadas e limitações. Não faça merge automático.

As verificações locais e de CI não exigem credenciais AWS. Provisionamento e cleanup exigem autorização humana específica, revisão de custos, conta, região e dependências. A política operacional do LAB 00 não autoriza o ciclo de vida do LAB 01; políticas experimentais locais não devem ser incluídas como solução validada.

Documente todos os laboratórios e demais conteúdos em português brasileiro (pt-BR), com o [LAB 01](labs/lab01-vpc-networking/README.md) como referência. Preserve termos técnicos consolidados em inglês e o histórico do LAB 00. Mantenha identificadores, arquivos, diretórios, branches e títulos de Pull Requests em inglês; escreva as descrições dos Pull Requests em pt-BR. A documentação deve ter caráter educacional e profissional. Não crie diretórios vazios para LABs planejados.

## Catálogo, arquitetura e critérios de aceite

Antes de criar LAB, procure capacidades reutilizáveis no [catálogo](catalog/README.md) e lacunas na [matriz de certificações](certifications/README.md). Siga o [roadmap](docs/roadmap/README.md), adicione manifesto conforme schema v1 e declare dependências por ID e tipo; não derive dependências da numeração. Não crie Terraform para LAB planejado.

Use o [template de LAB](shared/templates/lab-readme.md) e registre decisões significativas em [ADRs](docs/adr/README.md). Aplique a metodologia de 15 etapas, os três entregáveis e o [scorecard/Definition of Done](docs/standards/quality-gates.md). Planejamento não equivale a execução; não atribua nota ou cobertura integral sem evidência. Preserve os contratos e um único state proprietário por recurso.

Instale as dependências fixadas em ambiente isolado conforme [instruções do catálogo](catalog/README.md), execute os testes existentes e novos e `python3 shared/scripts/validate_catalog.py`. Prepare arquivos novos antes da validação de links, que lê somente caminhos Git. O CI continua sem credenciais AWS e sem deploy. Mudanças de guias oficiais exigem data, fonte, diferenças e revisão das evidências. O portal é tratado separadamente e não deve ser modificado neste PR.
