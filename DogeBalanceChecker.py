import requests
import json
from coinmarketcap import Market
import os

os.system('cls' if os.name == 'nt' else 'clear')

addresses = ["DKkiGk6QdPh8gJgkn5FSASsfqWzRkfMwgL","DT2X7SeX8P3gzjfHjAnkUs6LYcAduEcy25", "DQ49PRJ4TqT8XLBFrtgKFySHiDSg36qhhi", "DH2GJ132hSDg7npBN9LcUJVvC6ZAz6Juvc", "D59LaXXtJy5fPCZKx56D5WVRy6uKEwW1u6", "DEq2Ymr4wD6DwNnLQSDyFg188TnMiLBn23", "DRietsQ2jQ1XZRtn2t1TLPiZLze1hp7Gnv", "DCC1oPoRmeZTvfkdV4pMDT5HM323ZTmp1u"]

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

def addressBreakDown():
	balance = []
	for i in addresses:
		get_address_info = requests.get('https://api.blockcypher.com/v1/doge/main/addrs/'+i+'/full?limit=99999')
		address_info = get_address_info.text
		j_address_info = json.loads(address_info)
		balance.append(j_address_info['balance'])
		print('address : '+str(i)+' - balance : '+str(j_address_info['balance']/100000000)+' doge')
	print('total balance : '+str(sum(balance)/100000000)+' doge')
	totalBalance = sum(balance)/100000000
	print("balance usd :", str(float(usdprice) * totalBalance))
	print("balance btc :", str(float(btcprice) * totalBalance))
	print("balance gbp :", str(float(gbpprice) * totalBalance))
	print("balance eur :", str(float(eurprice) * totalBalance))
	print("balance aud :", str(float(audprice) * totalBalance))
	print("balance cad :", str(float(cadprice) * totalBalance))

addressBreakDown()
