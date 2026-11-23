# Diagramas — identidade e acesso

Os diagramas descrevem o LAB 00 sem IDs de conta, ARNs reais, nomes pessoais ou URLs privadas. Não representam contas membro, OUs ou SCPs adicionais como implantados.

## Componentes

```mermaid
flowchart TD
    User["Participante"]
    Admin["Administrador autorizado"]
    Org["AWS Organizations: todas as funcionalidades"]
    subgraph Management["Conta de gerenciamento existente"]
        IC["IAM Identity Center: instância organizacional em sa-east-1"]
        Directory["Diretório integrado: usuário e MFA"]
        Group["Grupo AWS-SAA-Labs"]
        PS["Permission Set SAA-Lab-Operator: sessão de 1 hora"]
    end
    subgraph Assigned["Conta AWS atribuída ao grupo"]
        Role["Role provisionada AWSReservedSSO"]
        APIs["Consultas autorizadas: Organizations e EC2"]
    end
    Client["AWS CLI v2 ou Console"]
    Temp["Sessão de role com credenciais temporárias AWS STS"]
    Admin -->|"configura"| Org
    Org -->|"integração organizacional"| IC
    IC --> Directory
    Directory -->|"associação"| Group
    Group -->|"atribuição à conta"| PS
    PS -->|"provisiona permissões"| Role
    User -->|"autenticação com MFA"| IC
    User --> Client
    IC -->|"acesso federado autorizado"| Temp
    Role -->|"permissões da sessão"| Temp
    Client -->|"utiliza"| Temp
    Temp -->|"chamadas assinadas"| APIs
```

A conta atribuída é uma representação lógica do destino do acesso; não indica uma segunda conta criada. O histórico não detalha um inventário de contas membro. Administração da organização e uso da role operacional são responsabilidades distintas.

## Fluxo de autenticação e uso da CLI

```mermaid
sequenceDiagram
    actor User as Participante
    participant CLI as AWS CLI v2
    participant IC as IAM Identity Center
    participant Dir as Diretório integrado e MFA
    participant Account as Conta AWS e role provisionada
    participant API as APIs AWS
    User->>CLI: Iniciar login SSO com perfil aws-saa-labs
    CLI->>IC: Iniciar autorização no navegador
    IC->>Dir: Autenticar participante
    Dir->>User: Solicitar autenticação e MFA no login
    User->>Dir: Concluir autenticação
    Dir-->>IC: Identidade autenticada
    IC-->>CLI: Autorizar sessão SSO
    CLI->>IC: Solicitar credenciais da conta e Permission Set
    IC->>Account: Obter sessão da role atribuída
    Account-->>IC: Credenciais temporárias AWS STS
    IC-->>CLI: Entregar credenciais temporárias
    Note over CLI,Account: Sessão da conta limitada a 1 hora pelo Permission Set
    CLI->>API: Assinar consulta com credenciais temporárias
    API-->>CLI: Responder conforme permissões efetivas
    Note over CLI,IC: Sessão SSO tem duração própria e pode permitir renovação
```

O fluxo é conceitual: não descreve todas as chamadas internas do serviço. A CLI obtém as credenciais pelo IAM Identity Center; o usuário não precisa chamar `sts assume-role` manualmente nem armazenar chaves permanentes. Sessões SSO existentes podem ser reutilizadas; MFA é exigido no login, não em cada chamada API.

Veja [arquitetura](../docs/architecture.md), [implementação](../docs/implementation.md) e [validação](../docs/validation.md).
