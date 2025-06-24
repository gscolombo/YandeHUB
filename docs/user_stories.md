# Requisitos funcionais

## Visualização de conteúdo em página inicial
> _**Como** usuário, **eu quero** visualizar as feiras indígenas cadastradas no sistema **para** poder descobrir e escolher quais eu desejo ou posso participar._<br>
> _**Como** usuário, **eu quero** poder filtrar a listagem de feiras **para** visualizar somente feiras que apresentam propriedades específicas._<br>
> _**Como** usuário, **eu quero** visualizar os expositores de uma feira **para** melhor avaliar se irei ou não participar de alguma feira._<br>
> _**Como** usuário, **eu quero** visualizar a quantidade de ingressos de uma feira **para** me organizar para participar da feira ou saber o volume de participantes esperado para o evento._<br>
> _**Como** usuário, **eu quero** visualizar os produtos de um expositor de uma feira **para** saber antecipadamente os produtos que estarão disponíveis na feira._<br>
> _**Como** usuário visitante, **eu quero** ter a opção de me autenticar no sistema **para** cadastrar, editar ou deletar feiras organizadas por mim._<br>


### Detalhamento
- #### Visitante 

    Fulano é um entusiasta de feiras que decidiu acessar o **YandêHUB** para procurar a próxima feira que irá visitar. Ao acessar a *home-page*, é apresentado para ele uma listagem de feiras, em forma de grade, ordenadas (da esquerda para direita e de cima para baixo) por proximidade da data de abertura da feira com a data atual. Feiras finalizadas são incluídas ao final da listagem. Uma barra de navegação na parte superior do site apresenta a logo do **YandêHUB** e um botão para autenticação no sistema. Clicar no botão leva à página de autenticação do usuário. \
    Em cada item da listagem, é apresentado o nome da feira, a data de início e término, uma imagem representativa da feira, um breve resumo descritivo e um botão para visualizar mais detalhes sobre a feira. Na parte superior da listagem, há campos para filtrar feiras: um de texto para nome, dois de data de início e término e duas listas de opções para cidade e estado. Ao definir qualquer filtro, a listagem é atualizada para apresentar somente as feiras que satisfazem o filtro.
    Ao clicar no botão para visualizar detalhes em algum item da listagem, é aberto um *modal* contendo mais informações sobre a respectiva feira: nome, data de início, data de término, local, cidade, estado e número de ingressos disponíveis. \
    Também são apresentados os nomes dos expositores cadastrados na feira, com um botão para visualizar os produtos oferecidos pelo expositor. Ao clicar no botão, o *modal* é alterado para apresentar uma listagem dos produtos do expositor, junto ao nome, descrição e contato do expositor e um botão para voltar para a listagem de expositores. Cada item da listagem de produtos apresenta o nome e preço do produto, junto a uma imagem ilustrativa. Ao sobrepor o cursor sobre o produto, é apresentada uma descrição curta do produto. O *modal* apresenta uma botão para fechar a todo momento.
    A listagem de feiras apresenta até 10 feiras. Caso haja mais feiras cadastradas que satisfaçam o filtro aplicado, uma paginação é disponibilizada ao final da listagem.

- #### Usuário autenticado
    Cicrano é um organizador de feiras que utiliza o **YandêHUB** para registrar feiras. Nesse caso, ele possui cadastro no sistema. Ao acessar a *home-page*, ele é apresentado à mesma listagem de Fulano. Depois de se autenticar, a barra de navegação apresenta um botão adicional para cadastro de uma nova feira e um botão para acessar seu perfil de usuário, com visualizações dedicadas para essas funcionalidades.

## Autenticação de usuário
> _**Como** usuário visitante, **eu quero** realizar login no sistema **para** poder gerenciar as feiras que organizo._<br>
> _**Como** usuário visitante, **eu quero** me cadastrar no sistema **para** para poder começar a organizar e divulgar feiras._<br>
> _**Como** usuário visitante, **eu quero** solicitar um *link* por e-mail **para** recuperar a minha senha pelo cadastro de uma nova senha._

### Detalhamento
- #### Login
    Sicrano acessou o **YandêHUB** visando registrar uma feira. Como um usuário cadastrado, ao acessar a tela inicial, ele clicou no botão para autenticação no sistema, sendo redirecionado para uma outra página contendo uma formulário. O formulário apresenta dois campos, para *e-mail* e senha, e trẽs botões: um para realizar cadastro, um para recuperação de senha e outro para submissão do formulário. Esse último só é habilitado caso os campos de *e-mail* e senha estejam preenchidos. Ao inserir os dados e submeter o formulário, as informações são validadas e, caso positivo, Sicrano é redirecionado para a tela inicial alterada para um usuário autenticado. Caso negativo, é emitido um alerta ao usuário indicando que um usuário com as credenciais fornecidas não foi encontrado.

