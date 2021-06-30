import requests

response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

# print(response.text)

binfo = response.json() # provides python's dict object

print('Bitcoin Price as on',binfo['time']['updated'])
print()
print('1 BitCoin = $',binfo['bpi']['USD']['rate']) 