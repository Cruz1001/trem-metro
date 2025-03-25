from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi import Request
from fastapi.responses import FileResponse
from apscheduler.schedulers.background import BackgroundScheduler
from api.api import *
import subprocess
import json
from pathlib import Path

app = FastAPI()

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(atualizar, 'interval', minutes=1)
    #scheduler.add_job(coletar_dados_whats, 'interval', minutes=1)
    scheduler.start()

@app.on_event("startup")
async def on_startup():
    print("Iniciando agendador...")
    start_scheduler()
    
 

@app.get("/", response_class=HTMLResponse)
async def read_root():
   with open("frontend/index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.get("/dados/metro")
def get_dados_metro():
    with open("data/metro.json", "r", encoding="utf-8") as f:
        return json.load(f)

@app.get("/dados/trem")
def get_dados_trem():
    with open("data/cptm.json", "r", encoding="utf-8") as f:
        return json.load(f)

@app.post("/atualizar")
def atualizar_dados():
    try:
        subprocess.run(["python", "scripts/metro.py"]) 
        subprocess.run(["python", "scripts/trem.py"])
        return {"message": "Dados atualizados com sucesso"}
    except Exception as e:
        return {"error": str(e)}
