# Agenda

Uma aplicação para que um usuário possa gerenciar uma lista de contatos.

API de contatos:

Para listar todos os contatos : GET
http://localhost:8000/contatos/

Para exibir detalhes de um contato : GET
http://localhost:8000/contatos/id

  
Para alterar os dados de um contato: PUT 
http://localhost:8000/contatos/id
  
Para deletar um contato: DELETE 
http://localhost:8000/contatos/id


## Pré-Requisitos

Será necessario o docker e docker-compose instalado no computador.

## Rodando ambiente com Docker

Na raiz do projeto executar o comando abaixo para subir a imagem do projeto:
'docker-compose up' 

## Criando as as migrações no banco

Execute o comando 'docker-compose exec web python manage.py migrate'


## Populando o banco de dados para os dados iniciais

Execute o comando 'docker-compose exec web python manage.py loaddata fixtures.json'
