🚀 Sistema de Gestão de RH - API Django
Este projeto é uma API REST desenvolvida para gerenciar o relacionamento entre Funcionários e Cursos de capacitação em uma empresa. O sistema permite o controle completo (CRUD) de colaboradores e o histórico de treinamentos vinculados a cada um.

🛠️ Tecnologias Utilizadas
Python 3.x

Django 5.x: Framework web principal.

Django REST Framework (DRF): Para a construção da API.

MySQL: Banco de dados relacional para persistência de dados.

Postman: Utilizado para testes de requisições HTTP.

📌 Funcionalidades
[x] Cadastro de Cursos (Nome, Carga Horária).

[x] Cadastro de Funcionários (Nome, Cargo, Salário, Data de Contratação).

[x] Relacionamento Many-to-Many: Um funcionário pode realizar vários cursos e um curso pode ter vários funcionários.

[x] Interface Administrativa nativa do Django para gestão rápida.

[x] Endpoints para Integração (Listagem, Criação, Edição e Exclusão via JSON).

🗄️ Estrutura do Banco de Dados
O banco de dados biblioteca_django (nome configurado) possui as seguintes tabelas principais:

app_funcionario: Dados dos colaboradores.

app_curso: Catálogo de cursos disponíveis.

app_funcionario_cursos: Tabela intermediária de relacionamento.


