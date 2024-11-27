import requests
from bs4 import BeautifulSoup

def get_product_price(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        price_span = soup.find('span', class_='price')
        if price_span:
            return price_span.text.strip()
        else:
            return "Preço não encontrado na página."
    except requests.exceptions.RequestException as e:
        return f"Erro ao acessar a página: {e}"

url = "https://www.granado.com.br/granado/perfume-granado-esplendor-75ml?queryID=882b62ce96fe32e1f0c61c34c4f5b99a&objectID=5965&indexName=prd_granado_products"
price = get_product_price(url)
print(f"Preço do produto: {price}")