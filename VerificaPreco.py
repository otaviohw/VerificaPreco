import requests
from bs4 import BeautifulSoup

url = "https://www.granado.com.br/granado/perfume-granado-esplendor-75ml?queryID=882b62ce96fe32e1f0c61c34c4f5b99a&objectID=5965&indexName=prd_granado_products"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

price = soup.find('span', class_='price').text.strip()
print(f"Preço: {price}")
