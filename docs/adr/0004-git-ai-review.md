# ADR 0004 — Git, engenharia assistida por IA e revisão humana

Data: 2026-11-24. Estado: **aceito** para o fluxo de engenharia, sem publicação externa executada nesta entrega.

Contexto: o repositório possui Conventional Commits, branches dedicadas, Pull Requests e CI sem credenciais AWS. A expansão de escopo exige rastreabilidade e conteúdo consistente no GitHub e portal.

Decisão: Git permanece fonte de verdade do desenho e do histórico; estado operacional real continua em registros privados conferidos pelo operador. ChatGPT e Codex apoiam pesquisa, redação, testes e implementação; humanos validam fontes, evidências, custos, mudanças AWS, publicação e merge. Não tratar resposta de IA como evidência de execução. Documentação em pt-BR, commits/identificadores/títulos de PRs em inglês.

Alternativas: edição direta de main e publicação sem revisão reduzem rastreabilidade; depender obrigatoriamente de um gerador externo de sites aumenta acoplamento. Lovable pode ser opcional, mas não é requisito.

Consequências: três entregáveis por LAB, com estados separados; sem duplicação extensa, conforme [publicação](../standards/learning-publication.md). O portal não é modificado neste PR. Evidências existentes: histórico de PRs e workflow; novos conteúdos externos permanecem planejados até revisão e URL real.
