# LAB 06 — Amazon CloudWatch & Observability

**Status: planejado.** Não há Terraform, recursos provisionados, testes executados ou publicação externa confirmada. [Manifesto](lab.yaml) · [Roadmap](../../docs/roadmap/README.md).

## Cenário e objetivos iniciais

Uma equipe precisa da capacidade `observability` como componente reutilizável, sem replicá-la por certificação. Definir sinais, alarmes, retenção e hipóteses de troubleshooting.

## Dependências, alternativas e ownership

Workload observado e integrações ainda não definidos; declarar dependências funcionais quando o cenário for aprovado, sem adivinhar consumidores. Antes da implementação, comparar alternativas, definir requisitos, trade-offs, contrato de inputs/outputs, conta/região autorizadas e recursos pertencentes exclusivamente ao LAB. Manter estado separado e nunca assumir ownership de recursos de outro stack.

## Validação, segurança e custos planejados

Planejar sinais esperados, ausência de dados, alertas positivos/negativos e custo de ingestão/retenção. Remover integrações antes de recursos observados. Usar credenciais temporárias e menor privilégio; não assumir gratuidade. Se houver simulação por limite de orçamento, identificá-la explicitamente.

## Próxima etapa e critérios de aceite

Detalhar cenário, revisão teórica, arquitetura/diagrama, testes, troubleshooting, questões autorais e respostas, implementação autorizada, cleanup ou retenção controlada, scorecard, documentação, três publicações e retrospectiva conforme o [padrão de aprendizado](../../docs/standards/learning-publication.md). Dividir em sessões de 45–75 minutos quando viável. Esses itens são pendências, não entregas executadas. Aplicar os [Quality Gates](../../docs/standards/quality-gates.md).
