import requests
import json
from coinmarketcap import Market
import os

loop == True

coinmarketcap = Market()
dogecoin = coinmarketcap.ticker("Dogecoin", limit=3, convert="USD")[0]
usdprice = dogecoin["price_usd"]
btcprice = dogecoin["price_btc"]
dogecoin = coinmarketcap.ticker("Dogecoin", limit=3, convert="EUR")[0]
eurprice = dogecoin["price_eur"]
dogecoin = coinmarketcap.ticker("Dogecoin", limit=3, convert="GBP")[0]
gbpprice = dogecoin["price_gbp"]
dogecoin = coinmarketcap.ticker("Dogecoin", limit=3, convert="AUD")[0]
audprice = dogecoin["price_aud"]
dogecoin = coinmarketcap.ticker("Dogecoin", limit=3, convert="CAD")[0]
cadprice = dogecoin["price_cad"]

def addressBreakDown(addresses):
	balance = []
	for i in addresses:
		get_address_info = requests.get('https://api.blockcypher.com/v1/doge/main/addrs/'+i+'/full?limit=99999')
		address_info = get_address_info.text
		j_address_info = json.loads(address_info)
		balance.append(j_address_info['balance'])
	print(addresses[0]+"'s balance : "+str(sum(balance)/100000000)+' doge')
	totalBalance = sum(balance)/100000000
	print("balance usd :", str(float(usdprice) * totalBalance))
	print("balance btc :", str(float(btcprice) * totalBalance))
	print("balance gbp :", str(float(gbpprice) * totalBalance))
	print("balance eur :", str(float(eurprice) * totalBalance))
	print("balance aud :", str(float(audprice) * totalBalance))
	print("balance cad :", str(float(cadprice) * totalBalance))

while(loop):
	os.system('cls' if os.name == 'nt' else 'clear')
	addresses = [input("What address balance do you want to lookup? ")]
	addressBreakDown(addresses)
	if input("Do you want to search another address(Y/n)? ") == "n" or "N":
		global loop = False
