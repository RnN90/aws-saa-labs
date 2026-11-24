# Architecture Decision Records

ADRs registram decisões, alternativas, consequências, evidências e estado. Use [o template](../../shared/templates/adr.md). Estados: **proposto**, **aceito**, **substituído**. Aceito significa decisão de engenharia adotada no escopo declarado, não prova de recursos ativos. Um ADR substituído aponta para o sucessor; nunca reescrever fatos históricos como se fossem implementações novas.

| ADR | Estado | Decisões |
| --- | --- | --- |
| [0001 — Identidade e conta](0001-identity-account.md) | Aceito para identidade; conta dedicada proposta | Preserva decisões já documentadas no LAB 00, sem repeti-las como implantação nova |
| [0002 — IaC, estados e ownership](0002-iac-state-ownership.md) | Aceito | Terraform existente; isolamento e recurso com proprietário único; backend remoto não implementado |
| [0003 — Dependências e reutilização](0003-dependencies-reuse.md) | Aceito | Manifestos, DAG, contratos, cleanup inverso e reutilização entre certificações |
| [0004 — Git, IA e revisão humana](0004-git-ai-review.md) | Aceito | Git como desenho versionado, apoio de IA, revisão e publicação humanas |
| [0005 — Orquestração e nome futuro](0005-orchestration-naming.md) | Proposto | labctl, adoção futura de plataforma e eventual aws-engineering-labs |

Nenhum ADR substituído nesta entrega; atualizações futuras devem manter a cadeia de decisão explícita. As decisões dos PRs anteriores permanecem válidas salvo indicação explícita de substituição.
