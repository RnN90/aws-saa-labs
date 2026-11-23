# Implementação — LAB 00

## Como usar este procedimento

O LAB já foi executado. As instruções abaixo reconstituem um caminho reproduzível compatível com o histórico confirmado; não são transcrição de cliques, prompts ou comandos preservados da execução original. Os nomes de opções do Console podem mudar.

As etapas de Console exigem um administrador autorizado e alteram a configuração AWS quando realizadas por uma pessoa. Os comandos de configuração/login modificam o ambiente local ou iniciam sessões. **Nenhuma dessas ações foi executada pelo agente nesta entrega.** Em ambiente já configurado, revise o estado existente em vez de recriar componentes.

## 1. Console AWS — conferir Organizations

Identidade necessária: administrador autorizado da conta de gerenciamento existente.

1. Acesse o Console com o método administrativo aprovado. Não utilize root na rotina operacional.
2. Abra **AWS Organizations** e confira se a conta pertence à organização esperada e se todas as funcionalidades estão habilitadas (**All features**).
3. Em uma reprodução sem organização, o administrador deve avaliar a criação de uma organização com todas as funcionalidades. Se já existir no modo de faturamento consolidado, a habilitação de todas as funcionalidades exige o fluxo de aprovação apropriado. No LAB documentado, Organizations já está habilitado; não crie uma segunda estrutura.
4. Preserve a organização e a conta de gerenciamento. Este LAB não exige criar contas membro, OUs ou SCPs.

Consulte o [procedimento oficial de configuração de uma organização](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_tutorials_basic.html). A política do operador não autoriza essa administração.

## 2. Console AWS — IAM Identity Center

Identidade necessária: administrador autorizado a configurar IAM Identity Center e sua integração organizacional.

1. Selecione a região `sa-east-1` e abra **IAM Identity Center**.
2. Verifique a instância existente. Em uma reprodução inicial, habilite uma **organization instance**, integrada ao AWS Organizations; uma account instance não atende à arquitetura deste LAB.
3. Em **Settings**, confira a fonte de identidades: **Identity Center directory**, o diretório integrado.
4. Consulte a URL do AWS access portal apenas no ambiente privado. Não copie essa URL para o GitHub.
5. Preserve a região e a fonte existentes; mudança de região ou diretório exige planejamento próprio e pode afetar o acesso.

Referência: [instâncias do IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/identity-center-instances.html).

## 3. Console AWS — usuário, grupo e MFA

1. Em **Users**, configure uma identidade individual para o participante, sem compartilhar credenciais. A identidade já existe no histórico; seu nome e dados pessoais são omitidos.
2. Em **Groups**, configure o grupo `AWS-SAA-Labs` e associe o usuário.
3. Em **Settings → Authentication → Multi-factor authentication → Configure**, selecione **Every time they sign in (always-on)**.
4. Defina o tratamento de usuários sem dispositivo para exigir registro no login ou bloquear acesso até o registro. Não selecione opção que permita acesso sem MFA.
5. O participante conclui privadamente o registro de um autenticador compatível e realiza login com MFA.

O requisito de MFA em todos os logins é confirmado. O método do autenticador, os passos de inscrição e a opção exata para usuários ainda sem dispositivo não foram registrados; confira-os na revisão humana. O MFA do usuário root e de eventuais usuários IAM possui configuração independente, não coberta pelo histórico do Identity Center.

Referência: [MFA no IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/mfa-getting-started.html).

## 4. Console AWS — Permission Set e atribuição

1. Em **Permission sets**, configure um Permission Set personalizado chamado `SAA-Lab-Operator`.
2. Use a [política IAM validada](../iam/policies/saa-lab-operator.json) como inline policy do Permission Set na reprodução. O histórico confirma o conteúdo da política, mas não detalha a forma original de anexação.
3. Defina **Session duration** como **1 hour** (`PT1H`).
4. Revise as políticas associadas para evitar permissões adicionais às publicadas; não acrescente `AdministratorAccess`.
5. Em **AWS accounts**, selecione a conta aprovada e escolha **Assign users or groups**. Selecione o grupo `AWS-SAA-Labs` e o Permission Set `SAA-Lab-Operator`.
6. Aguarde a conclusão da atribuição e do provisionamento. Após mudanças futuras no Permission Set, confira se foram provisionadas nas contas atribuídas.
7. Verifique pelo portal se a conta e o Permission Set estão disponíveis ao participante. Não edite a role `AWSReservedSSO` criada pelo serviço.

O operador não consegue executar essas etapas com a própria política. Consulte [criação de Permission Sets](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) e a explicação de [roles e privilégios](architecture.md).

## 5. CLI local — configuração para reprodução humana

Ambiente confirmado: AWS CLI v2 em Ubuntu, perfil `aws-saa-labs`, região padrão `sa-east-1`. O nome privado da estação e a versão exata da CLI não são necessários à reprodução e não são publicados.

A instalação da CLI v2 é um pré-requisito. Caso necessário em outro ambiente, siga a [instalação oficial](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html). Não há instalação automática neste repositório.

Comandos de referência, **não executados nesta entrega**:

```bash
aws --version
aws configure sso --profile aws-saa-labs
```

No assistente, informe privadamente:

| Campo | Valor ou orientação |
| --- | --- |
| SSO session name | Nome local escolhido para a sessão; o histórico não informa esse nome |
| SSO start URL | URL real do portal obtida no Console; não publicar |
| SSO region | `sa-east-1` |
| SSO registration scopes | `sso:account:access` para acesso às contas atribuídas |
| AWS account | Conta aprovada pelo responsável; não publicar o ID |
| Role / Permission Set | `SAA-Lab-Operator` |
| CLI default client Region | `sa-east-1` |
| CLI default output format | `json` sugerido para reprodução; formato histórico não informado |
| CLI profile name | `aws-saa-labs` |

O assistente pode abrir o navegador e iniciar autenticação. O usuário deve verificar o domínio e concluir o MFA. Para iniciar uma sessão posteriormente, a instrução humana é:

```bash
aws sso login --profile aws-saa-labs
```

A CLI mantém configuração e caches no ambiente do usuário. Não os copie para o repositório; não exporte credenciais temporárias para arquivos de documentação. As instruções seguem o [fluxo oficial de autenticação SSO da CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso.html).

## 6. CLI — validação de leitura

Após autenticação humana, siga os [comandos e critérios de validação](validation.md). Eles usam explicitamente o perfil e a região do LAB, sem operações de provisionamento.

Em caso de `AccessDenied`, confira perfil, conta atribuída, associação ao grupo, provisionamento do Permission Set e possíveis negações aplicáveis. Em caso de sessão expirada, o participante deve autenticar novamente pelo fluxo aprovado. Nenhum desses casos justifica ampliar automaticamente a política.

## 7. Limpeza histórica

A VPC personalizada legada foi removida manualmente e a VPC padrão preservada. Não há registro detalhado das dependências, comandos, IDs ou identidade usados nessa remoção; não é possível reconstruir uma sequência exata de exclusão. A política publicada não autoriza essa operação. Consulte [limpeza e custos](cleanup.md) para as salvaguardas de qualquer intervenção futura.
