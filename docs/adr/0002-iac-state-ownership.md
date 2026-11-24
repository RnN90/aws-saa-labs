# ADR 0002 — Terraform, isolamento de estado e ownership

Data: 2026-11-24. Estado: **aceito** no desenho; somente LAB 01 possui stack Terraform implementado.

Contexto: o [LAB 01](../../labs/lab01-vpc-networking/README.md) já utiliza Terraform, lock versionado, tags comuns e estado local. Doze recursos não justificam módulos complexos. Consumo de rede por outro LAB exige limite de ownership.

Decisão: manter Terraform como IaC, preservar stack/endereços/locks atuais e exigir um proprietário/estado por recurso. LAB 02 terá estado independente; consome outputs autorizados e nunca redefine/importa os recursos do LAB 01. Backend remoto e locking distribuído são propostas condicionadas à colaboração real, não infraestrutura implementada.

Alternativas: monólito compartilhado mistura lifecycle; copiar recursos causa duplicação e conflito de estados; extração prematura de módulos aumenta custo de mudança. O contrato explícito permite evolução incremental.

Consequências: execução local única por ambiente/diretório até haver isolamento e coordenação adequados. Concorrência e recuperação precisam de testes antes de adoção distribuída. Critérios e evidências em [dependências](../architecture/dependencies.md) e [evolução Terraform](../architecture/terraform-evolution.md).
