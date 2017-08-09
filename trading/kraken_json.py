import json
import requests
# URL: https://api.kraken.com/0/public/Ticker

def krak(ticker):
    uri = "https://api.kraken.com/0/public/Ticker"
    blah = uri + "?pair=" + ticker
    r = requests.get(blah)
    json_data = r.text
    fj = json.loads(json_data)
    fuu = fj["result"][ticker]["c"]

    for price in fuu:
        btc = fuu[0]
        size = fuu[1]
    x = ( "last trade: %s BTC at %s " ) %(size, btc)
    return x 

print(krak('XXBTZEUR'))