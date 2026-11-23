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

## Documentação

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

- Preserve Organizations, IAM Identity Center, MFA, atribuições de acesso e a VPC padrão.
- Limpeza de infraestrutura exige confirmação humana do alvo, dependências e conta/região.
- O operador do LAB 00 não tem permissões de exclusão; não amplie sua política para realizar limpeza.
- A auditoria confirmada cobre NAT Gateways, Elastic IPs e VPC Endpoints em `sa-east-1`. Nunca declare a conta livre de cobranças com base nela.
- Ao entregar, apresente arquivos criados, verificações realmente executadas e pendências para revisão, sem commit automático.
