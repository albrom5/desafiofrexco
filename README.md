# Desafio Tech (Automação) | Processo Seletivo Estágio Frexco

## Instruções para instalação local

1. Clonar repositório.
```console
git clone https://github.com/albrom5/desafiofrexco.git desafiofrexco
cd desafiofrexco
```

2. Crie e ativar um ambiente virtual com Python 3.10.
```console
python -m venv venv
venv/Scripts/activate
```

4. Instalar as dependências.
```console
pip install -r requirements.txt
```

5. Definir as variáveis de ambiente.
```console
6. cp contrib/env-sample .env
```
7. Executar os testes.
```console
python manage.py test
```

8. Instalar as migrações.
```console
python manage.py migrate
```

8. Executar o servidor local.
```console
python manage.py runserver
```

## Utilização da API

###Criação de novo usuário - (http://127.0.0.1:8000/create_user/)

Dados obrigatórios: 'username' e 'birth_date'. Dado opcional: 'password' (O sistema gerará a senha automaticamente, caso o usuário não a informe.)
```console
curl -X POST -F "username=tester" -F "birth_date=2000-10-01" http://127.0.0.1:8000/create_user/
```

###Consulta de usuários cadastrados.

Formato JSON (http://127.0.0.1:8000/users_json/)

```console
curl http://127.0.0.1:8000/users_json/
```

Formato CSV (http://127.0.0.1:8000/users_csv/)

```console
curl -o users.csv http://127.0.0.1:8000/users_csv/
```

Formato XLSX (http://127.0.0.1:8000/users_xlsx/)

```console
curl -o users.xlsx http://127.0.0.1:8000/users_xlsx/
```
