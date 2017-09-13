import requests
import json
from coinmarketcap import Market
import os
import sys
from time import gmtime, strftime, sleep

os.system('cls' if os.name == 'nt' else 'clear')
helptext = """
DogeBalanceChecker 1.4

python DogeBalanceChecker [FLAG]

-[letter] : defintion : usage <default: -[LETTER]>

Help:

-b : shows balance of recorded addresses

-l : lets you lookup the balance of any address in dogecoin only : -l [ADDRESS]

-a : adds address to the list of addresses : -a [ADDRESS]

-h : display help text

-v : display the program version

-B : display balance of bitcoin addresses

-L : display balance of litecoin addresses

-d : tracks an address for future trasactions : -d [ADDRESS]
"""
version = "DogeBalanceChecker 1.1"

coinmarketcap = Market()
class doge:
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
	dogecoin = coinmarketcap.ticker("Dogecoin", limit=3, convert="LTC")[0]
	ltcprice = dogecoin["price_ltc"]

class btc:
	bitcoin = coinmarketcap.ticker("Bitcoin", limit=3, convert="USD")[0]
	usdprice = bitcoin["price_usd"]
	btcprice = bitcoin["price_btc"]
	bitcoin = coinmarketcap.ticker("Bitcoin", limit=3, convert="EUR")[0]
	eurprice = bitcoin["price_eur"]
	bitcoin = coinmarketcap.ticker("Bitcoin", limit=3, convert="GBP")[0]
	gbpprice = bitcoin["price_gbp"]
	bitcoin = coinmarketcap.ticker("Bitcoin", limit=3, convert="AUD")[0]
	audprice = bitcoin["price_aud"]
	bitcoin = coinmarketcap.ticker("Bitcoin", limit=3, convert="CAD")[0]
	cadprice = bitcoin["price_cad"]
	bitcoin = coinmarketcap.ticker("Bitcoin", limit=3, convert="DOGE")[0]
	dogeprice = bitcoin["price_doge"]

class ltc:
	litecoin = coinmarketcap.ticker("Litecoin", limit=3, convert="USD")[0]
	usdprice = litecoin["price_usd"]
	btcprice = litecoin["price_btc"]
	litecoin = coinmarketcap.ticker("Litecoin", limit=3, convert="EUR")[0]
	eurprice = litecoin["price_eur"]
	litecoin = coinmarketcap.ticker("Litecoin", limit=3, convert="GBP")[0]
	gbpprice = litecoin["price_gbp"]
	litecoin = coinmarketcap.ticker("Litecoin", limit=3, convert="AUD")[0]
	audprice = litecoin["price_aud"]
	litecoin = coinmarketcap.ticker("Litecoin", limit=3, convert="CAD")[0]
	cadprice = litecoin["price_cad"]
	litecoin = coinmarketcap.ticker("Litecoin", limit=3, convert="DOGE")[0]
	dogeprice = litecoin["price_doge"]

def verifyAddresses(currency="addresses",prefix=["D","A","9"], documented=True, address=None):
	if documented:
		addresses = importAddresses(currency)
	elif not documented:
		addresses = [address]
	
	for i in addresses:
		if not i[0] in prefix:
			raise ValueError("Invalid Address")
		elif len(i) != 34:
			raise ValueError("Invalid Address")

def dogebalance():
	addresses = importAddresses()
	verifyAddresses()
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
	print("balance usd :", str(float(doge.usdprice) * totalBalance))
	print("balance btc :", str(float(doge.btcprice) * totalBalance))
	print("balance ltc :", str(float(doge.ltcprice) * totalBalance))
	print("balance gbp :", str(float(doge.gbpprice) * totalBalance))
	print("balance eur :", str(float(doge.eurprice) * totalBalance))
	print("balance aud :", str(float(doge.audprice) * totalBalance))
	print("balance cad :", str(float(doge.cadprice) * totalBalance))
	
def btcbalance():
	addresses = importAddresses('btc')
	verifyAddresses("btc", ["1", "3"])
	os.system('cls' if os.name == 'nt' else 'clear')
	balance = []
	for i in addresses:
		get_address_info = requests.get('https://api.blockcypher.com/v1/btc/main/addrs/'+i+'/full?limit=99999')
		address_info = get_address_info.text
		j_address_info = json.loads(address_info)
		balance.append(j_address_info['balance'])
		print('address : '+str(i)+' - balance : '+str(j_address_info['balance']/100000000)+' btc')
	print('total balance : '+str(sum(balance)/100000000)+' btc')
	totalBalance = sum(balance)/100000000
	print("balance doge :", str(float(btc.dogeprice) * totalBalance))
	print("balance usd :", str(float(btc.usdprice) * totalBalance))
	print("balance btc :", str(float(btc.btcprice) * totalBalance))
	print("balance gbp :", str(float(btc.gbpprice) * totalBalance))
	print("balance eur :", str(float(btc.eurprice) * totalBalance))
	print("balance aud :", str(float(btc.audprice) * totalBalance))
	print("balance cad :", str(float(btc.cadprice) * totalBalance))
	
