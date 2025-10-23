# API para devs adicionar vagas que acharam interessantes 

API para devs se cadastrarem e adicionar vagas para si mesmo e outros devs.

## Requisitos

- Python 3.10+
- Pip ou Pipenv/Poetry para dependências
- Banco de dados Postgres instalado e em execução

## Instalação (local)

1. Clonar o repositório:
   - git clone https://github.com/hevertongomes256/devhunter

2. Entrar no diretório:
   - cd devhunter

3. Criar e ativar um ambiente virtual:
   - Linux/macOS: python -m venv .venv && source .venv/bin/activate
   - Windows: python -m venv .venv && .venv\Scripts\activate

4. Instalar dependências:
   - pip install -r requirements.txt

5. Variáveis de ambiente (opcional):
   - Criar um arquivo .env na raiz com, por exemplo:
     - DATABASE_URL=postgresql+psycopg://user:password@localhost:5432/vagas_DB
     - APP_ENV=local
     - APP_DEBUG=true

## Executando

- Desenvolvimento (hot-reload):
  - Na raiz do projeto executar o script python para criar tabelas: python criar_tabelas.py
  - Na raiz do projeto para iniciar a aplicação: python main.py
  - Acessar http://127.0.0.1:8000 e a documentação em http://127.0.0.1:8000/docs

## Estrutura do projeto

- app/main.py — instancia FastAPI e inclui routers
- app/api/*.py — rotas da aplicação
- app/schemas/*.py — schemas Pydantic para requests/responses
- app/models/*.py — modelos ORM (SQLAlchemy)
- app/core/*.py — conexão/sessão do banco, configurações geral do projeto
- requirements.txt ou pyproject.toml — dependências

## Banco de dados

- PostgreSQL

## Documentação da API

- Swagger UI: /docs