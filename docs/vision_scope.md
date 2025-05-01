# Visão e Escopo

### Introdução
O presente documento apresenta uma visão geral acerca do projeto de desenvolvimento do *software* **ExpoHUB**. Será apresentada uma descrição geral do produto, junto às soluções que almeja fornecer aos usuários e *stakeholders*, também especificados nesse documento.

---
### Posicionamento

O projeto visa o desenvolvimento de um sistema de *software*, denominado **ExpoHUB**, para o gerenciamento de eventos públicos de exposição de mercadorias por indivíduos autonômos, ou seja, feiras. O sistema possibilitará a **criação de feiras por organizadores de eventos**, assim como o **cadastramento de expositores** e a **compra e venda de ingressos por participantes**, quando for o caso. \
Toda a gestão de divulgação de feiras, expositores e produtos, associados entre si, será mediada pelo sistema, assim como a venda de ingressos e gestão de participantes da feira. O sistema busca **facilitar a comunicação** entre organizadores de eventos, feirantes e consumidores por meio de uma plataforma centralizada de acesso via *web*. Visto que muitos feirantes podem ter seus negócios comprometidos simplesmente pela baixa divulgação de seus produtos (em geral, bastante desejados pelo custo-benefício associado), o sistema oferece uma solução simples e moderna, que aproveita a alta conectividade dos dias atuais devido a maior disponibilidade de acesso à internet.
Logo, **ExpoHUB é um sistema web destinado a qualquer indivíduo que tenha interesse em feiras, seja como vendedor, consumidor ou organizador**. A facilidade provida pelo sistema para divulgação e controle de participantes de feiras também será uma oportunidade para expandir o negócio de organizadores de eventos, gerando maior rentabilidade.

---
### Stakeholders

|Nome       | Descrição | Responsabilidade(s) |
|---------  |-----------|----------------- |
|Feirante   | Indivíduo ou grupo de atuação autonôma na venda de mercadorias em feiras. | Utilização do sistema para divulgação de produtos. |
|Expositor| Indivíduo ou grupo de atuação com exposição cadastrada em uma feira. | Utilização do sistema para divulgação de produtos.
|Participante|Indivíduo de posse de ingressos para participação em feiras como consumidor. | Utilização do sistema para visualização de produtos e compra de ingressos para participação em feiras. |
|Organizador de evento| Indivíduo ou grupo interessado na organização de feiras. | Utilização do sistema para criação de feiras; fornecimento de suporte a Participantes; investimento nos custos de desenvolvimento e manutenção do sistema. |
| Desenvolvedor | Indivíduo atuante nas etapas de execução do projeto quanto a construção, validação e manutenção do produto. | Desenvolvimento de *software* do sistema; Teste de *software* do sistema; Execução de tarefas voltadas à construção, manutenção e validação de *sofware* do sistema. |
Gerente de Projeto | Indivíduo encarregado da organização e monitoramento de processos de *software*. | Especificação e validação de requisitos do sistema; Gerenciamento de tarefas para execução de projeto de *software* do sistema; Validação de processos de *software* do sistema.
Analista | Indivíduo responsável pela compreensão da necessidade e problemas de *stakeholders* para definição de requisitos. | Identificação dos problemas/necessidades dos *stakeholders*; Definição de visão de produto; Elicitação e validação de requisitos junto aos *stakeholders*.

---

### Visão geral do produto

O *sofware* **ExpoHUB** permitirá a visualização, divulgação e gerenciamento de feiras pelos usuários. O gerenciamento se limita à **compra e venda de ingressos**, **listagem de participantes** e **cadastro e divulgação de produtos por feira**. Logo, o *software* **não é destinado** ao gerenciamento da logística, definição de cronogramas/programação e controle de acesso a qualquer feira que seja cadastrada no *sofware*.<br>
De maneira geral, o *sofware* deverá permitir as seguintes operações:

- Cadastro, busca/listagem e visualização de:
  - Feiras;
  - Expositores;
  - Produtos;
  - Expositores em uma feira;
  - Produtos em uma feira;
  - Produtos de um expositor em uma feira;
- Compra e venda de ingressos para participação em feira;
- Listagem de participantes de uma feira;
- Cadastro de usuário de tipo definido (Participante, Expositor ou Organizador);
  
Devido à necessidade de comunicação entre diferentes usuários através da Internet, **o *software* será disponibilizado como um aplicativo web**. Ou seja, o acesso será feito em navegadores como Google Chrome e Mozilla Firefox, independentemente do sistema operacional subjacente, desde que este suporte algum navegador web. A expansão do acesso para dispositos *mobile* por meio de aplicativos nativos deverá ser considerada. 
Com isso, **o uso do produto está sujeito ao acesso à Internet** pelo usuário. Parte da performance para busca e envio de dados estará dependente da qualidade da conexão à Internet do usuário. De qualquer forma, espera-se que o *software* garanta que o tempo de resposta a requisições do usuário não ultrapasse 30 segundos e que dure, em média, 5 segundos. 
Toda comunicação entre diferentes usuários do produto será realizada de forma assíncrona, sem quaisquer funcionalidades como um *chat* ou troca de mensagens em tempo real. Os pagamentos eletrônicos associados à compra de ingressos deverá ser mediada por uma empresa especializada que provê esses serviços, como a PayPal ou o PagSeguro.
O uso do *software* não estará restrito para usuários cadastrados, porém algumas funcionalidades deverão ser restritas a usuários cadastrados, como a compra de ingressos, o cadastro de feiras/produtos e a visualização dos participantes em uma feira. 