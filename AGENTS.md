# Instruções para agentes — aws-saa-labs

## Escopo e autorização

- Trabalhe exclusivamente neste repositório e preserve alterações existentes do usuário.
- Esta etapa é documental: registre o LAB 00 já executado, sem provisionar recursos.
- Não execute comandos que criem, alterem ou excluam recursos AWS.
- Não modifique arquivos locais do AWS CLI, credenciais, caches ou sessões SSO. Não execute login ou logout durante a documentação.
- Não consulte contas AWS para complementar evidências sem autorização explícita. Validações desta entrega são locais.
- Não execute `git commit`, `git push`, nem crie Pull Requests. Deixe os arquivos para revisão humana.

## Estrutura e nomenclatura

- Use `labs/labNN-tema`, numeração de dois dígitos e nomes em `kebab-case`.
- O LAB 00 contém README, documentos em `docs/`, política em `iam/policies/` e diagramas Mermaid em `diagrams/`.
- LABs 01–05 estão apenas planejados. Não crie documentação de implementação, recursos fictícios ou arquivos de preenchimento para eles.
- `shared/scripts`, `shared/templates` e `.github/workflows` ficam reservados para necessidades futuras.

## Arquitetura evolutiva e cumulativa

- Os laboratórios formam uma plataforma AWS evolutiva e cumulativa. Organize os LABs em uma sequência lógica de evolução arquitetural, permitindo reutilizar a fundação em laboratórios posteriores e em outras certificações AWS, sem reconstrução desnecessária.
- É permitido e recomendado referenciar recursos e configurações de LABs anteriores quando houver relação técnica real. Documente essa relação e use links relativos para o LAB de origem.
- Cada LAB deve identificar pré-requisitos, recursos herdados, recursos novos, dependências e possibilidades de reutilização futura. Quando não houver itens em uma dessas categorias, explicite isso sem inventar componentes ou dependências.
- Para cada recurso compartilhado, registre o LAB de origem, os LABs consumidores conhecidos e a responsabilidade por manutenção e ciclo de vida, incluindo os critérios para preservação ou remoção.
- Diferencie recursos existentes e confirmados de recursos planejados e de opções de arquitetura. Uma opção não implica implementação; registre separadamente se foi adotada. Não afirme que recursos futuros já foram provisionados.
- A evolução para outras certificações é uma possibilidade arquitetural; não representa novos LABs ou recursos já implementados. LABs apenas planejados permanecem sujeitos às restrições de estrutura desta etapa.

## Documentação

- Cada LAB deve documentar os recursos, configurações, decisões arquiteturais, validações e procedimentos de cleanup de seu escopo, incluindo dependências reais e recursos herdados da plataforma. Não mencione recursos legados, treinamentos externos, incidentes históricos ou configurações particulares que não pertençam à plataforma de laboratórios.
- Escreva em português brasileiro, preservando a terminologia técnica AWS quando apropriado.
- Separe histórico confirmado, procedimento reproduzível, resultado esperado e validação pendente.
- Não invente saídas, evidências, datas de execução, versões exatas ou nomes de recursos.
- Não afirme que comandos de exemplo foram executados. Explicite as limitações das verificações.
- Use links relativos para arquivos internos e referências oficiais AWS para detalhes técnicos.
- Diferencie instruções no Console de comandos CLI e identifique a identidade necessária em cada etapa.

## Segurança e menor privilégio

- Não leia nem publique credenciais, tokens, arquivos `.env`, caches SSO ou material MFA.
- Não inclua dados pessoais, IDs reais de conta, ARNs reais, e-mails ou URLs específicas do portal.
- Preserve exatamente a política IAM validada do LAB 00. Ampliação de permissões exige revisão humana explícita.
- Não recomende `AdministratorAccess` como solução para falhas do operador.
- Não edite roles `AWSReservedSSO` diretamente; documente seu gerenciamento pelo IAM Identity Center.
- Não trate SCPs como restrição de usuários ou roles da conta de gerenciamento.

## Validação local

- Valide JSON, ações IAM esperadas, links relativos, cercas de código e estrutura Markdown.
- Verifique a coerência dos diagramas; informe se não houver renderizador Mermaid disponível.
- Revise a documentação e o diff em busca de segredos e identificadores antes da entrega.
- Não confunda parse de JSON com validação IAM pelo serviço ou com teste de autorização.
- Não instale ferramentas nem acesse a AWS apenas para obter um resultado de validação documental.

## Custos e limpeza

- Cada LAB deve classificar seus recursos como fundacionais/compartilhados ou temporários. Recursos fundacionais podem permanecer ativos para reutilização em LABs posteriores, desde que sua manutenção seja justificada, suas dependências sejam documentadas e seus custos sejam avaliados. Recursos temporários devem possuir procedimento de remoção seguro. A conclusão de um LAB não exige a destruição de sua infraestrutura quando ela integra a fundação reutilizável da plataforma.
- Preserve Organizations, IAM Identity Center, MFA e atribuições de acesso compartilhadas. Reversões específicas do LAB exigem aprovação humana e não podem comprometer outros acessos.
- Cleanup exige confirmação humana do alvo, dependências e conta; confirme também a região quando aplicável.
- O cleanup de um LAB não pode remover recursos ainda necessários para LABs posteriores. Antes de propor remoção de recursos compartilhados, confira os consumidores documentados e preserve as dependências necessárias à continuidade da plataforma.
- Recursos temporários devem ser removidos quando não forem mais necessários, visando controle de custos. Documente sua finalidade, condição de encerramento e responsável pela remoção; a execução depende da revisão de alvos e dependências e da confirmação humana exigidas acima.
- O operador do LAB 00 não tem permissões de exclusão; não amplie sua política para realizar limpeza.
- Não declare a conta livre de cobranças com base nas validações de identidade e acesso do LAB 00.
- Ao entregar, apresente arquivos criados, verificações realmente executadas e pendências para revisão, sem commit automático.
