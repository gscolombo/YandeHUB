# Visão e Escopo

### Introdução
O presente documento apresenta uma visão geral acerca do projeto de desenvolvimento do *software* **YandêHUB**. Será apresentada uma descrição geral do produto, junto às soluções que almeja fornecer aos usuários e *stakeholders*, também especificados nesse documento.

---
### Posicionamento

O projeto visa o desenvolvimento de um sistema de *software*, denominado **YandêHUB** ("Yandê" significa "Nosso" ou "Nós" em tupi-guarani), para o gerenciamento de eventos públicos de exposição de mercadorias elaboradas por indígenas. O sistema possibilitará o **registro de feiras**, **expositores**, **produtos** e **ingressos** por usuários cadastrados.<br>
O sistema busca **promover a disseminação e reconhecimento da cultura e tradição de diferentes povos indígenas** por meio de uma plataforma centralizada de acesso via *web*. A partir do registro de usuários cadastrados, feiras indígenas poderão ter sua divulgação impulsionada para todos aqueles interessados em conhecer melhor a cultura, história e tradição dos povos originários, assim como grupos indígenas dedicados à venda de mercadorias poderão se beneficiar da divugalção de seus produtos, contribuindo com a inclusão socioprodutiva desses grupos.<br>
Logo, **YandêHUB é um sistema web destinado a qualquer indivíduo que tenha interesse em feiras indígenas, seja como vendedor, consumidor ou organizador**. A facilidade provida pelo sistema para criação de ingressos também irá contribuir para a organização e definição da capacidade máxima de pessoas nessas feiras.

---
### Stakeholders

|Nome       | Descrição | Responsabilidade(s) / Papel(éis) |
|---------  |-----------|----------------- |
| Indígena | Indivíduo que se identifica como pertencente aos povos originários das regiões da América do Sul e Central antes da chegada de estrangeiros e que  preservam a cultura de seus povos. | Utilização do sistema como usuário; Orientação, autorização e validação de informações referentes à cultura e história indígena.  |
| Visitante | Indivíduo interessado em visitar feiras | Utilização do sistema como usuário não autenticado para visualização de feiras. |
|Expositor| Indivíduo ou grupo indígena com exposição cadastrada em uma feira. | Autorizar divulgação de exposição e produtos associados no sistema;
|Organizador de evento| Indivíduo ou grupo interessado na organização de feiras. | Utilização do sistema para criação de feiras como usuário autenticado; |
| Desenvolvedor | Indivíduo atuante nas etapas de execução do projeto quanto a construção, validação e manutenção do produto. | Desenvolvimento de *software* do sistema; Teste de *software* do sistema; Execução de tarefas voltadas à construção, manutenção e validação de *sofware* do sistema. |
Gerente de Projeto | Indivíduo encarregado da organização e monitoramento de processos de *software*. | Especificação e validação de requisitos do sistema; Gerenciamento de tarefas para execução de projeto de *software* do sistema; Validação de processos de *software* do sistema.
Analista | Indivíduo responsável pela compreensão da necessidade e problemas de *stakeholders* para definição de requisitos. | Identificação dos problemas/necessidades dos *stakeholders*; Definição de visão de produto; Elicitação e validação de requisitos junto aos *stakeholders*.

---

### Visão geral do produto

O *sofware* **YandêHUB** permitirá a visualização, divulgação e cadastramento de feiras indígenas pelos usuários. O cadastramento se limita ao **registro de expositores, produtos e ingressos** associados à feira. O *software* **não é destinado** ao gerenciamento da logística, definição de cronogramas/programação e controle de acesso a qualquer feira que seja cadastrada no *sofware*.<br>
De maneira geral, o *sofware* deverá permitir as seguintes operações:

- Registro, busca/listagem e visualização de:
  - Feiras;
  - Expositores de uma feira;
  - Produtos de expositores de uma feira;
- Registro e visualização de ingressos para uma feira por usuário autenticado;
- Login e cadastro de usuário;
  
Devido à necessidade de comunicação entre diferentes usuários através da Internet, **o *software* será disponibilizado como um aplicativo web**. Ou seja, o acesso será feito em navegadores como Google Chrome e Mozilla Firefox, independentemente do sistema operacional subjacente, desde que este suporte algum navegador web. A expansão do acesso para dispositos *mobile* (*i.e.*, tablet, celulares, etc.) por meio de aplicativos nativos deverá ser considerada. 
Com isso, **o uso do produto está sujeito ao acesso à Internet** pelo usuário. Parte da performance para busca e envio de dados estará dependente da qualidade da conexão à Internet do usuário, assim como da capacidade de processamento da máquina utilizada por esse usuário.<br>
Toda comunicação entre diferentes usuários do produto deverá ser realizada de forma assíncrona, sem quaisquer funcionalidades como um *chat* ou troca de mensagens em tempo real.<br>
Visando simplicidade, **espera-se que o primeiro *release* do sistema seja lançado em 2 meses**, contendo as funcionalidades descritas aqui, além de outras que possam surgir no decorrer do projeto, desde que não comprometam esse prazo.<br>
Custos associados ao produto deverão ser minimizados por meio do **uso de ferramentas *open-source* gratuitas** e concentrados na infraestrutura para execução do sistema em ambiente de produção, a fim de favorecer a performance e usabilidade do sistema.