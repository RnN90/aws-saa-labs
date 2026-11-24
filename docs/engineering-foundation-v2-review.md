# Engineering Foundation v2 — auditoria e relatório

## Diagnóstico inicial

Referência auditada: main remota `92bc5e1`, merge do PR #4, após PRs #1–#3 de identidade, rede e engenharia. Referências sincronizadas por clone temporário via GitHub CLI e fetch local, devido à limitação de DNS do git direto. A branch de trabalho é `feat/engineering-foundation-v2`. A fonte de verdade foi o conteúdo real do repositório, não diretórios presumidos pelo planejamento.

- LAB 00: README, arquitetura, implementação, validação, cleanup, diagramas e política IAM aprovada; governança histórica, sem IaC de workload. A política e seus limites permanecem intactos.
- LAB 01: único root Terraform; 12 recursos históricos provisionados/destruídos, Control Plane validado por CLI/State, sem Data Plane. Recursos, tags, outputs, CIDRs, AZs, versões e lock preservados byte a byte.
- LABs futuros: apenas linhas no README, sem diretórios versionados. Inserir EC2 como LAB 02 e deslocar S3/serverless/mensageria/observabilidade para 03–06 não renumera implementação existente.
- CI: descoberta por arquivos Git, sete testes existentes, actions por SHA, permissões contents:read, concurrency, timeouts, fmt/init/validate e nenhuma credencial/deploy AWS.
- Segurança/documentação: pt-BR consolidado, ignore de states/planos/tfvars/segredos, revisão humana e evidências históricas explicitadas. Nenhum diretório ou política experimental local foi lido, alterado ou incluído.
- Referências afetadas: índice e convenções na raiz/AGENTS e recomendação de S3 no relatório anterior. Fixtures sintéticas de testes antigos não são referências de LABs de negócio e permanecem intactas. Links novos são relativos; IDs sem número evitam acoplamento futuro à apresentação.

## Arquitetura adotada e estrutura

A fundação combina [manifestos/capacidades](../catalog/README.md), [DAG e contratos](architecture/dependencies.md), [matriz de competências](../certifications/README.md), [ADRs](adr/README.md) e [Quality Gates](standards/quality-gates.md). Metadados estáticos não viram inventário AWS ou executor.

```text
catalog/                         descrições de capacidades e fonte de verdade
certifications/                  catálogo oficial e matriz inicial SAA-C03
shared/schemas/                  JSON Schema v1
shared/scripts/                  descoberta existente e validação de catálogo
shared/templates/                LAB, ADR e registro privado de ambiente
labs/lab00-identity-governance/   implementação histórica + manifesto
labs/lab01-vpc-networking/        Terraform existente + documentação + manifesto
labs/lab02-ec2-connectivity/      cenário e manifesto; sem Terraform
labs/lab03-s3-security/           planejamento e manifesto
labs/lab04-lambda-api-gateway/    planejamento e manifesto
labs/lab05-sqs-sns/               planejamento e manifesto
labs/lab06-cloudwatch/            planejamento e manifesto
docs/roadmap/                    dez ondas de competências
docs/architecture/               dependências, evolução Terraform e labctl futuro
docs/standards/                  aprendizado/publicação, qualidade, FinOps/segurança
docs/adr/                        decisões aceitas/propostas
```

O [roadmap](roadmap/README.md) preserva a sequência 00–06 e planeja ondas 02–10 por competências, sem antecipar dezenas de pastas. Cada capacidade tem um LAB proprietário em `provides`; não há owner duplicado no catálogo. Manifestos descrevem estado de implementação e publicação; registros privados descrevem ambientes ativos. JSON compatível com YAML 1.2 evita um parser adicional; JSON Schema usa biblioteca consolidada com dependências de validação fixadas por versão/hash. Não há avaliação de expressões.

## Rastreabilidade e decisões

Os 13 códigos solicitados tiveram guias individuais acessados em 24/11/2026; o índice geral não retornou conteúdo legível. O [catálogo](../certifications/catalog.json) separa código confirmado de disponibilidade comercial pendente. Destacam-se transição DVA-C03, beta MLA-C02/AIB-C01, divergência de código na tabela comercial MLA e aposentadoria ANS em 31/12/2026. Não tratar guia disponível como prova de agenda por idioma. Não declarar cobertura integral.

A matriz SAA-C03 explicita os 14 objetivos oficiais, competência interna, nível, modalidades, evidências, lacunas e artigos pendentes. As outras trilhas têm catálogo global, sem matriz detalhada inventada. Objetivos foram traduzidos com referência à fonte, sem criar objetivos oficiais novos. Aposentadoria de exame não remove capacidade técnica do roadmap.

