# Agenda

Uma aplicação para que um usuário possa gerenciar uma lista de contatos.

This project was generated with [Angular CLI](https://github.com/angular/angular-cli) version 12.1.1.

## Pré-Requisitos

Será necessario o docker e docker-compose instalado no computador.

## Rodando ambiente com Docker

Na raiz do projeto executar o comando abaixo para subir a imagem do projeto:
'docker-compose up' 

## Criando as as migrações no banco

Execute o comando 'docker-compose exec web python manage.py migrate'


## Populando o banco de dados para os dados iniciais

Execute o comando 'docker-compose exec web python manage.py loaddata fixtures.json'
