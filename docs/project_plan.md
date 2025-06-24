# Plano e gerenciamento de projeto

### Introdução
O presente documento apresenta as atividades associadas ao projeto para desenvolvimento do *software* **YandêHUB**, assim como métricas para avaliação de progresso e o cronograma tentativo dividido por iterações.

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
Um modelo de _card_ de tarefa pode ser conferido abaixo, em linguagem *markdown*. Para todo _card_, deve ser atribuído uma categoria (_label_) e uma prioridade, assim como um repositório associado. Dessa forma, todo card consiste em uma _issue_ de algum repositório. _Issues_ podem conter _sub-issues_, ou seja, subtarefas. *Cards* que não correspondem a uma *issue* de algum repositório são definidos como *drafts* (rascunhos) por padrão no Github Projects.

```markdown
# Título da tarefa 
*Definição da tarefa*

### Descrição (opcional)
*Detalhamento sobre o trabalho a ser feito.*

### Premissas (opcional)
*Premissas para execução da tarefa.*

### Requisitos
*Lista de requisitos (funcionais e não funcionais) a serem cumpridos para finalização da tarefa.*
```

### Cronograma
O cronograma tentativo do projeto, dividido em iterações por linha, é apresentado abaixo. Cada iteração deve durar o período de uma semana. O projeto criado no Github deverá refletir as iterações definidas aqui, pela visualização do *roadmap*, e vice-versa. Portanto, poderão haver divergências entre o cronograma apresentado abaixo e o *roadmap*.

| Período | Atividades | Entregas |
|:----:|----|----|
| <div style="width:max-content">05/05 - 12/05</div>  | <ul><li>Definição de casos de uso</li><li>Elicitação de requisitos<ul><li>Criação de histórias de usuário</li><li>Definição de requisitos de sistema</li></ul> | <ul><li>Histórias de usuário para: <ul><li>Visualização de conteúdo em página inicial</li><li>Login e cadastro de usuário</li></ul></li></ul> |
| <div style="width:max-content">13/05 - 19/05</div> | <ul><li>Definição de arquitetura de *software*</li><li>Elaboração de diagrama de entidade-relacionamento</li><li>Elaboração inicial de protótipo de interface de usuário</li></ul> | <ul><li>Modelo básico de arquitetura do *software*</li><li>Diagrama de entidade-relacionamento final</li><li>*Wireframe* de tela de início (*home-page*)</li><li>*Wireframe* de tela de login</li></ul> |
|<div style="width:max-content">20/05 - 26/05</div>| <ul><li>Detalhamento de protótipo de interface de usuário</li><li>Desenvolvimento da interface de usuário das telas de autenticação</li></ul> | <ul><li>Protótipo de tela de início</li><li>Protótipo de tela de login</li><li>Interface de usuário das telas de autenticação implementadas</li></ul> |
| <div style="width:max-content">27/05 - 02/06</div>  | <ul><li>Implementação de serviço para autenticação de usuário<ul><li>Serviço de *login*</li><li>Serviço de cadastro</li><li>Serviço de recuperação de senha</li></ul></li><li>Criação de histórias de usuário para criação, edição e deleção de registros</li><li>Criação de histórias de usuário para edição e deleção de conta</li></ul>| <ul><li>Histórias de usuário para criação e deleção de registros.</li><li>Histórias de usuário para edição e deleção de conta.</li><li>Serviço de *login*/cadastro/recuperação de senha implementado</li></ul> |
| <div style="width:max-content">02/06 - 09/06</div>  | <ul><li>Elaboração inicial de protótipo de interface de usuário para criação/edição/deleção de registro</li><li>Elaboração inicial de protótipo de interface de usuário para edição/deleção de conta</li><li>Desenvolvimento de interface de usuário da tela inicial</li></ul> | <ul><li>*Wireframe* de tela para criação/edição/deleção de registro</li><li>*Wireframe* de tela para edição/deleção de conta</li><li>Interface de usuário da tela inicial implementada</li></ul> |
|<div style="width:max-content">09/06 - 16/05</div>| <ul><li>Detalhamento de protótipo da tela para criação/edição/deleção de registro</li><li>Detalhamento de protótipo da tela para edição/deleção de conta</li><li>Especificação de infraestrutura de implantação</li></ul> | <ul><li>Protótipo de tela para criação/edição/deleção de registro</li><li>Protótipo de tela para edição/deleção de conta</li><li>Documento com descrição de infraestrutura de implantação</li></ul> |
|<div style="width:max-content">16/06 - 23/05</div>| <ul><li>Desenvolvimento de interface de usuário da tela de criação/edição/deleção de registro</li><li>Desenvolvimento de interface de usuário da tela de edição/deleção de conta</li><li>Implementação de serviço para criação/edição/deleção de registro</li><li>Implementação de serviço para edição/deleção de conta</li></ul> | <ul><li>Interface de usuário da tela de criação/edição/deleção de registro implementada</li><li>Interface de usuário da tela de edição/deleção de conta implementada</li><li>Serviço de criação/edição/deleção de registro implementado</li><li>Serviço de edição/deleção de conta implementado</li></ul> |