Cinco ADRs registram as decisões efetivamente adotadas: identidade/conta, Terraform/estado/ownership, dependências/reutilização, Git/IA/revisão e proposta de labctl/nome futuro. Conta dedicada, backend remoto, locking distribuído, módulos, OIDC, CD e orquestrador continuam propostas; nenhuma conta ou serviço foi criado.

## LAB 01, LAB 02 e cleanup

LAB 01 ganhou modos independente e sequencial, sem alteração de Terraform ou das evidências originais. LAB 02 é consumidor planejado; não há execução ou consumidor ativo confirmado. Retenção exige prazo, responsável, orçamento, conta/região e registro local. Cleanup remove consumidores antes de produtores, bloqueando dependência de outro consumidor ativo mediante verificação humana; o validador não implementa esse bloqueio operacional.

LAB 02 tem cenário corporativo, contrato dos seis outputs existentes para inputs propostos, estados separados, matriz positiva/negativa, acesso administrativo restrito, troubleshooting e cleanup integrado. NACL/rotas herdadas serão inspecionadas, sem serem modificadas. Testes negativos mutáveis dependem de fixture isolada pertencente ao consumidor e aprovação futura. SSM não é presumido funcional em subnets privadas sem egress/endpoints. Tudo permanece planejamento, sem EC2 ou Terraform desse LAB.

## Qualidade, aprendizado e publicação

O scorecard totaliza 100 pontos: arquitetura/IaC/segurança/testes com 15 cada; DevOps/FinOps/documentação/qualidade educacional com 10 cada. Meta 90, critérios verificáveis, evidências e normalização por itens aplicáveis; impeditivos não são compensados pela nota. Não foi atribuída nota fictícia aos LABs históricos ou à implementação futura. Definition of Done distingue fundação documental, LAB implementado e publicação concluída.

A metodologia de 15 etapas orienta sessões compactas sem sacrificar qualidade. GitHub, artigo e hands-on do portal têm propósitos e status separados; ChatGPT/Codex apoiam fluxo Git/PR/humano, Lovable é opcional. O portal e o nome do repositório não mudam.

## Validações e limites

Na validação local, passaram 34 testes (sete existentes e 27 novos), catálogo/schema/DAG, 143 links relativos e cinco diagramas estruturais, Terraform Format/Init/Validate do LAB 01, actionlint e Gitleaks nas alterações preparadas. O init usou o mirror temporário já disponível do provider oficial, com lock somente leitura; a execução remota do CI é verificada após a publicação e registrada no PR. O diff confirmou que Terraform/lock do LAB 01, política IAM do LAB 00 e scripts/testes antigos de descoberta permanecem byte a byte intactos. Os checks implementados abrangem JSON Schema, IDs/números duplicados, dependências inexistentes/cíclicas, capacidades/owners/contratos, status, caminhos, publicação sem URL, referências de cobertura, links locais e estrutura básica Mermaid. O CI existente recebe somente instalação de dependências de validação, execução do catálogo e filtros de caminhos relacionados; a matriz Terraform e suas versões/permissões permanecem preservadas.

Não há operações AWS, plano real, provisionamento, mudança de IAM/Organizations, Terraform State, portal ou lock Terraform. Não foram executados testes de Data Plane, custos reais, concorrência distribuída ou cleanup ativo. Mermaid é verificado estruturalmente; renderização visual depende de ferramenta indisponível neste ambiente. Links locais são verificados por existência; âncoras e disponibilidade externa não são validadas automaticamente. As fontes oficiais consultadas têm data, e mudanças futuras exigem revisão.

## Dívidas explícitas e próximo incremento

- Revisar disponibilidade SAP-C03 e idiomas/janelas em transição antes de qualquer inscrição; expandir matrizes além da SAA gradualmente.
- Validar visualmente diagramas e realizar avaliação humana dos Quality Gates; não confundir checks estáticos com comprovação arquitetural.
- Implementar LAB 02 somente em atividade autorizada, com estimativa regional, imagem/quantidade/tamanho de EC2, acesso administrativo e fixture aprovados.
- Inventário ativo/cleanup continuam manuais; teste de locking distribuído, backend remoto e orquestração exigem necessidade e decisões futuras.
- Artigos e hands-on do portal continuam pendentes até atividade separada; manifestos não inventam URLs nem publicação.
