from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import json
import requests
import os

# URL da página que contém o iframe
url = "https://www.metro.sp.gov.br/wp-content/themes/metrosp/direto-metro.php?embed=1"

# Inicializa o navegador
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Comente para depuração
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get(url)
soup = BeautifulSoup(driver.page_source, 'html.parser')

linhas = soup.find_all('li', class_='linha list-group-item')

linhas_data = []

for linha in linhas:
    numero = linha.find('div', class_='linha-numero').text.strip()
    nome = linha.find('div', class_='linha-nome').text.strip()
    situacao = linha.find('div', class_='linha-situacao').text.strip()
    info = linha.find('div', class_='linha-info')['aria-label']

    linha_data = {
        'numero': numero,
        'nome': nome,
        'situacao': situacao,
        'info': info
    }
    
    linhas_data.append(linha_data)

with open('data/metro.json', 'w', encoding="utf-8") as f:
    json.dump(linhas_data, f, ensure_ascii=False, indent=4)
driver.quit()