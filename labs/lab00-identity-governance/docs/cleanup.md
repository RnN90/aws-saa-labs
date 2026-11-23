# Cleanup — reversão das configurações do LAB 00

## Estado e finalidade

Não há reversão confirmada das configurações de identidade e acesso do LAB. Este documento descreve um procedimento opcional para execução humana após aprovação técnica; nenhuma etapa foi executada nesta entrega.

O escopo limita-se ao usuário, à associação ao grupo `AWS-SAA-Labs`, ao Permission Set `SAA-Lab-Operator`, à atribuição na conta de gerenciamento e à configuração SSO do perfil `aws-saa-labs`. Organizations, IAM Identity Center, diretório e MFA são configurações de governança que devem ser preservadas quando compartilhadas ou necessárias para manter acesso seguro.

## Pré-condições e dependências

Identidade necessária no Console: administrador autorizado a gerenciar os componentes de identidade e acesso envolvidos. A política operacional do LAB não autoriza essa reversão e não deve ser ampliada para realizá-la.

Antes de qualquer alteração, o responsável deve:

1. Confirmar privadamente a conta de gerenciamento e a instância do IAM Identity Center em `sa-east-1`.
2. Identificar quais componentes foram criados exclusivamente para o LAB e quais foram apenas utilizados ou configurados nele. O registro não comprova exclusividade de todos os componentes; em caso de dúvida, preservá-los.
3. Conferir membros do grupo, atribuições a contas e aplicações, usos do Permission Set e referências à role provisionada. Não remover componentes utilizados por outras pessoas ou atividades.
4. Garantir acesso administrativo independente e recuperação com MFA antes de retirar o acesso do participante. Não remover a última forma de acesso administrativo.
5. Aprovar explicitamente os alvos, a ordem e o impacto. Não há exclusão automática ou seleção em massa de alvos neste procedimento.

## Console — reversão seletiva de acesso

As etapas dependem da revisão anterior. Execute somente as que correspondam a componentes exclusivos do LAB e aprovados para remoção.

1. Em **IAM Identity Center → AWS accounts**, remova a atribuição do grupo `AWS-SAA-Labs` ao Permission Set `SAA-Lab-Operator` na conta de gerenciamento, se ela não for mais necessária. Confira outras atribuições antes de prosseguir.
2. Gerencie a role `AWSReservedSSO` pelo IAM Identity Center; não a exclua nem edite diretamente no IAM. Remover todas as atribuições do Permission Set na conta pode excluir a role pelo serviço; uma nova atribuição pode gerar outro sufixo e invalidar referências ao ARN anterior. Veja o [ciclo de vida da role](https://docs.aws.amazon.com/singlesignon/latest/userguide/referencingpermissionsets.html).
3. Em **Permission sets**, exclua `SAA-Lab-Operator` somente após confirmar que não restam atribuições ou dependências. A política versionada no repositório permanece como parte da documentação aprovada.
4. Em **Groups**, remova a associação do participante ao grupo somente se ela for exclusiva do LAB. Exclua o grupo apenas se ele não tiver outros membros, atribuições ou usos.
5. Em **Users**, exclua a identidade do participante somente se tiver sido criada exclusivamente para o LAB e não possuir outros acessos ou dependências. Preserve usuários compartilhados e seu MFA; não desative a exigência de MFA da instância para encerrar o LAB.

A exclusão de Organizations, da conta de gerenciamento, da instância do IAM Identity Center ou do diretório integrado não faz parte deste cleanup. Essas operações afetam a governança e o acesso compartilhado e exigem planejamento próprio. Mudanças globais de autenticação e MFA também não devem ser revertidas automaticamente.

## CLI local — configuração do participante

Identidade necessária: proprietário do ambiente local, após revisão de perfis e sessões utilizados por outras atividades.

O perfil `aws-saa-labs` pode ser mantido para reproduzir o LAB. Se sua remoção for aprovada, o participante deve remover somente a configuração desse perfil e uma eventual seção SSO que seja comprovadamente exclusiva dele, preservando outras configurações. Não publique o conteúdo dos arquivos locais.

Esta entrega não altera configuração, credenciais, caches ou sessões. Não há comandos de logout nem remoção automática de caches: sessões SSO podem ser compartilhadas entre perfis e a retirada de uma configuração local não comprova revogação de acesso na AWS.

## Validação posterior à reversão

Resultado esperado, quando a reversão for aprovada e realizada: somente os acessos e componentes selecionados do LAB são removidos, mantendo o acesso administrativo e os componentes compartilhados.

O administrador deve conferir no Console as atribuições, os membros e as dependências remanescentes. O participante deve conferir privadamente o estado do perfil local, caso tenha sido alterado. Registre apenas resultados efetivamente observados e sanitizados; essa validação permanece pendente e não foi executada nesta entrega.

As [validações de identidade e acesso](validation.md) não constituem auditoria financeira e não comprovam ausência de cobranças na conta.
