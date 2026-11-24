# labctl — proposta de evolução

Status: **proposto, não implementado**. O único mecanismo funcional nesta entrega é a validação local de metadados em [validate_catalog.py](../../shared/scripts/validate_catalog.py). Não há comando labctl, detecção de recursos AWS, plano operacional ou execução de Terraform por esse mecanismo.

A arquitetura futura separa leitura de manifestos, resolução do DAG, inventário autorizado, planejador, aprovação humana, executor e evidências. O planejador lê os [contratos e lifecycle](dependencies.md); somente o executor aprovado pode chamar ferramentas de infraestrutura.

| Capacidade futura | Critério para adoção |
| --- | --- |
| Listar LABs e consultar metadados | Catálogo estável e demanda de navegação |
| Resolver dependências e ciclos | Reutilizar a semântica existente, selecionar cenário sem executar expressões |
| Gerar plano de execução | Separar pré-requisitos educacionais, operação e infraestrutura; listar alvos e impactos |
| Validar conta/região e identificar recursos | Acesso temporário explicitamente autorizado, conferência de ownership e estado |
| Compartilhar outputs autorizados | Allowlist versionada, sem exposição do state completo |
| Executar com aprovação | Aprovação vinculada ao plano, revisão humana e recusa se alvos mudarem |
| Cleanup seguro | Inventário de consumidores ativos, ordem inversa e confirmação de propriedade |
| Registrar evidências | Dados sanitizados, correlação por execução e armazenamento privado de detalhes |

Recusar operação destrutiva com ownership ambíguo, inventário desatualizado, consumidor ativo ou estado concorrente. Falhas intermediárias geram pausa e reconciliação, nunca destruição automática da fundação. Não acrescentar motor de expressões, serviço sempre ativo ou plataforma de orquestração antes de uma necessidade concreta e ADR.
