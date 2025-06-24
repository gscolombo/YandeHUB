# Requisitos não funcionais

O presente documento lista os requisitos não funcionais do produto **YandêHUB**. Cada requisito faz parte de pelo menos uma das seguintes categorias: **desempenho**, **infraestrutura**, **segurança**, **usabilidade**, **acessibilidade** e **arquitetura**. Na listagem abaixo, o requisito será incluído na categoria na qual melhor condiz.

## Desempenho
<p style="background-color: #00000066; padding: 10px; border-radius: 5px; color: white;"><i>As ferramentas de desenvolvedor do navegador devem ser utilizadas para avaliar os requisitos abaixo.</i></p>

- Para uma velocidade de *download* de 30 Mbps e *upload* de 15 Mbps:
    - O tempo de espera pelo retorno da requisição por qualquer serviço não deve ultrapassar 5 segundos.
    - O tempo para *download* de mídias e fontes não deve ultrapassar 2 segundos.
- Para velocidades de *download* e *upload* acima de 500 Kbps, o tempo de espera para qualquer requisição não deve ultrapassar 15 segundos.
- A taxa de *frames* da interface de usuário deve ser sempre maior ou igual a 30 fps.
- Funções para processamentos de dados devem apresentar tempo de execução de até 1 segundo.

## Infraestrutura
- O produto deve ser projetado e implementado para acesso em navegadores *web*, preferencialmente Google Chrome e Mozilla Firefox, em computadores pessoais (PCs) como *notebooks* e *desktops*.
- O produto não deve ser necessariamente planejado para execução em dispositivos *mobile* (*e.g.,* tablets e celulares), porém a consideração desses dispositivos em decisões técnicas é encorajada.
- A execução do *software* deve ser realizada em contêineres (*e.g.*, Docker) para padronização do ambiente de execução (*runtime enviroment*).
- Para minimização de latência, a infraestrutura de hospedagem do *software* deve estar localizada em território brasileiro.

## Segurança
- Sessões de usuários autenticados devem ser associadas a identificadores únicos criados a partir de informações desse usuário. Esse identificador deve estar acessível somente ao usuário autenticado e ao sistema e seu uso deve estar restrito à consulta e deleção para ambos, sem qualquer possibilidade de modificação após a criação do identificador.
- A deleção do identificador de uma sessão de usuário deve implicar na finalização dessa sessão.
- Toda comunicação entre sistemas que compõem o *software* deve ser realizada utilizando protocolo HTTPS/1.1 ou HTTPS/2.
- Dados pessoais de usuários devem ser armazenados em bancos de dados de acesso restrito, autorizado somente para o *software*, mediante requisição do respectivo usuário, e para administradores do bancos de dados.
- Senhas devem ser armazenadas como *hashs* no banco de dados, utilizando o algoritmo SHA-256.
- Toda comunicação ao banco de dados deve ser realizada pelo *software*, mediante requisição do usuário possibilitada pela interface de usuário, e por administradores do banco de dados.

## Usabilidade
- Animações, transições e outros efeitos de tela devem ser minimalistas, preferencialmente restritos a *fade-in/out*, translações curtas e suavizadas e alterações de opacidade de elementos.
- Formulários devem conter instruções explícitas para o seu preenchimento e validação.
- Textos devem conter até 240 caracteres, exceto para textos com finalidade de descrever algum registro, cujo limite deve ser de 1000 caracteres. Para os dois casos, inclui-se os espaços.
- Erros durante requisições de usuário devem ser suficientemente informados ao requisitante.


## Acessibilidade
- Toda imagem deve apresentar texto alternativo para leitores de tela.

## Arquitetura
- O *design* do sistema deve facilitar a inclusão de novos serviços para o *software*.
- A arquitetura do sistema deve propiciar a escalabilidade horizontal da infraestrutura.
- A lógica de integração entre cliente e servidor deve facilitar a extensão da execução do *software* associado ao cliente para outros dispositivos.
- O acoplamento entre os serviços oferecidos pelo *software* deve ser minimizado.