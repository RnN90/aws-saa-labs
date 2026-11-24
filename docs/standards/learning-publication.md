# Aprendizado, evidências e publicação

Cada LAB deve conter as etapas abaixo, adaptadas ao escopo. O [template](../../shared/templates/lab-readme.md) é uma estrutura reutilizável, não uma afirmação de implementação.

1. Cenário corporativo e problema verificável.
2. Objetivos de aprendizagem observáveis e nível interno L1–L5.
3. Revisão teórica com referências oficiais.
4. Arquitetura e requisitos, incluindo dependências/ownership.
5. Alternativas e trade-offs fundamentados.
6. Segurança e custos, antes de executar.
7. Implementação hands-on somente quando autorizada.
8. Testes e validação com hipóteses e evidências.
9. Troubleshooting orientado por sintomas, causas e diagnóstico.
10. Questões autorais de conhecimento, com respostas justificadas.
11. Cleanup ou retenção controlada com prazo, responsável e consumidores.
12. Revisão de engenharia e scorecard.
13. Documentação reproduzível e sanitizada.
14. Publicação revisada nos três canais.
15. Retrospectiva: aprendizado, limitações e próximo incremento.

Preferir sessões compactas de 45–75 minutos quando compatíveis. Dividir cenários complexos em etapas sem sacrificar qualidade. Não usar dumps de exames, reproduzir questões protegidas ou prometer aprovação em certificação. Teoria, prática, arquitetura, simulação e execução real devem ser diferenciadas nas evidências.

## Três entregáveis, sem cópias extensas

| Canal | Propósito | Critério de publicação |
| --- | --- | --- |
| GitHub | Código-fonte, contratos, procedimentos e evidências técnicas | PR revisado e integrado; links reais e validações descritas |
| Artigo no portal pessoal | Conceitos, arquitetura, alternativas e trade-offs | Texto educacional revisado; apontar para código e LAB, sem duplicar todo o procedimento |
| Hands-on na seção LABs do portal | Reprodução, comandos, validação, troubleshooting e cleanup | Passos testados no escopo declarado e limites explícitos; referenciar artigo para aprofundamento |

GitHub documentado não prova que artigo ou hands-on já existem. Manifestos mantêm os três estados separados e URLs nulas até confirmação. Atualizações devem apontar para versão/commit e contrato usados; publicação antiga não deve ensinar comandos incompatíveis silenciosamente.

ChatGPT e Codex apoiam pesquisa, redação, revisão e código por Git e Pull Request. Humanos aprovam decisões, mudanças AWS e publicação. Lovable é opcional e não é dependência do fluxo. O repositório do portal será tratado em atividade independente; nenhum arquivo ou conteúdo do portal é modificado/publicado neste PR. Toda documentação é pt-BR; termos técnicos consolidados, identificadores, código e Conventional Commits permanecem em inglês.
