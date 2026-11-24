# Quality Gates e Definition of Done

Referência: os seis pilares do [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/the-pillars-of-the-framework.html): excelência operacional, segurança, confiabilidade, eficiência de desempenho, otimização de custos e sustentabilidade. São referências de revisão, não certificação automática de conformidade.

## Scorecard de 100 pontos

Cada linha tem três verificações com o mesmo peso dentro da dimensão. Avaliar cada verificação em 0 (ausente), 0,5 (parcial, lacuna explícita) ou 1 (critério atendido e evidência revisável). Evidência deve identificar arquivo/execução, escopo, data, responsável e limite. Autodeclaração sem artefato recebe 0. Revisão humana confirma a pontuação; CI não atribui nota arquitetural.

| Dimensão | Pontos | Três critérios verificáveis e evidências |
| --- | ---: | --- |
| Arquitetura | 15 | Requisitos e alternativas ligados ao cenário; diagrama/contratos/ownership coerentes; análise de confiabilidade, desempenho e sustentabilidade com limites explícitos. Evidência: README, ADR e revisão de trade-offs. |
| Infrastructure as Code | 15 | Código formatado/validado e providers fixados; parâmetros/outputs e ownership verificáveis; state/contratos/lifecycle sem colisão. Evidência: diff, CI, lock e contrato. |
| Segurança | 15 | Conta/região e identidade temporária definidas; superfície de acesso e menor privilégio revisados; dados sensíveis ausentes e controles/limitações explícitos. Evidência: threat review, scan e testes autorizados. |
| Testes e validações | 15 | Hipóteses e resultados esperados explícitos; testes positivos/negativos adequados e executados no escopo alegado; evidências distinguem estático, Control Plane, Data Plane e simulação. Evidência: comandos, resultados sanitizados e limites. |
| DevOps e automação | 10 | Checks reproduzíveis sem credenciais desnecessárias; actions/permissões/timeouts revisados; PR/commits e tratamento de falhas documentados. Evidência: workflow, CI e revisão. |
| FinOps e cleanup | 10 | Estimativa e risco financeiro com região/data; inventário/responsável/prazo de retenção; cleanup inverso e verificação de remanescentes. Evidência: estimativa, registro privado referenciado de forma sanitizada e checklist. |
| Documentação | 10 | pt-BR e navegação corretos; procedimento reproduzível/diagramas/limitações; referências e publicação com status verdadeiro. Evidência: links, revisão e URLs quando publicadas. |
| Qualidade educacional | 10 | Objetivos mensuráveis e nível interno; questões autorais/troubleshooting/retrospectiva; rastreabilidade a competências sem duplicação ou dumps. Evidência: README, matriz e revisão didática. |

Meta: **90/100**, sem falhas críticas. Para itens realmente não aplicáveis, o revisor registra a justificativa e remove somente o peso desses itens do denominador: `nota = 100 × pontos obtidos / pontos aplicáveis`. Não marcar como não aplicável um teste necessário mas não executado, uma dívida ou uma limitação de ferramentas: esses itens são pendentes/parciais. Se não houver pontos aplicáveis, não há nota nem aprovação. Não comparar notas sem publicar denominador e exclusões.

## Critérios impeditivos

Segredo/state/plano exposto, operação AWS não autorizada, recurso gerenciado por dois states, exclusão de dependência ativa, custo não avaliado, alegação falsa de execução/cobertura, teste crítico falhando, DAG cíclico ou contrato incompatível impedem aceite independentemente da nota. Suspeita de evidência inválida exige revisão. Retenção sem responsável/prazo e permissões administrativas indiscriminadas também bloqueiam execução futura.

## Definition of Done por tipo de entrega

**Fundação documental/planejamento:** schema, catálogo, DAG, links e testes aprovados; status planejado explícito; arquitetura/contratos/custos/riscos/alternativas revisáveis; nenhum recurso apresentado como criado; PR aberto. Não exigir teste real de infraestrutura inexistente nem classificar o LAB planejado como concluído. Esta entrega não atribui automaticamente nota 90 aos LABs históricos.

**LAB implementado:** objetivos e metodologia completos, IaC/testes proporcionais aprovados, execução autorizada ou simulação claramente identificada, riscos e lacunas registrados, evidências sanitizadas, cleanup concluído ou retenção formal aprovada, scorecard ≥90 sem impeditivos e revisão humana. Registrar separadamente aceite técnico e conclusão de publicação; artigo e hands-on pendentes não são publicados ficticiamente. Nenhum agente faz merge ou publicação externa sem autorização.

**Publicação completa:** três entregáveis revisados conforme [metodologia e publicação](learning-publication.md), com links reais. Reprovar cobertura integral de certificação baseada somente em serviços citados.
