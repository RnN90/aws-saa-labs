# LAB 03 — Amazon S3 & Storage Security

**Status: planejado.** Não há Terraform, recursos provisionados, testes executados ou publicação externa confirmada. [Manifesto](lab.yaml) · [Roadmap](../../docs/roadmap/README.md).

## Cenário e objetivos iniciais

Uma equipe precisa da capacidade `storage-security` como componente reutilizável, sem replicá-la por certificação. Proteger objetos, revisar criptografia, Block Public Access, propriedade, políticas e retenção.

## Dependências, alternativas e ownership

Não há dependência obrigatória da VPC. Acesso federado equivalente ao LAB 00 é pré-requisito operacional a confirmar; não implica recriar identidade. Antes da implementação, comparar alternativas, definir requisitos, trade-offs, contrato de inputs/outputs, conta/região autorizadas e recursos pertencentes exclusivamente ao LAB. Manter estado separado e nunca assumir ownership de recursos de outro stack.

## Validação, segurança e custos planejados

Comparar acesso permitido e negado, criptografia e versões/retention antes de implementar. Avaliar armazenamento, requisições, transferência e cleanup de todas as versões. Usar credenciais temporárias e menor privilégio; não assumir gratuidade. Se houver simulação por limite de orçamento, identificá-la explicitamente.

## Próxima etapa e critérios de aceite

Detalhar cenário, revisão teórica, arquitetura/diagrama, testes, troubleshooting, questões autorais e respostas, implementação autorizada, cleanup ou retenção controlada, scorecard, documentação, três publicações e retrospectiva conforme o [padrão de aprendizado](../../docs/standards/learning-publication.md). Dividir em sessões de 45–75 minutos quando viável. Esses itens são pendências, não entregas executadas. Aplicar os [Quality Gates](../../docs/standards/quality-gates.md).
