# Limpeza e custos — LAB 00

## Estado histórico confirmado

- A VPC personalizada legada foi removida manualmente.
- A VPC padrão foi preservada.
- A auditoria final em `sa-east-1` encontrou zero NAT Gateways, zero Elastic IPs alocados e zero VPC Endpoints.

Não foram fornecidos IDs, dependências, sequência de exclusão ou identidade usada na remoção. A política `SAA-Lab-Operator` não permite exclusão. Nenhuma limpeza foi executada pelo agente nesta entrega e não há instruções destrutivas automatizadas neste repositório.

## Recursos e acesso que devem ser preservados

Mantenha AWS Organizations, a conta de gerenciamento, IAM Identity Center, o diretório integrado, usuário, grupo `AWS-SAA-Labs`, MFA, Permission Set e atribuição de acesso. Preserve a VPC padrão e seus componentes necessários. Eles não devem ser removidos para encerrar o LAB 00.

Não remova a atribuição de acesso ou a última forma administrativa de recuperação como parte de limpeza de networking. Não exclua a role `AWSReservedSSO` manualmente. Remover todas as atribuições de um Permission Set na conta pode causar a exclusão da role pelo serviço e alterar seu sufixo em futura recriação. Consulte o [ciclo de vida da role](https://docs.aws.amazon.com/singlesignon/latest/userguide/referencingpermissionsets.html).

Configuração e caches locais da CLI pertencem ao usuário e devem permanecer fora do Git. Esta etapa não exige alterar perfil, apagar caches, revogar sessões ou executar logout.

## Proteção para qualquer limpeza futura

Uma nova intervenção depende de autorização humana específica; a execução histórica não autoriza exclusões adicionais.

1. Confirme privadamente a conta e a região do alvo com o responsável.
2. Faça inventário de leitura e confirme propriedade, finalidade, tags e dependências. Ausência de tags não prova que um recurso pode ser excluído.
3. Verifique se a VPC é padrão e se há workloads compartilhados, interfaces de rede, endpoints, rotas ou dependências gerenciadas por outros serviços.
4. Registre o alvo e o impacto em ambiente privado; obtenha a revisão do responsável antes de qualquer exclusão.
5. Use uma identidade autorizada com as permissões específicas necessárias, sem ampliar o Permission Set operacional apenas para limpar.
6. Após uma intervenção autorizada, repita as [consultas de leitura](validation.md) e revise os custos. Sanitizar eventuais evidências antes de publicação.

Não use exclusão em massa, comandos com seleção automática de alvos ou dependências inferidas. Excluir uma VPC exige avaliar seus componentes; a documentação não presume que a remoção da VPC tenha eliminado todo recurso relacionado ou toda cobrança.

## Interpretação de custos

O resultado regional dos três tipos de recurso não equivale a uma auditoria financeira da conta. Recursos em outras regiões, outros serviços, armazenamento, tráfego e outros itens faturáveis não foram integralmente examinados. Custos de VPC Endpoints dependem do tipo; a contagem isolada também não calcula uma fatura.

Para uma revisão futura, um responsável com acesso apropriado deve examinar **Billing and Cost Management**, **Bills** e **Cost Explorer**, por serviço, região e período. Considere o intervalo entre consumo e atualização dos dados de faturamento. A política operacional não concede esse acesso. Não há Budget, alerta de custo ou auditoria financeira completa confirmado no histórico.

Não declare que a conta está totalmente livre de cobranças. Consulte [Billing and Cost Management](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-what-is.html) e a [página oficial de preços de VPC](https://aws.amazon.com/vpc/pricing/) para uma análise atual antes de novas atividades.