- #### Recuperação de senha
    Ao realizar *login* no **YandêHUB**, Sicrano percebeu que esqueceu a senha dele. No formulário de *login*, ao clicar no botão para recuperação de senha, o formulário é modificado para somente um campo para *e-mail*, com instruções informando que Sicrano irá receber um *link* para redefinição de senha no *e-mail*, um botão para submissão do formulário e um botão para voltar ao formulário de *login*. O *e-mail* recebido informa que foi enviado devido a uma solicitação de recuperação de senha, assim como um aviso para ignorar a mensagem caso Sicrano não tenha realizado essa solicitação. Ao clicar no *link*, uma página é aberta em outro guia ou janela do navegador, com um formulário contendo 2 campos para inserção da nova senha. O segundo campo deve conter a mesma entrada do primeiro, a fim de confirmar a nova senha. O formulário também possui um botão para submissão, habilitado somente se os dois campos estiverem preenchidos. Ao clicar o botão, um ícone de carregamento é apresentado enquanto o sistema processa os dados. Em caso de sucesso no processamento dos dados, o formulário é substituído por uma mensagem informando ao Sicrano que tente *login* novamente com a nova senha. Caso contrário, é apresentada uma mensagem de falha no processamento dos dados ao Sicrano, solicitando que ele tente novamente mais tarde.
    
- #### Cadastro
    Beltrano é um organizador de feiras que decidiu utilizar o **YandêHUB** para registrar feiras. Ao acessar a tela de *login* após clicar no botão para autenticação no sistema, ele clica no botão para cadastro no sistema. Com isso, o formulário é modificado com 4 campos de entrada: um para o nome, um para *e-mail* e dois para senha, com o segundo destinado para a confirmação da senha. Ao final do formulário, há um botão para submissão do formulário que efetiva o cadastro no sistema. Esse botão só é habilitado caso todos os campos estejam preenchidos. Há um botão para voltar para o formulário de *login*. Ao submeter o formulário, um ícone de carregamento é apresentado enquanto o sistema processa os dados. Em caso de sucesso, Beltrano é informado que está cadastrado no sistema e que será redirecionado à página inicial já autenticado no sistema. Após alguns segundos, Beltrano é redirecionado para a página inicial como um usuário autenticado. Em caso de falha, é apresentada uma mensagem de erro a Beltrano, solicitando que tente novamente mais tarde.

## Criação/edição/deleção de registro

> _**Como** usuário autenticado, **eu quero** visualizar as feiras que cadastrei **para** poder gerenciar as feiras que estou organizando._<br>
> _**Como** usuário autenticado, **eu quero** cadastrar uma feira **para** permitir que outros usuários tenham conhecimento do evento._<br>
> _**Como** usuário autenticado, **eu quero** emitir os ingressos para uma feira que cadastrei **para** poder distribuí-los quando eu achar necessário._<br>
>  _**Como** usuário autenticado, **eu quero** alterar os dados de uma feira cadastrada por mim **para** atualizar as informações vistas por outros usuários._<br>
>  _**Como** usuário autenticado, **eu quero** deletar uma feira cadastrada por mim **para** que ela não seja mais apresentada para outros usuários._<br>
>  _**Como** usuário autenticado, **eu quero** cadastrar os dados de um expositor de uma feira e seus produtos **para** que estejam visíveis a outros usuários._<br>
>  _**Como** usuário autenticado, **eu quero** alterar os dados de um expositor de uma feira e seus produtos **para** que estejam em conformidade com o especificado pelo expositor._<br>

### Detalhamento

- #### Visualização de feiras

    Após efetuar *login* no sistema, Sicrano acessou a página para cadastrar uma nova feira. A página apresenta para ele uma listagem das feiras que ele cadastrou, contendo: nome, a data de criação e a última data de atualização. Além disso, para cada feira, ele tem a opção de editá-la, deletá-la e visualizar mais detalhes da feira, como os expositores e seus produtos e os ingressos emitidos. A opção para cadastrar uma nova feira está disponível o tempo todo.

