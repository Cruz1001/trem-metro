# trem-metro-sp

Um site simples que exibe o status atualizado das linhas de Metrô e CPTM de São Paulo, com dados coletados diretamente dos sites oficiais.

🔗 Acesse a aplicação: [https://trem-metro.onrender.com](https://trem-metro.onrender.com)

## Objetivo

Fornecer uma forma prática e centralizada para os usuários verificarem o funcionamento das linhas do transporte metropolitano de São Paulo, contribuindo para uma melhor mobilidade no dia a dia.

---

## ⚙️ Tecnologias Utilizadas

- **Python** – Lógica principal e scripts de coleta
- **FastAPI** – Criação da API para fornecer os dados
- **BeautifulSoup** – Web scraping dos sites oficiais
- **Render** – Hospedagem gratuita da aplicação



## 🚀 Como Executar Localmente

1. Clone o repositório:

git clone https://github.com/seu-usuario/trem-metro-sp.git
cd trem-metro-sp

Instale as dependências:

pip install -r requirements.txt
Execute o projeto:

uvicorn main:app --reload
Acesse http://127.0.0.1:8000 no navegador.

📦 Endpoints da API
GET /status/metro – Retorna o status atualizado das linhas do Metrô

GET /status/trem – Retorna o status atualizado das linhas da CPTM

📈 Futuras Melhorias
- Envio de alertas via SMS

- Integração com Telegram/WhatsApp

- Dashboard com histórico de ocorrências

- Interface mais elaborada e responsiva

🙋‍♂️ Autor
Vinicius Silva Cruz
LinkedIn • GitHub
