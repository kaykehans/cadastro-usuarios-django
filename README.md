# Sistema de Cadastro de Usuários

Projeto web desenvolvido com Django para gerenciamento básico de usuários.

## 🚀 Funcionalidades

* Cadastro de usuários
* Listagem de usuários cadastrados
* Exclusão de usuários
* Validação de email único
* Validação de senha (mínimo de 6 caracteres)
* Interface simples utilizando Bootstrap

## 🛠️ Tecnologias utilizadas

* Python
* Django
* HTML / CSS
* Bootstrap

## 📂 Estrutura do projeto

O projeto segue a estrutura padrão do Django, com separação entre aplicação, templates e arquivos estáticos.

## ⚙️ Como executar o projeto

1. Clone o repositório ou extraia os arquivos:

git clone https://github.com/kaykehans/cadastro-usuarios-django.git
```
2. Crie um ambiente virtual:

```
python -m venv venv
```

3. Ative o ambiente virtual:

* Linux/Mac:

```
source venv/bin/activate
```

* Windows:

```
venv\Scripts\activate
```

4. Instale as dependências:

```
pip install -r requirements.txt
```

5. Execute as migrações do banco de dados:

```
python manage.py migrate
```

6. Inicie o servidor:

```
python manage.py runserver
```

7. Acesse no navegador:

```
http://127.0.0.1:8000/
```

## 📌 Observações

* O projeto utiliza banco de dados SQLite para simplicidade.
* As senhas são armazenadas de forma segura utilizando hash.
* Projeto desenvolvido com foco em aprendizado e prática de conceitos de backend com Django.

## 👨‍💻 Autor

Desenvolvido por [Kayke Hans]
