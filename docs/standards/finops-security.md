# Segurança, FinOps e retenção controlada

Antes de qualquer execução futura, o operador deve registrar em ambiente privado: conta autorizada, região, sessão temporária/federada, responsável, finalidade, `environment_id`, `run_id`, recursos esperados, estimativa regional com data, limite de gasto, janela e aprovação. Não coletar credenciais em manifestos nem registrar IDs reais na documentação pública. Exigir allowlist de conta e conferir perfil e região; a configuração da CLI não é barreira IAM.

Não assumir que AWS Free Tier garante ausência de cobrança. Gratuidade depende de elegibilidade, idade/condições da conta, ofertas vigentes e consumo acumulado. Consultar [Free Tier](https://aws.amazon.com/free/) e [preços oficiais](https://aws.amazon.com/pricing/) na data da execução. EC2, EBS, IPv4 público, transferência entre AZs, NAT, endpoints e retenção de logs merecem avaliação explícita. Nenhum serviço de custo é criado por esta fundação.

Retenção temporária deve ter prazo de expiração, consumidor conhecido, responsável por cleanup e motivo. Estender somente após nova avaliação e aprovação. Capacidade reutilizável pode ser reprovisionada; não é justificativa para manter recursos permanentemente ativos. Usar o [registro local de ambiente](../../shared/templates/environment-record.example.json), sem tratá-lo como inventário já preenchido ou bloqueio automatizado.

Antes da remoção, reconciliar recursos reais com estados privados e consumidores ativos, conferir alvos, conta/região e ownership e obter aprovação. Remover consumidores antes dos produtores e verificar remanescentes, volumes, endereços, interfaces e dependências do escopo. Estado vazio não comprova ausência de recursos órfãos ou de cobranças. Falhas exigem reconciliação; nunca apagar state para ignorar recursos ou destruir componentes compartilhados para resolver erro.

Se o orçamento não comportar o serviço, escolher demonstração, simulação, análise arquitetural ou Terraform Plan explicitamente autorizado. Documentar o que a alternativa não comprova; não classificar simulação como execução real. Não introduzir plano que consulte AWS durante uma revisão sem essa autorização.

Não versionar credenciais, segredos, Terraform States, tfvars locais, planos ou evidências brutas com identificadores. Preservar a política validada do LAB 00; não ler, modificar ou publicar políticas IAM experimentais locais. Perfil federado não concede automaticamente os privilégios do LAB seguinte. Controles novos exigem revisão proporcional ao risco, sem recomendar AdministratorAccess como atalho.
