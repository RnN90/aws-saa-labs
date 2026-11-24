# ADR 0001 — Identidade federada e separação de conta

Data: 2026-11-24. Estado: **aceito** para identidade; **proposto** para adoção de conta-membro dedicada ainda não confirmada.

Contexto: o [LAB 00](../../labs/lab00-identity-governance/docs/architecture.md) já documenta Organizations, IAM Identity Center, MFA e acesso federado temporário, com atribuição do Permission Set na conta de gerenciamento por simplificação educacional. Não há evidência de conta-membro adicional. Este ADR referencia essa decisão preexistente, sem recriar sua implementação.

Decisão: preservar identidade federada e política validada; separar autorização de governança da operação de workloads. Para workloads futuros, propor conta dedicada, com aprovação humana e verificação de elegibilidade/custos antes de execução. Esta proposta não cria conta nem altera Organizations.

Alternativas: chaves estáticas e administração indiscriminada aumentam exposição; workloads na conta de gerenciamento simplificam o estudo, mas ampliam impacto. Preferir isolamento quando adotado formalmente.

Consequências: LAB 02 exige permissão revisada separadamente; LAB 00 não concede criação de EC2. Evidência atual é a documentação histórica; migração da conta permanece pendente, sem afirmar execução.
