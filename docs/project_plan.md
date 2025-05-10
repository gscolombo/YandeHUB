# ExpoHUB
## Plano de Projeto


### Introdução
O presente documento apresenta as atividades associadas ao projeto para desenvolvimento do *software* **ExpoHUB**, assim como métricas para avaliação de progresso e o cronograma tentativo dividido por iterações.

### Práticas e medidas
O processo de desenvolvimento de _software_ utilizado nesse projeto é iterativo e incremental, com etapas pré-definidas a serem seguidas em cada iteração:

- Criação de *backog*
  - As primeiras tarefas do projeto são definidas.
- Seleção de tarefas
  - Tarefas são selecionadas do *backlog* para serem cumpridas na iteração atual.
- Execução/Desenvolvimento das tarefas
  - Cada tarefa é realizada com base nas informações apresentadas no *card* da tarefa.
- Apresentação e validação de resultados
  - Os resultados obtidos pela realização da tarefa são reportados no próprio *card* da tarefa em um ou mais comentários, junto aos resultados de testes automatizados.
- Avaliação e revisão da iteração
  - Os resultados obtidos ao final da iteração são revisados e avaliados quanto a:
    - Quantidade de tarefas concluídas em relação ao total de tarefas escolhidas;
    - Tempo médio para finalização de cada tarefa;
  - Caso necessário, atualizações nos requisitos do sistema são identificadas e aplicadas. 
- Atualização do *backlog*
  - Com base na revisão da iteração, tarefas presentes no *backlog* são revisadas e, se necessário, alteradas, assim como novas tarefas podem ser adicionadas.

O modelo de ciclo de iteração abaixo apresenta a ordem de execução dessas etapas. A criação de um _backlog_ é realizada antes da primeira iteração.

![Image](images/iteration_model.drawio.svg)

O gerenciamento do projeto será realizado no [Github Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects). A organização das tarefas e seus respectivos estados na iteração atual será realizada por um quadro _kanban_, com cada tarefa atribuída a um _card_ contendo:

- Resumo
- Descrição
- Premissas (opcional)
- Requisitos (se aplicável)

O quadro *kanban* terá as seguintes colunas: *Backlog*, *Para fazer*, *Em andamento* e *Concluído*, nessa ordem. Caso haja necessidade, colunas intermediárias podem ser adicionados para satisfazer etapas específicas. 
Um modelo de _card_ de tarefa pode ser conferido abaixo. Para todo _card_, deve ser atribuído uma categoria (_label_) e uma prioridade, assim como um repositório associado. Dessa forma, todo card consiste em uma _issue_ de algum repositório. _Issues_ podem conter _sub-issues_, ou seja, subtarefas. *Cards* que não correspondem a uma *issue* de algum repositório são definidos como *drafts* (rascunhos) por padrão no Github Projects.

---
> # Modelo de _card_ de tarefa 
> *Definição da tarefa*
> ### Descrição (opcional)
> *Detalhamento sobre o trabalho a ser feito.*
> ### Premissas (opcional)
> *Premissas para execução da tarefa.*
> ### Requisitos
> *Lista de requisitos (funcionais e não funcionais) a serem cumpridos para finalização da tarefa.*

---

### Marcos e objetivos
O cronograma tentativo atual do projeto, dividido em iterações por linha, é apresentado abaixo. Cada iteração deve durar o período de uma semana. O projeto criado no Github deverá refletir as iterações definidas aqui, pela visualização de *roadmap*, e vice-versa. Portanto, o cronograma poderá sofrer alterações e incrementos no decorrer do projeto.

| Período | Atividades | Marcos |
|:----:|----|----|
| <div style="width:max-content">05/05 - 12/05</div>  | <ul><li>Definição de casos de uso</li><li>Elicitação de requisitos<ul><li>Criação de histórias de usuário</li><li>Definição de requisitos de sistema</li></ul></li> | <ul><li>Histórias de usuário para: <ul><li>Visualização de conteúdo em página inicial</li><li>Login e cadastro de usuário</li></ul></li></ul> |
| <div style="width:max-content">12/05 - 19/05</div> | <li>Definição inicial de arquitetura de *software*</li><li>Elaboração de diagrama de entidade-relacionamento</li><li>Elaboração inicial de protótipo de interface de usuário</li> | <li>Elaboração de modelo básico de arquitetura do *software*</li><li>Elaboração de diagrama de entidade-relacionamento que possibilite login/cadastro de usuário em banco de dados</li><li>*Wireframe* de tela de início (*home-page*)</li><li>*Wireframe* de tela de login</li> |
|<div style="width:max-content">19/05 - 26/05</div>| <li>Detalhamento de protótipo de interface de usuário</li><li>Desenvolvimento *front-end*</li>| <li>Protótipo de tela de início</li><li>Protótipo de tela de login</li><li>Implementação de interface de usuário para login e cadastro</li> |
