import requests
from bs4 import BeautifulSoup
import json
import os

url_cptm = "https://www.cptm.sp.gov.br/Pages/Home.aspx"

diretorio = 'data'
os.makedirs(diretorio, exist_ok=True)

request = requests.get(url_cptm)
soup = BeautifulSoup(request.content, 'html.parser')


linhas_classes = ['lilás', 'diamante', 'esmeralda', 'turquesa', 'coral', 'safira', 'jade']
linhas_data = []

for linha_class in linhas_classes:
    linhas = soup.find_all('div', class_='col-xs-4 col-sm-4 col-md-2 ' + linha_class)
    
    for linha in linhas:
        spans = linha.find_all('span')
        
        if len(spans) >= 2:  
            nome_linha = spans[0].text.strip() 
            status_linha = spans[1].text.strip()  
            linha_info = {
                "nome_linha": nome_linha,
                "status": status_linha
            }
            linhas_data.append(linha_info)

with open('data/cptm.json', 'w', encoding='utf-8') as f:
    json.dump(linhas_data, f, ensure_ascii=False, indent=4)

print("Dados salvos em 'linhas_cptm.json'.")
