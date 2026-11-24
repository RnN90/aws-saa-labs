# Roadmap evolutivo por ondas

O programa cobre competências de todas as trilhas do [catálogo de certificações](../../certifications/README.md), sem prometer cobertura integral. Ondas organizam competências, não contas, stacks ou pré-requisitos automáticos. L1 fundamentos, L2 implementação, L3 operação e troubleshooting, L4 arquitetura e L5 liderança de engenharia são níveis **internos**, não classificações AWS.

| Onda | Tema | Competências/capacidades e profundidade alvo | Sobreposição a reutilizar |
| --- | --- | --- | --- |
| 01 | Cloud Core Foundations | LABs 00–06 na sequência abaixo; identidade, rede, computação, armazenamento, serverless, mensageria e observabilidade; L1–L3 | Base das trilhas Foundational e Associate; fundamentos de Security/Networking |
| 02 | Resilient Cloud Architecture | Alta disponibilidade, recuperação, desacoplamento, desempenho e compromissos de custo; L3–L4 | SAA/SAP, CloudOps e DevOps reutilizam fundações |
| 03 | Platform Engineering & DevSecOps | CI, testes de infraestrutura, políticas, experiência de desenvolvimento, isolamento e estado; L2–L4 | DVA, DOP, SOA e SCS compartilham automação |
| 04 | Advanced Architecture & AI Engineering | Decisões de arquitetura, fundamentos de IA, Responsible AI e avaliação; L1–L4 | AIF, SAP e AIP; IA não duplica segurança e redes |
| 05 | Enterprise Networking | Redes híbridas, conectividade, DNS, inspeção e diagnóstico; L3–L4 | ANS e SAP; manter competências após aposentadoria do exame |
| 06 | Enterprise Security & Governance | Identidade multicliente, governança, proteção de dados e resposta; L3–L5 | SCS, SAP, DOP e AIB reutilizam controles |
| 07 | Data Engineering & Analytics | Ingestão, transformação, qualidade, catálogo e lifecycle; L2–L4 | DEA, SAA e MLA compartilham armazenamento e observabilidade |
| 08 | Machine Learning & MLOps | Dados, treinamento, implantação, avaliação, drift e operação; L2–L4 | MLA, DEA, DOP e AIF |
| 09 | Enterprise Generative AI & Agentic Systems | RAG, agentes, avaliação, guardrails, custos e integração; L2–L5 | AIP, AIF, MLA e AIB; reutilizar plataforma e segurança |
| 10 | Enterprise Architecture & Capstone | Trade-offs, negócio, sustentabilidade, estratégia e evidências integradas; L4–L5 | SAP e AIB; síntese de capacidades sem repetir implementações |

As certificações relacionadas são hipóteses de afinidade até mapeamento contra objetivos oficiais e evidências. Dentro de cada onda, só criar novos LABs quando houver lacuna de aprendizagem: aumentar profundidade ou criar cenário consumidor antes de duplicar recursos. Revisar roadmap por PR ao concluir cada LAB, mudar contrato ou atualizar um guia AWS. Não criar diretórios antecipados para as ondas 02–10.

## Sequência inicial preservada e ampliada

| LAB | Diretório | Situação e capacidade |
| --- | --- | --- |
| 00 | [lab00-identity-governance](../../labs/lab00-identity-governance/README.md) | Implementado; identity-foundation; histórico e política preservados |
| 01 | [lab01-vpc-networking](../../labs/lab01-vpc-networking/README.md) | Implementado e destruído após validação original; network-foundation |
| 02 | [lab02-ec2-connectivity](../../labs/lab02-ec2-connectivity/README.md) | Planejado; compute-connectivity, primeiro consumidor obrigatório da rede |
| 03 | [lab03-s3-security](../../labs/lab03-s3-security/README.md) | Planejado; storage-security; sem dependência automática de VPC |
| 04 | [lab04-lambda-api-gateway](../../labs/lab04-lambda-api-gateway/README.md) | Planejado; serverless-api; VPC somente no cenário privado |
| 05 | [lab05-sqs-sns](../../labs/lab05-sqs-sns/README.md) | Planejado; messaging |
| 06 | [lab06-cloudwatch](../../labs/lab06-cloudwatch/README.md) | Planejado; observability; integrações concretas serão declaradas ao definir o cenário |

Antes desta revisão, LABs 02–05 existiam apenas como referências de planejamento, sem diretórios versionados. A nova numeração atualiza essas referências; nenhum LAB implementado/publicado foi renumerado. Os cinco novos diretórios contêm planejamento real e manifesto, sem Terraform fictício.
