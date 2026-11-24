# LAB 04 — AWS Lambda & API Gateway

**Status: planejado.** Não há Terraform, recursos provisionados, testes executados ou publicação externa confirmada. [Manifesto](lab.yaml) · [Roadmap](../../docs/roadmap/README.md).

## Cenário e objetivos iniciais

Uma equipe precisa da capacidade `serverless-api` como componente reutilizável, sem replicá-la por certificação. Projetar API serverless com autorização, validação de entradas e tratamento de falhas.

## Dependências, alternativas e ownership

Cenário básico sem dependência de VPC; network-foundation é opcional somente ao integrar a função com recursos privados. O manifesto registra esse cenário textual. Antes da implementação, comparar alternativas, definir requisitos, trade-offs, contrato de inputs/outputs, conta/região autorizadas e recursos pertencentes exclusivamente ao LAB. Manter estado separado e nunca assumir ownership de recursos de outro stack.

## Validação, segurança e custos planejados

Planejar testes de autorização, entradas inválidas, erros e limites. Avaliar requisições, execução, logs e conectividade privada antes de implementar. Usar credenciais temporárias e menor privilégio; não assumir gratuidade. Se houver simulação por limite de orçamento, identificá-la explicitamente.

## Próxima etapa e critérios de aceite

Detalhar cenário, revisão teórica, arquitetura/diagrama, testes, troubleshooting, questões autorais e respostas, implementação autorizada, cleanup ou retenção controlada, scorecard, documentação, três publicações e retrospectiva conforme o [padrão de aprendizado](../../docs/standards/learning-publication.md). Dividir em sessões de 45–75 minutos quando viável. Esses itens são pendências, não entregas executadas. Aplicar os [Quality Gates](../../docs/standards/quality-gates.md).
