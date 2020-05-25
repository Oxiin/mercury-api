import requests, sys

class Mercury:

	def __init__(self):

		## The token (Key) that we will use for the consumption. 
		self.token = 'MERCURY_API_TOKEN'
		
		## Define the headers. 
		self.header = headers = {
		    'accept': "application/json",
		    'content-type': "application/json",
		    "Authorization": "Bearer {}".format(self.token)
		}

		## Setup the endpoints that we will be dealing with. 
		self.endpoint = {
			'accounts': 'https://backend.mercury.com/api/v1/accounts',
			'cards': 'https://backend.mercury.com/api/v1/account/id/cards',
			'transactions': 'https://backend.mercury.com/api/v1/account/id/transactions'
		};

		## Additional filters for select endpoints. 
		self.querystring = {}

		## Consume accounts to get account ID. 
		self.accountData = self.getAccounts()
		

	def consume( self ):

		try:
		   response = requests.request("GET", self.url, headers=self.header, params=self.querystring).json()
		except requests.ConnectionError:
			print("[-] Encountered a ConnectionError. Please try again later.")
			sys.exit()

		if ('errors' in response):
			print("[-] Encountered error with message: {}.".format(response['errors']['message']))
			sys.exit()

		return response

	## Gets all account information. 
	## Required for parsing endpoints. 
	def getAccounts( self ):

		## Update the URL to the right endpoint. 
		self.url = self.endpoint['accounts']

		return self.consume()

	def accountOverview( self ):

		balanceData = {
			'balance': float(0),
			'accounts': len(self.accountData['accounts'])
		}

		for account in self.accountData['accounts']:
			balanceData['balance'] += account['availableBalance']

		return balanceData
		


## Initialise the class.
mercury = Mercury()

## Get summary data. 
summary = mercury.accountOverview()

## Outout the account summary.
print("[+] Total Balance is ${:.2f} over {} accounts".format(summary['balance'], summary['accounts']))




