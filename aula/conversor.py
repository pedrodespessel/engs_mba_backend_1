import requests # Lib que permite fazer requisições http

response = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')


taxa_dolar = float(response.json()['USDBRL']['bid'])
valor_real = float(input("Digite o valor em reais: R$ "))

valor_dolar = valor_real / taxa_dolar
print(f"Valor em dólares (cotação a {taxa_dolar:.2f}): {valor_dolar:.2f}")