def ltcbalance():
	addresses = importAddresses('ltc')
	verifyAddresses("ltc", ["L"])
	os.system('cls' if os.name == 'nt' else 'clear')
	balance = []
	for i in addresses:
		get_address_info = requests.get('https://api.blockcypher.com/v1/ltc/main/addrs/'+i+'/full?limit=99999')
		address_info = get_address_info.text
		j_address_info = json.loads(address_info)
		balance.append(j_address_info['balance'])
		print('address : '+str(i)+' - balance : '+str(j_address_info['balance']/100000000)+' ltc')
	print('total balance : '+str(sum(balance)/100000000)+' ltc')
	totalBalance = sum(balance)/100000000
	print("balance doge :", str(float(ltc.dogeprice) * totalBalance))
	print("balance usd :", str(float(ltc.usdprice) * totalBalance))
	print("balance btc :", str(float(ltc.btcprice) * totalBalance))
	print("balance gbp :", str(float(ltc.gbpprice) * totalBalance))
	print("balance eur :", str(float(ltc.eurprice) * totalBalance))
	print("balance aud :", str(float(ltc.audprice) * totalBalance))
	print("balance cad :", str(float(ltc.cadprice) * totalBalance))

def lookup(address):
	loop = True
	while(loop):
		addresses = []
		addresses.append(address)
		os.system('cls' if os.name == 'nt' else 'clear')
		balance = []
		for i in addresses:
			get_address_info = requests.get('https://api.blockcypher.com/v1/'+currency+'/main/addrs/'+i+'/full?limit=99999')
			address_info = get_address_info.text
			j_address_info = json.loads(address_info)
			balance.append(j_address_info['balance'])
		print(addresses[0]+"'s balance : "+str(sum(balance)/100000000)+' doge')
		totalBalance = sum(balance)/100000000
		print("balance usd :", str(float(doge.usdprice) * totalBalance))
		print("balance btc :", str(float(doge.btcprice) * totalBalance))
		print("balance gbp :", str(float(doge.gbpprice) * totalBalance))
		print("balance eur :", str(float(doge.eurprice) * totalBalance))
		print("balance aud :", str(float(doge.audprice) * totalBalance))
		print("balance cad :", str(float(doge.cadprice) * totalBalance))
		if input("Do you want to search another address(Y/n)? ").lower() == "n":
			loop = False
			break
		address = [input("What address balance do you want to lookup? ")]

def importAddresses(currency="addresses"):
	addresses = open(currency+".txt", "r")
	x = []
	for line in addresses:
		x.append(line)
	for i in range(len(x)):
		y = x[i]
		x[i] = y[0:-1]
	addresses.close
	addresses = x
	return addresses
	
def addAddress(address, currency="addresses"):
	addresses = open(currency+".txt", "r+")
	x = importAddresses()
	for i in range(len(x)):
		addresses.write(x[i] + '\n')
	addresses.write(address)
	addresses.close
	print("Success!")
	
def detect(address):
	verifyAddresses(documented=False, address=address)
	os.system('cls' if os.name == 'nt' else 'clear')
	addresses = []
	theBalance = -1
	addresses.append(address)
	while True:
		balance = []
		time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
		for i in addresses:
			get_address_info = requests.get('https://api.blockcypher.com/v1/doge/main/addrs/'+i+'/full?limit=99999')
			address_info = get_address_info.text
			j_address_info = json.loads(address_info)
			balance.append(j_address_info['balance'])
			newBalance = int(j_address_info['balance']/100000000)
			if newBalance != theBalance:
				if theBalance == -1:
					print("["+time+"]", "Initial balance:", newBalance)
				elif newBalance > theBalance:
					print("["+time+"]", "Address has received", newBalance - theBalance, "New balance:", newBalance)
				elif newBalance < theBalance:
					print("["+time+"]", "Address has withdrawn", str(theBalance - newBalance) + "doge", "New balance:", newBalance)
			theBalance = newBalance
		sleep(60)
def main(flag):
		if flag[0] == "-h":
			print(helptext)
		elif flag[0] == "-a":
			try:
				addAddress(flag[1])
			except IndexError:
				print(helptext)
		elif flag[0] == "-l":
			try:
				lookup(flag[1])
			except IndexError:
				print(helptext)
		elif flag[0] == "-b":
			dogebalance()
		elif flag[0] == "-v":
			print(version)
		elif flag[0] == "-B":
			btcbalance()
		elif flag[0] == "-L":
			ltcbalance()
		elif flag[0] == "-d":
				detect(flag[1])
		else:
			print(helptext)
	

if __name__ == "__main__":
	main(sys.argv[1:])
