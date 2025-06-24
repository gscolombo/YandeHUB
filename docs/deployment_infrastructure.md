# Descrição da Infraestrutura de Implantação

## Propósito
Este documento descreve a infraestrutura necessária para implantação em produção do sistema YandêHUB, alinhado com a [descrição de arquitetura de software](system_architecture.md). As especificações apresentadas devem ser consideradas para uma implantação inicial, podendo sofrer alterações no futuro.

## Visão geral
A infraestrutura será implantada na AWS utilizando os seguintes componentes/ferramentas principais:

- **Instância EC2**: Hospedagem da aplicação Dockerizada.
- **Conteiners Docker**:
  - Container 1: Aplicação Django (servidor web)
  - Container 2: Banco de dados PostgreSQL
- **Docker Compose**: Orquestração de containers
- **Armazenamento EBS (*Elastic Block Store*)**: Persistência de dados

Ou seja, tanto a aplicação Django quanto o banco de dados PostgreSQL serão executadas na mesma instância AWS EC2, porém em containers separados, orquestrados utilizando o Docker Compose. A persistência dos dados no banco de dados será provida pelo volume fornecido pelo serviço EBS da AWS. Dessa forma, a aplicação irá se comunicar com o servidor de banco de dados como se este estivesse em uma máquina remota, o que provê maior segurança e escalabilidade para o sistema. O Docker Compose também deve ser utilizado para definir as configurações de rede para permitir essa comunicação.


## Especificações de *hardware*
- ### Instância AWS EC2
| Parâmetro | Especificação |
|---|---|
| Tipo de Instância | *t3.medium* |
| vCPUs | 2 |
| Memória | 4 GiB |
| Armazenamento | Volume EBS de 30 GB (SSD de uso geral) |
| Sistema Operacional | Ubuntu 24.04 LTS |


## Especificações de *software*
| Componente | Versão | Função |
|---|---|---|
| Docker Engine | 28.1+ | Tecnologia de containerização |
| Docker Compose | 2.35+ | Orquestração de containers |
| Interpretador Python | 3.11+ | Linguagem de programação da aplicação |
| Django | 5.2+ | *Framework* para aplicações web |
| PostgreSQL | 16+ | SGDBR para persistência de dados |
| Gunicorn | 23.0+ | Servidor WSGI |
| Nginx | 1.28+ | Proxy reverso (recomendado pela [documentação do Gunicorn](https://docs.gunicorn.org/en/latest/deploy.html)) |

## Outros serviços
- ### AWS S3
    O uso de um *bucket* S3 da AWS deve ser utilizado para armazenamento de mídia, as quais, por ora, constituem somente as imagens ilustrativas de feiras e produtos.
- ### Let's Encrypt
    A *Let's Encrypt* é uma CA que fornece certificados TLS gratuitos. Deverá ser utilizada para habilitar criptografar a comunicações entre cliente e servidor utilizando HTTPS.

## Visualizações de arquitetura
O diagrama abaixo apresenta a visão física da arquitetura de *software* correspondente à infraestrutura planejada.

![image](images/system_architecture_physical_vision.drawio.svg)