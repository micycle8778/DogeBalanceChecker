import requests
import json
from coinmarketcap import Market
import os
import sys

os.system('cls' if os.name == 'nt' else 'clear')
helptext = """
DogeBalanceChecker 1.1

python DogeBalanceChecker [FLAG]

Help:

-b : shows balance of recorded addresses

-l : lets you lookup the balance of any address in multiple currencies

-m : shows you the balance of recorded addresses in multiple currencies

-a : adds address to the list of addresses

-h : display help text

-v : display the program version
"""
version = "DogeBalanceChecker 1.1"

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

def balance():
	os.system('cls' if os.name == 'nt' else 'clear')
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

def lookup(address):
	loop = True
	while(loop):
		addresses = []
		addresses.append(address)
		os.system('cls' if os.name == 'nt' else 'clear')
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
		if input("Do you want to search another address(Y/n)? ").lower() == "n":
			loop = False
			break
		address = [input("What address balance do you want to lookup? ")]

def importAddresses():
	addresses = open("addresses.txt", "r")
	x = []
	for line in addresses:
		x.append(line)
	for i in range(len(x)):
		y = x[i]
		x[i] = y[0:-1]
	addresses.close
	addresses = x
	return addresses
	
def addAddress(address):
	addresses = open("addresses.txt", "r+")
	x = importAddresses()
	for i in range(len(x)):
		addresses.write(x[i] + '\n')
	addresses.write(address)
	addresses.close
	print("Success!")
		
def main(flag):
	try:
		if flag[0] == "-h":
			print(helptext)
		elif flag[0] == "-a":
			try:
				addAddress(flag[1])
			except:
				print(helptext)
				raise ValueError("Usage: -a [ADDRESS]")
		elif flag[0] == "-l":
			try:
				lookup(flag[1])
			except:
				print(helptext)
				raise ValueError("Usage: -l [ADDRESS]")
		elif flag[0] == "-b":
			balance()
		elif flag[0] == "-v":
			print(version)
		else:
			print(helptext)
	except IndexError:
		balance()
	

if __name__ == "__main__":
	addresses = importAddresses()
	main(sys.argv[1:])
