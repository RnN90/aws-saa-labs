# Catálogo de capacidades e manifestos

Capacidades permitem reutilizar o mesmo LAB entre certificações. Uma nova referência de exame não cria código nem infraestrutura duplicados. Antes de criar um LAB, consulte objetivos e lacunas na [matriz de certificações](../certifications/README.md) e o [roadmap](../docs/roadmap/README.md).

| Fonte de verdade | Informação |
| --- | --- |
| `labs/*/lab.yaml` | Identidade, objetivos, status, ownership, capacidades fornecidas/consumidas, dependências e publicação de cada LAB |
| [capabilities.json](capabilities.json) | IDs e descrição curta das capacidades; proprietário derivado de `provides` nos manifestos |
| [catalog.json](../certifications/catalog.json) | Código, fonte oficial, data e status de cada exame |
| [saa-c03.json](../certifications/saa-c03.json) | Objetivos oficiais e evidências de cobertura por modalidade |
| READMEs dos LABs | Procedimentos, arquitetura, explicações e evidências detalhadas |
| Registro privado de ambientes | Recursos ativos, responsáveis, custos e retenção; não presumir atividade pela presença do manifesto |

O validador exige proprietário único para cada capacidade. Consultar `provides` em cada manifesto identifica o LAB proprietário: `identity-foundation` → LAB 00, `network-foundation` → LAB 01; as demais capacidades são planejadas: `compute-connectivity`, `storage-security`, `serverless-api`, `messaging` e `observability`. As listas descritivas não devem ser usadas para inferir provisionamento.

## Formato v1

`lab.yaml` usa deliberadamente **JSON, subconjunto de YAML 1.2**. Isso preserva o formato declarativo solicitado e permite análise segura pela biblioteca padrão, sem parser YAML extra, aliases, tags executáveis ou avaliação de expressões. YAML fora desse subconjunto é rejeitado nesta versão, com erro de sintaxe. Use aspas duplas e `null`; comentários explicativos ficam no README. O [schema JSON Schema 2020-12](../shared/schemas/lab-v1.schema.json) é validado por jsonschema, biblioteca consolidada, em vez de um interpretador de schema próprio. Dependências exclusivas de validação têm versões e hashes fixados em [requirements-catalog.txt](../shared/requirements-catalog.txt), limitados a Linux x86_64 CPython 3.12/3.14; outras plataformas exigem revisão dos hashes de wheels, sem editar locks Terraform.

Todos os campos são obrigatórios; valores não aplicáveis usam `null` ou listas vazias. `status` aceita `implemented`, `planned` e `retired`; não representa recursos ativos. LAB planejado tem `terraform: null` e não contém `.tf`. `publication` separa GitHub, artigo e hands-on; `planned`, `documented` e `published` não são equivalentes. Publicação externa só deve mudar para `published` com URL real e revisão humana. Dificuldade L1–L5 e ondas 1–10 são classificações internas.

`schema_version` é fixado em 1; mudanças incompatíveis exigem novo schema e migração explícita. IDs independem da numeração de apresentação. Cada dependência declara ID, LAB, tipo e cenário textual se opcional; cada consumo aponta para essa aresta e uma versão de contrato. A v1 aceita contrato 1; expansão exige revisão dos consumidores. Campos desconhecidos são rejeitados para evitar erros silenciosos.

## Validação reproduzível

Em um ambiente Python 3.12 ou 3.14 compatível, sem credenciais AWS:

```bash
python3 -m venv /tmp/aws-catalog-venv
/tmp/aws-catalog-venv/bin/python -m pip install --require-hashes -r shared/requirements-catalog.txt
/tmp/aws-catalog-venv/bin/python -m unittest discover -s shared/scripts -p 'test_*.py'
/tmp/aws-catalog-venv/bin/python shared/scripts/validate_catalog.py
```

Execute a partir da raiz do repositório, com arquivos novos preparados para commit: a verificação de Markdown usa `git ls-files` para evitar ler arquivos privados não versionados. Links locais são verificados por existência e confinamento no repositório; âncoras internas e disponibilidade de links externos exigem revisão complementar. Mermaid recebe verificação estrutural básica, não renderização visual. JSON Schema valida forma; verificações semânticas validam referências, ownership e DAG. Nenhuma delas conhece o estado real da AWS ou autoriza provisionamento.
