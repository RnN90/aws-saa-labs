# Arquitetura — LAB 00

## Organização e responsabilidades

AWS Organizations está habilitado com todas as funcionalidades. A conta de gerenciamento preexistente administra a organização e concentra responsabilidades de governança e faturamento consolidado. Habilitar todas as funcionalidades permite recursos de governança, mas não comprova que políticas específicas tenham sido criadas ou aplicadas.

O Permission Set `SAA-Lab-Operator` foi atribuído ao grupo `AWS-SAA-Labs` na própria conta de gerenciamento do AWS Organizations, por simplificação educacional. Essa abordagem não representa a arquitetura recomendada para workloads corporativos. O histórico não confirma contas-membro adicionais, OUs, administrador delegado ou SCPs personalizados.

| Responsabilidade | Identidade apropriada |
| --- | --- |
| Configurar Organizations, Identity Center, MFA e atribuições | Administrador autorizado; fora do escopo da política operacional |
| Executar consultas permitidas pela política aprovada | Grupo `AWS-SAA-Labs`, Permission Set `SAA-Lab-Operator` |
| Aprovar e reverter configurações do LAB | Administrador autorizado, após revisão das dependências e preservação de acessos compartilhados |
| Manter a documentação | Colaborador local, sem necessidade de acesso à AWS |

Em ambientes corporativos, prefira contas-membro dedicadas para laboratórios e workloads. A conta de gerenciamento deve permanecer restrita às atividades administrativas necessárias. Não execute workloads de estudo nessa conta como prática padrão para os próximos laboratórios. A separação em contas-membro é uma recomendação futura, não um recurso criado neste LAB. SCPs não concedem permissões e **não restringem diretamente usuários nem roles da conta de gerenciamento**. O menor privilégio nessa conta depende dos controles IAM e da separação de acesso. Referências: [SCPs](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) e [boas práticas da conta de gerenciamento](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_best-practices_mgmt-acct.html).

## Diretório integrado, MFA e RBAC

O IAM Identity Center opera como instância organizacional em `sa-east-1`, com o diretório integrado como fonte de identidades. Um usuário foi configurado e associado ao grupo `AWS-SAA-Labs`. O acesso é atribuído ao grupo, reduzindo a necessidade de concessões individuais.

MFA é exigido em todos os logins. Na reprodução, o administrador deve selecionar **Every time they sign in (always-on)** e garantir que usuários sem dispositivo não consigam contornar a exigência, por meio de registro obrigatório ou bloqueio até o registro. O tipo de autenticador e o comportamento exato configurado para usuários sem MFA não foram fornecidos; precisam de conferência humana. Senhas, códigos, QR codes e material de recuperação não pertencem ao repositório. Veja [configuração de MFA](https://docs.aws.amazon.com/singlesignon/latest/userguide/mfa-getting-started.html).

## Permission Set e role provisionada

O Permission Set `SAA-Lab-Operator` define a política de acesso e a duração de uma hora para a sessão na conta AWS. Ele é um modelo gerenciado no IAM Identity Center; não é um usuário IAM nem uma credencial.

Ao atribuir o Permission Set ao grupo na conta, o IAM Identity Center provisiona uma role cujo nome começa com `AWSReservedSSO_SAA-Lab-Operator_`, seguido de sufixo gerado pelo serviço. A role recebe as permissões do Permission Set e é controlada pelo Identity Center. Alterações de política devem ser feitas no Permission Set e provisionadas nas contas atribuídas, sem editar a role diretamente. Veja [roles gerenciadas pelo serviço](https://docs.aws.amazon.com/singlesignon/latest/userguide/identity-center-and-iam-roles.html).

Se todas as atribuições desse Permission Set forem removidas de uma conta, a role correspondente pode ser excluída pelo serviço. Uma nova atribuição gera outro sufixo; referências diretas ao ARN antigo podem deixar de funcionar. Não publique ARNs reais nem trate o sufixo como constante. Referência: [ciclo de vida e referências a Permission Sets](https://docs.aws.amazon.com/singlesignon/latest/userguide/referencingpermissionsets.html).

## Política e menor privilégio

A [política validada](../iam/policies/saa-lab-operator.json) permite duas consultas de Organizations e nove operações EC2 `Describe`. Não permite criar, alterar ou excluir infraestrutura, administrar IAM/Identity Center ou consultar faturamento.

As 11 ações são preservadas integralmente como configuração aprovada do Permission Set. As permissões EC2 não implicam criação de recursos de rede nem tornam inventários de rede parte dos requisitos deste LAB de identidade e governança.

As operações EC2 presentes nessa política não oferecem autorização por ARN de recurso na tabela de autorização do serviço. Por isso exigem `Resource: "*"`. Isso abrange os recursos consultáveis pelas ações listadas, sem conceder outras ações EC2. Não generalize essa regra para todas as operações `Describe`: confira cada ação na [Service Authorization Reference do EC2](https://docs.aws.amazon.com/service-authorization/latest/reference/list_ec2.html).

As duas ações Organizations também não têm escopo de recurso nessa tabela e usam `Resource: "*"`; veja a [referência de Organizations](https://docs.aws.amazon.com/service-authorization/latest/reference/list_organizations.html). O acesso continua sujeito à avaliação das políticas aplicáveis e a negações explícitas.

A política não contém condição de região. A configuração padrão da CLI e o uso de `--region sa-east-1` direcionam as consultas, mas não são barreiras de autorização. Qualquer endurecimento futuro deve ser revisado separadamente, preservando nesta documentação o JSON já validado.

## SSO, AWS STS e duração das sessões

Na CLI, o perfil `aws-saa-labs` referencia a configuração SSO. O login autentica o usuário pelo navegador; o cliente obtém credenciais temporárias para a role atribuída. As chamadas AWS usam Access Key ID temporária, Secret Access Key temporária e Session Token fornecidos pelo fluxo federado, sem exigir chaves permanentes de usuário IAM.

Há duas durações distintas: a sessão de autenticação do IAM Identity Center e a sessão de acesso à conta AWS. O Permission Set limita a segunda a uma hora; a duração da primeira não foi informada. A CLI pode renovar credenciais enquanto a sessão SSO permitir. MFA em todos os logins não significa MFA em cada chamada API, nem encerramento de todo acesso após uma hora desde o login inicial. Veja [duração de sessão da conta](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtosessionduration.html) e [sessões de autenticação](https://docs.aws.amazon.com/singlesignon/latest/userguide/authconcept.html).

Os [diagramas de componentes e sequência](../diagrams/identity-architecture.md) representam essas relações. O histórico comprova a configuração e consultas descritas, sem evidência bruta publicada ou novos testes de autorização nesta entrega.
