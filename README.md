API de Gestão de BibliotecaEste projeto é um sistema de backend desenvolvido em Django e Django REST Framework para gerenciar livros e autores, utilizando MySQL como banco de dados.
🚀 TecnologiasPython 3.xDjangoDjango REST FrameworkMySQL🛠️ Como configurar o ambienteClonar o repositório:Bashgit clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
Criar e ativar o ambiente virtual:Bashpython -m venv venv
# No Windows:

.\venv\Scripts\activate
Instalar dependências:Bashpip install django djangorestframework mysqlclient
Configurar o MySQL:Crie um banco de dados chamado biblioteca_django.Configure o USER e PASSWORD no arquivo settings.py.Rodar as migrações:Bashpython manage.py migrate
Iniciar o servidor:Bashpython manage.py runserver

🔌 Documentação da API (Endpoints)A API pode ser testada via Postman ou Insomnia.AutoresMétodoEndpointDescriçãoGET/api/autores/Lista todos os autoresPOST/api/autores/Cadastra um novo autorGET/api/autores/{id}/Detalhes de um autor específicoPUT/api/autores/{id}/Atualização total do autorDELETE/api/autores/{id}/Remove um autorLivrosMétodoEndpointDescriçãoGET/api/livros/Lista todos os livrosPOST/api/livros/Cadastra um novo livroPATCH/api/livros/{id}/Atualização parcial (ex: mudar estoque)Exemplo de JSON para criar um livro (POST):JSON{
    "titulo": "Dom Casmurro",
    "autor": 1,
    "data_publicacao": "1899-01-01",
    "isbn": "9788535914849"
}
