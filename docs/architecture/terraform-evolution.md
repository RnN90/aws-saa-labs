# Evolução incremental de Terraform e DevOps

| Etapa | Situação | Gatilho e evidência necessária |
| --- | --- | --- |
| Terraform Foundation | Existente no LAB 01 | Preservar recursos, referências, tags, versões e lock já validados |
| Stack Dependencies | Contrato documentado; consumo ainda planejado | Implementar LAB 02 com estado separado e demonstrar passagem segura de outputs |
| Reusable Modules | Proposta | Extrair somente após repetição real e contrato estável; evitar módulo por serviço sem reutilização |
| Remote State | Proposta | Colaboração/múltiplos ambientes justificarem backend criptografado, acesso restrito e recuperação testada |
| State Locking distribuído | Proposta | Antes de concorrência entre operadores; escolher mecanismo suportado pelo backend e testar disputa/recuperação |
| Infrastructure Testing | Estático existente; Data Plane planejado | Cada teste deve comprovar hipótese e limite; mocks não substituem execução real |
| Policy as Code | Proposta | Políticas estáveis e riscos recorrentes justificarem ferramentas; documentar falsos positivos e exceções |
| GitHub Actions OIDC | Proposta | Necessidade autorizada de acesso AWS pelo CI, trust restrita a repositório/ref/ambiente e permissões mínimas |
| Continuous Delivery | Proposta | Aprovação de deploy, ambientes isolados, custos, planos revisados e rollback/reconciliação definidos |
| Platform Orchestration | Proposta | Vários consumidores reais justificarem o [labctl](labctl.md) e inventário confiável |

O CI atual continua sem credenciais e sem deploy. Não haverá backend remoto, módulo extra, OIDC ou CD criado nesta fundação. A validação nova é apenas de catálogo/documentação. Templates não são recursos ativos. Recursos do LAB 01 e sua política de versionamento não mudam neste PR.
