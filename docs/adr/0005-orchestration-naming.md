# ADR 0005 — Orquestração e nome do repositório

Data: 2026-11-24. Estado: **proposto**.

Contexto: o nome aws-saa-labs expressa a origem SAA-C03, mas o programa agora contempla todas as trilhas AWS. Vários consumidores poderão justificar coordenação no futuro; hoje só há uma stack implementada.

Proposta: manter o nome atual e avaliar aws-engineering-labs em atividade própria, com inventário de URLs, redirects, integrações e revisão humana. Desenvolver [labctl](../architecture/labctl.md) somente quando demandas concretas justificarem; nesta fase, limitar-se ao validador de catálogo.

Alternativas: renomear agora criaria quebra de links e custos de migração desnecessários; orquestrar recursos antes de existir consumidor real cria complexidade sem evidências.

Consequências e aceite futuro: ADR adicional deve aprovar migração de nome ou executor, com testes, custos, ownership, consumidores ativos, proteção destrutiva e estratégia de falha. Nada disso é implementado neste PR; repositório e portal não são renomeados.
