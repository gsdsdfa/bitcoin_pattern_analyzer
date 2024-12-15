import requests

def get_bitcoin_data(days=30):
    url = f'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days={days}'
    response = requests.get(url)
    data = response.json()
    return data['prices']  # Возвращает список цен