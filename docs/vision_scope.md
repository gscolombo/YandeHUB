# Visão e Escopo

### Introdução
O presente documento apresenta uma visão geral acerca do projeto de desenvolvimento do *software* ExpoHUB, junto aos escopos de projeto e produto associados. Será apresentado uma descrição geral do produto, junto às soluções que almeja fornecer aos usuários e *stakeholders*, também especificados nesse documento.

---
### Posicionamento

O projeto visa o desenvolvimento de um sistema de *software*, denominado **ExpoHUB**, para o gerenciamento de eventos públicos de exposição de mercadorias por indivíduos autonômos, ou seja, feiras. O sistema possibilitará a **criação de feiras por organizadores de eventos**, assim como o **cadastramento de expositores** e a **compra e venda de ingressos por participantes**, quando for o caso. \
Toda a gestão de divulgação de feiras, expositores e produtos, associados entre si, será mediada pelo sistema, assim como a venda de ingressos e gestão de participantes da feira. O sistema busca **facilitar a comunicação** entre organizadores de eventos, feirantes e consumidores por meio de uma plataforma centralizada de acesso via *web*. Visto que muitos feirantes podem ter seus negócios comprometidos simplesmente pela baixa divulgação de seus produtos (em geral, bastante desejados pelo custo-benefício associado), o sistema oferece uma solução simples e moderna, que aproveita a alta conectividade dos dias atuais devido a maior disponibilidade de acesso à internet.
Logo, **ExpoHUB é um sistema web destinado a qualquer indivíduo que tenha interesse em feiras, seja como vendedor, consumidor ou organizador**. A facilidade provida pelo sistema para divulgação e controle de participantes de feiras também será uma oportunidade para expandir o negócio de organizadores de eventos, gerando maior rentabilidade.

---
### Stakeholders

|Nome       | Descrição | Responsabilidade(s) |
|---------  |-----------|----------------- |
|Feirante   | Indivíduo ou grupo de atuação autonôma na venda de mercadorias em feiras | Utilização do sistema para divulgação de produtos |
|Participante|Indivíduo interessado na participação em feiras como consumidor| Utilização do sistema para visualização de produtos e compra de ingressos para participação em feiras|
|Organizador de evento| Indivíduo ou grupo interessado na organização de feiras | Utilização do sistema para criação de feiras; fornecimento de suporte a Participantes; investimento nos custos de desenvolvimento e manutenção do sistema |
| Desenvolvedor | Indivíduo atuante nas etapas de execução do projeto quanto a construção, validação e manutenção do sistema | Desenvolvimento de *software* do sistema; Teste de *software* do sistema; Execução de tarefas voltadas à construção, manutenção e validação de *sofware* do sistema |
Gerente de Projeto | Indivíduo encarregado da organização e monitoramento de processos de *software* | Especificação e validação de requisitos do sistema; Gerenciamento de tarefas para execução de projeto de *software* do sistema; Validação de processos de *software* do sistema

---

### Escopo do projeto

As atividades do projeto são apresentadas abaixo:


- #### Levantamento de requisitos
  - Definição de requisitos funcionais
    - Listagem de principais funcionalidades do sistema
    - Criação de histórias de usuários
  - Definição de requisitos não funcionais
    - Identificação das métricas mais relevantes para o sistema
  - Formalização de requisitos em documento próprio
  - Validação de requisitos
- #### Elaboração inicial da arquitetura do sistema
  - Definição geral da arquitetura
    - Tipo de arquitetura
    - Principais módulos e suas interrelações
  - Criação de modelos UML
- #### Escolha de tecnologias
  - Definição de linguagens de programação utilizadas
  - Definição de *frameworks* ou bibliotecas de código necessárias/relevantes
- #### Refinamento de arquitetura
  - Modelagem do sistema considerando tecnologias escolhidas
- #### Definição de padrões para gerenciamento de projeto
  - Criação de quadro *Kanban*
    - Definição de colunas para atribuição de estado de *cards*
  - Definição e cumprimento de modelo de *cards* para formalização e atribuição de tarefas
  - Definição de categorias (*labels*) de tarefas
- #### Criação de tarefas para o *backlog*
  - Redação de tarefas segundo o modelo definido com base nos requisitos e na arquitetura modelada
- #### Formalização de iterações
  - Estabelecimento de periodicidade de iterações
  - Definição de etapas de uma interação
    - Modelagem por diagrama de atividades
  - Definição de iterações com conjunto de tarefas do *backlog*
  - Análise de métricas para revisão e avaliação de iterações
- #### Implementação de práticas de DevOps
  - Escrita de testes automatizados
    - Testes de unidade
    - Testes de integração
  - Implementação de automações para fluxos de trabalho
    - *Pipelines* para integração de código
    - *Pipelines* para implantação (*deploy*) de *software*
- #### Definição de infraestrutura de produção
  - Avaliação de possibilidades com base na arquitetura do sistema
  - Determinação de ambiente(s) de produção para execução de produto de *software* obtido
- #### Desenvolvimento de *sofware*
  - Execução de tarefas definidas na iteração atual

De cima para baixo, a listagem define uma possível sequẽncia a ser cumprida, mas é possível que algumas atividades ocorram simultaneamente a outras ou em ordem inversa, ou ainda que algumas atividades se repitam durante a execução do projeto, como "Refinamento de arquitetura" ou "Criação de tarefas para o *backlog*". De qualquer forma, será priorizada a execução das atividades na sequẽncia descrita, na medida do possível.