- #### Criação de feira

    Ao clicar na opção para criar uma nova feira, é apresentado para o Sicrano um formulário com campos para inserir os dados da feira: nome, data de início e término, local, cidade, estado, descrição, uma imagem ilustrativa, o número de ingressos e uma lista dinâmica de expositores da feira. Caso Sicrano selecione a opção para incluir um expositor na lista, é apresentado um formulário com os campos: nome, e-mail, telefone, descrição e uma lista dinâmica de produtos, da mesma forma que a lista de expositores, que permite o cadastro de produtos associados ao expositor. Sicrano também tem a opção de editar ou deletar qualquer expositor/produto da lista dinâmica.<br>
    A submissão do formulário só pode ser realizada com todos os campos preenchidos, exceto pela imagem ilustrativa, que é opcional. A lista de expositores deve ter pelo menos um item, assim como a lista de produtos desse expositor.<br>
    Caso as informações estejam válidas, ao submeter o formulário, Sicrano é redirecionado para a lista de feira contendo a nova feira cadastrada. Caso contrário, os erros de validação são apresentados a Sicrano. Caso ocorra algum problema durante o processamento dos dados, Sicrano também é informado do erro de servidor.

- #### Edição de feira
    Ao clicar na opção para editar uma feira, é apresentado para o Sicrano o mesmo formulário para inserir os dados de uma nova feira, porém com os campos pré-preenchidos. A alteração de qualquer campo para valores diferentes do original habilitam o salvamento das informações, desde que não seja um valor nulo (exceto para a imagem ilustrativa). As regras associadas às listas de expositores e produtos na criação da feira ainda se aplicam.<br>
    Quando Sicrano submete o formulário para salvar as alterações, é pedido que ele confirme as alterações, uma vez que não poderão ser desfeitas sem que uma nova edição seja realizada. Ao confirmar e caso os novos dados sejam válidos, Sicrano é redirecionado para a lista de feiras, com a data da última atualização da feira recém editada atualizada para a data atual. Caso contrário, os erros de validação são apresentados a Sicrano. Caso ocorra algum problema durante o processamento dos dados, Sicrano também é informado do erro de servidor.

- #### Deleção de feira
    Ao clicar na opção para deletar uma feira, é solicitado que Sicrano confirme a ação, que é irreversível. Caso ele confirme, após retorno da resposta do servidor, Sicrano é redirecionado para a lista de feiras sem a feira recém-deletada se o processamento da requisição tiver sido bem-sucedido. Caso ocorra algum problema, a falha do servidor é notificada para Sicrano e a operação não é efetivada.

## Edição/deleção de conta

> _**Como** usuário autenticado, **eu quero** visualizar ou editar as informações da minha conta **para** mantê-la em conformidade com os meus dados pessoais._<br>
> _**Como** usuário autenticado, **eu quero** poder deletar a minha conta **para** ter meus dados pessoais deletados do sistema._<br>

### Detalhamento

- #### Visualização de conta
    Após efetuar *login* no sistema, Sicrano acessou a página para visualizar os dados de sua conta. Na página, Sicrano confere seu nome e e-mail cadastrados. As ações de editar ou deletar a conta estão disponíveis para uso a qualquer momento.

- #### Edição de conta
    Caso Sicrano decida editar os dados da sua conta, ao escolher a ação de edição, um formulário pré-preenchido com seu nome e e-mail é apresentado a ele. Um outro formulário permite trocar a senha, com um campo para a nova senha e outro para confirmá-la, desde que a nova senha não seja igual a atual. A submissão de cada formulário só é habilitada se os respectivos campos não estiverem vazios. No caso do formulário para edição de nome e e-mail, também é necessário que o novo valor não seja igual ao anterior para pelo menos um dos campos.<br>
    Após alterar seus dados, Sicrano submete o formulário e aguarda a resposta do servidor. Em caso de sucesso, ele é redirecionado para a página de visualização dos dados da conta. Caso contrário, ele é informado do erro do servidor e de como proceder.

- #### Deleção de conta
    Quando Sicrano decide deletar sua conta, ao escolher a ação de deleção, ele recebe uma mensagem com a opção de confirmar a operação, que é irreversível. Ao confirmar e aguardar resposta do servidor, ele é informado que seus dados foram deletados e que ele será redirecionado à página inicial, caso a operação tenha sido bem-sucedida. Caso contrário, ele é avisado que não foi possível concluir a operação, com instruções para como proceder.<br>
    Após ser redirecionado à página inicial, Sicrano não é mais um usuário autenticado no sistema. Ele nota que recebeu um e-mail confirmando a deleção da sua conta.