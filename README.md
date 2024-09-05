API de consulta de empresas e ranking

Esse API é um dos desafio do projeto do Lapes na qual foi feito para consultar o banco de dados
de sucesso de startups e tambem fazer um ranking dessas empresas por capital e categoria.

Linguagens utilizadas:
- Python
- HTML
  
Tecnologias utilizadas:
- FastAPI (p/criação dessas funcionalidades)
- Pandas (p/tratamento dos dados)
- Pycharm (IDE)

Funcionalidades:
- Consulta do banco de dados
- Ranking de empresas por:
  - Categoria
  - Capital

Tutorial:
1. Instala o requirements.txt (lista de bibliotecas dependentes) no terminal da IDE
```bash
  $ pip freeze > requirements.txt
```

2.Depois de instalar as dependencias, digite o comando:
```bash
fastapi dev app.py
```
para rodar a API

3. Clica na url do caminho onde a API se encontra:
```
 ╭────────── FastAPI CLI - Development mode ───────────╮
 │                                                     │
 │  Serving at: http://127.0.0.1:8000                  │
 │                                                     │
 │  API docs: http://127.0.0.1:8000/docs               │
 │                                                     │
 │  Running in development mode, for production use:   │
 │                                                     │
 │  fastapi run                                        │
 │                                                     │
 ╰─────────────────────────────────────────────────────╯

INFO:     Will watch for changes in these directories: ['diretorio']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [2248755] using WatchFiles
INFO:     Started server process [2248757]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```
4. Digite na final de endereço do site "/home"
```http://127.0.0.1:8000/home```

5. Aproveita as configurações da API
