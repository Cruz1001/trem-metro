import requests
import json
import os
from dotenv import load_dotenv


def enviar_mensagem(mensagem):
    print("enviando mensagem...")
    str(mensagem)
    print(mensagem)
    load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))
    account_sid = os.getenv('TWILIO_ACCOUNT_SID') 
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')  
    twilio_number = os.getenv('TWILIO_PHONE_NUMBER') 
    destinatario = os.getenv('DESTINATARIO_PHONE_NUMBER')  
    
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Messages.json"

    try:
        data = {
            "From": twilio_number,
            "To": destinatario,
            "Body": mensagem
        }
        response = requests.post(url, data=data, auth=(account_sid, auth_token))
        print(response.status_code, response.text)
    except Exception as e:
        print(f'Erro ao enviar mensagem: {str(e)}')

def atualizar():
    url_atualizar: str = "http://localhost:8000/atualizar"
    response = requests.post(url_atualizar)
    print(response.json())

def coletar_dados_whats():
    url_metro: str = "http://localhost:8000/dados/metro"
    url_trem: str = "http://localhost:8000/dados/trem"
    print("coletando dados...")
    response_metro = requests.get(url_metro)
    response_trem = requests.get(url_trem)
    
    dados_metro = response_metro.json()
    dados_trem = response_trem.json()

    mensagem_metro = "\n".join([f"Linha {linha['numero']} {linha['nome']}: {linha['situacao']}\n" for linha in dados_metro])
    mensagem_trem = "\n".join([f"{trem['nome_linha']}: {trem['status']}\n" for trem in dados_trem])
    mensagem = mensagem_metro + "\n\n" + mensagem_trem
    enviar_mensagem(mensagem)
