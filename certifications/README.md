# Certificações, fontes e rastreabilidade

Verificação: **2026-11-24 (UTC)**. [Catálogo global](catalog.json) registra as 13 trilhas solicitadas, códigos, fontes individuais, status e pendências. O índice solicitado de [guias oficiais](https://docs.aws.amazon.com/aws-certification/latest/examguides/) não retornou conteúdo legível, mas os guias individuais foram acessados. A [página AWS Certification](https://aws.amazon.com/certification/) e páginas específicas complementaram a verificação de disponibilidade. Fonte de verdade externa continua sendo a AWS; os dados locais são um snapshot revisável, não sincronização automática.

| Trilha | Códigos verificados | Estado relevante na data |
| --- | --- | --- |
| Foundational | CLF-C02, AIF-C01 | Guias e páginas disponíveis |
| Associate | SAA-C03, DVA-C03, SOA-C03, DEA-C01, MLA-C02 | DVA em transição; MLA em beta; demais guias verificados |
| Professional | SAP-C03, DOP-C02, AIP-C01 | Guia SAP-C03 confirmado, janela de aplicação pendente; não inferir disponibilidade geral |
| Specialty | SCS-C03, ANS-C01 | ANS com aposentadoria anunciada; manter competências de redes |
| Business | AIB-C01 | Beta confirmado; foco de negócio, não implementação técnica |

DVA-C03: o [guia](https://docs.aws.amazon.com/aws-certification/latest/developer-associate-03/developer-associate-03.html) confirma inscrições em 27/10/2026 e último dia de DVA-C02 em 30/11/2026. Não apagar competências ou evidências da versão anterior; revisar diferenças de objetivos antes de migrar cobertura.

MLA-C02: o [guia](https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02.html) confirma o código; a [página da certificação](https://aws.amazon.com/certification/certified-machine-learning-engineer-associate/) anuncia beta em inglês, retirada do MLA-C01 em inglês em 28/09/2026 e continuidade em outros idiomas até disponibilidade geral. A tabela comercial apresenta `ME1-C02`, divergente do título e guia; registrar a inconsistência e reconferir antes da inscrição, sem alterar silenciosamente o código do programa.

SOA-C03: CloudOps Engineer é o novo nome associado a essa versão; o [guia mantém o caminho sysops-administrator](https://docs.aws.amazon.com/aws-certification/latest/sysops-administrator-associate-03/sysops-administrator-associate-03.html). A [página comercial](https://aws.amazon.com/certification/certified-cloudops-engineer-associate/) informa retirada de idiomas coreano/chinês simplificado após 19/11/2026; isso não significa aposentadoria global do exame.

ANS-C01: a [página oficial](https://aws.amazon.com/certification/certified-advanced-networking-specialty/) anuncia último dia em 31/12/2026. A onda Enterprise Networking permanece após a aposentadoria; não descartar conhecimento ou laboratórios válidos. AIB-C01 consta como beta na [página oficial](https://aws.amazon.com/certification/certified-ai-business-strategist/). Para SAP-C03, DOP-C02 e SCS-C03, detalhes de aplicação por idioma ainda exigem reconferência; o guia prova o código, não todas as condições comerciais.

## Matriz inicial SAA-C03

[saa-c03.json](saa-c03.json) explicita os 14 objetivos numerados dos quatro domínios oficiais, com fontes por domínio, tradução pt-BR, competência interna, nível, LABs, artigos, evidências, lacunas e modalidades teórica/prática/arquitetural. O mapeamento é inicial e conservador: identidade e rede têm cobertura parcial documentada; outros objetivos são planejados ou não mapeados. Não há objetivo declarado integralmente validado nem certificação integralmente coberta. Duas AZs e serviços citados não provam resiliência, desempenho ou domínio do exame.

| Status interno | Regra |
| --- | --- |
| `not-mapped` — Não mapeado | Não há associação fundamentada ou a fonte ainda precisa de validação |
| `planned` — Planejado | Objetivo e LAB relacionados, sem evidência de execução suficiente |
| `partial` — Parcialmente coberto | Evidência do recorte indicado, com lacunas explícitas |
| `covered` — Coberto | Todos os requisitos do objetivo no escopo/mode avaliado têm evidência rastreável e revisão |
| `validated` — Validado | Cobertura revisada independentemente, com testes/evidências atuais suficientes e responsável/data |

Teoria: explicação correta e questões autorais; prática: execução e testes do escopo autorizado; arquitetura: requisitos, alternativas e trade-offs revisados. Evidências históricas informadas pelo responsável não se transformam em testes reexecutados pelo agente. URLs de artigos permanecem vazias até publicação real. Não calcular percentual de aprovação no exame ou completude do programa a partir da matriz inicial.

## Expansão progressiva

1. Revalidar código/versão/status/idioma no guia e página oficiais, registrando data e divergências. Se inacessíveis, marcar objetivos pendentes de validação, sem inventá-los.
2. Inventariar objetivos oficiais e comparar competências já atendidas pelos LABs; reutilizar e aprofundar antes de criar outro LAB.
3. Registrar cobertura separada por modalidade e evidência, com lacunas. Níveis L1–L5 são internos, não equivalências automáticas com categorias de exames.
4. Adicionar matriz de outra certificação somente com fonte verificada e testes de referência equivalentes aos da SAA. Hoje apenas SAA possui matriz detalhada; o catálogo global não equivale a mapeamento de todas as trilhas.
5. Revisar por PR e manter histórico de versões aposentadas; migração para novo código requer revisão de diferenças e evidências. Cobertura de certificação exige todos os objetivos e modalidades necessárias, sem extrapolar presença de serviços.
