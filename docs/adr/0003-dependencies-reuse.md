# ADR 0003 — Dependências declarativas e capacidades reutilizáveis

Data: 2026-11-24. Estado: **aceito** para catálogo e validação estática; execução de consumidores ainda planejada.

Contexto: uma certificação consome vários LABs e um LAB contribui para várias certificações. Numeração não representa dependência. A necessidade inicial concreta é LAB 02 consumir a rede do LAB 01.

Decisão: adotar IDs estáveis, manifesto v1 em JSON compatível com YAML 1.2, JSON Schema e catálogo mínimo. Capacidade tem proprietário único derivado do manifesto. O DAG diferencia educação, operação, infraestrutura obrigatória/opcional e integração funcional. Detectar ciclos em todas as arestas. Preservar competências após aposentadoria de exames e evoluir profundidade L1–L5 sem duplicar código por trilha.

Alternativas: árvore de diretórios por certificação duplica infraestrutura; inferir dependência por número quebra isolamento; motor de expressões e orquestrador completo são desnecessários nesta fase. JSON Schema com biblioteca consolidada evita um validador de schema próprio; o subconjunto JSON evita dependência extra de parser YAML. As dependências de validação são fixadas por versão/hash.

Consequências: schema e referências são testáveis; não há descoberta de consumidores ativos na AWS. Cleanup exige inventário privado, verificação de consumidores, ordem inversa e aprovação. Uma capacidade pode ser reprovisionada em vez de permanecer ativa. [Contratos e lifecycle](../architecture/dependencies.md) são a referência normativa; dependências opcionais são texto revisável, sem expressão executável.
