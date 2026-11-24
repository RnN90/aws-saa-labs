# LAB 05 — Amazon SQS & SNS

**Status: planejado.** Não há Terraform, recursos provisionados, testes executados ou publicação externa confirmada. [Manifesto](lab.yaml) · [Roadmap](../../docs/roadmap/README.md).

## Cenário e objetivos iniciais

Uma equipe precisa da capacidade `messaging` como componente reutilizável, sem replicá-la por certificação. Projetar desacoplamento, publicação/assinatura e processamento idempotente.

## Dependências, alternativas e ownership

Não presumir dependência do LAB 04 pela numeração. Integrações reais serão declaradas ao escolher os produtores/consumidores. Antes da implementação, comparar alternativas, definir requisitos, trade-offs, contrato de inputs/outputs, conta/região autorizadas e recursos pertencentes exclusivamente ao LAB. Manter estado separado e nunca assumir ownership de recursos de outro stack.

## Validação, segurança e custos planejados

Planejar testes de entrega, repetição, falha e mensagens não processadas. Avaliar requisições, retenção e cleanup dos consumidores antes das filas/tópicos. Usar credenciais temporárias e menor privilégio; não assumir gratuidade. Se houver simulação por limite de orçamento, identificá-la explicitamente.

## Próxima etapa e critérios de aceite

Detalhar cenário, revisão teórica, arquitetura/diagrama, testes, troubleshooting, questões autorais e respostas, implementação autorizada, cleanup ou retenção controlada, scorecard, documentação, três publicações e retrospectiva conforme o [padrão de aprendizado](../../docs/standards/learning-publication.md). Dividir em sessões de 45–75 minutos quando viável. Esses itens são pendências, não entregas executadas. Aplicar os [Quality Gates](../../docs/standards/quality-gates.md).
