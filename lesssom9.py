import requests
from bs4 import BeautifulSoup

response = requests.get("https://bank.gov.ua/ua/markets/exchangerates")
response_text = response.text

soup = BeautifulSoup(response_text, 'lxml')
exchange_rate = None
for row in soup.find_all('tr'):
    cells = row.find_all('td')
    if cells:
        currency_code_cell = row.find('td', {'data-label': 'Код літерний'})
        if currency_code_cell and currency_code_cell.text.strip() == "USD":
            exchange_rate_cell = row.find('td', {'data-label': 'Офіційний курс'})
            exchange_rate = exchange_rate_cell.text.strip()
            break
exchange_rate = exchange_rate.replace(',', '.')

if exchange_rate:
    print(f"Exchange rate for USD: {exchange_rate}")
else:
    print(f"Exchange rate for USD not found.")

gruvnia = int(input("How many gruvnia do you have - "))
print(f"You have {int(gruvnia)/float(exchange_rate)} dollars")
