import requests
from bs4 import BeautifulSoup
import json

# URL da página que contém o iframe
url = "https://www.metro.sp.gov.br/wp-content/themes/metrosp/direto-metro.php?embed=1"

# Fazendo a requisição HTTP para obter o conteúdo da página
response = requests.get(url)

# Verificando se a requisição foi bem-sucedida
if response.status_code == 200:
    # Usando o BeautifulSoup para parsear o HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    # Encontrando todos os elementos de linha
    linhas = soup.find_all('li', class_='linha list-group-item')

    linhas_data = []

    # Iterando sobre as linhas encontradas para extrair as informações
    for linha in linhas:
        numero = linha.find('div', class_='linha-numero').text.strip()
        nome = linha.find('div', class_='linha-nome').text.strip()
        situacao = linha.find('div', class_='linha-situacao').text.strip()
        info = linha.find('div', class_='linha-info')['title'].strip()

        linha_data = {
            'numero': numero,
            'nome': nome,
            'situacao': situacao,
            'info': info
        }

        linhas_data.append(linha_data)

    # Salvando os dados extraídos em um arquivo JSON
    with open('data/metro.json', 'w', encoding="utf-8") as f:
        print("Dados salvos em 'metro.json'.")
        json.dump(linhas_data, f, ensure_ascii=False, indent=4)

else:
    print(f"Erro ao acessar a página: {response.status_code}")
