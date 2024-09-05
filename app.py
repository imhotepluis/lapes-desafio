import pandas as pd
from fastapi import FastAPI, HTTPException, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates")
tab = pd.read_csv('startup_data.csv')

@app.get("/home", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/dados_empresa")
async def dados_status(request: Request):
    nome_empresa = tab['name'].to_list()
    status_empresa = tab['status'].to_list()

    return templates.TemplateResponse("dados_empresa.html", {
            "request": request,
            "dados": {
                "nome_empresa": " ".join(nome_empresa),
                "status": " ".join(status_empresa)
            }
        })
@app.get("/dados_empresa/{id}")
async def dados_empresa(request: Request, id: int):

    #Verificar se o ID é valido
    if id < 0 or id >= len(tab):
        raise HTTPException(status_code=404, detail="ID invalido")

    empresa_dados = tab[["name","founded_at","closed_at","category_code", "funding_total_usd","has_angel","has_VC","status"]]
    linha_especifica = empresa_dados.iloc[id]

    return templates.TemplateResponse("dados_empresa_id.html", {
        "request": request,
        "nome": str(linha_especifica['name']),
        "fundação": str(linha_especifica['founded_at']),
        "fechado": str(linha_especifica['closed_at']),
        "categoria": str(linha_especifica['category_code']),
        "total_capita": str(linha_especifica['funding_total_usd']),
        "invest_anjo": str(linha_especifica['has_angel']),
        "vc": str(linha_especifica['has_VC']),
        "status": str(linha_especifica['status'])
    })

@app.get('/dados_empresa/ranking/capital')
def dados_ranking_capital(request: Request):
    #Orderna os capitais de empresa (descendente)
    ranking = tab.sort_values(by='funding_total_usd', ascending=False)
    #transforma a tabela em dicionario python
    ranking_capita = ranking[['name', 'funding_total_usd']].to_dict(orient='records')

    return templates.TemplateResponse("ranking_capital.html", {"request": request, "ranking": ranking_capita})

@app.get('/dados_empresa/ranking/categoria')
def dados_ranking_categoria(request: Request):
    ranking = tab.sort_values(by='category_code', ascending=True)

    ranking_categoria = ranking[['name', 'category_code']].to_dict(orient='records')

    return templates.TemplateResponse("ranking_categoria.html", {"request": request, "ranking": ranking_categoria})




