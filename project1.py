import pandas as pd
import requests

#For 5000 cryptocureencies
params = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}

headers = {
    'Accepts': 'application/json',
    "X-CMC_PRO_API_KEY":"f3469e33-5f77-4910-8901-4fa0a79c6825"
}
#The url from coinmarketcap api
url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

#Made the response a json file
json = requests.get(url, params=params,headers=headers).json()

#Filtered the data from the json 
coins = json['data']

#Created a new array for the coins with over $20m hard cap
newCoin = []

#Loop through the array of dictionary on the coins
for coin in coins:

    #Filter the defi tokens from the other cryptocurrencies
    if 'defi' in coin['tags']:
        name = coin['name']
        symbol = coin['symbol']
        price = coin['quote']['USD']['price']
        market_cap = coin['quote']['USD']['market_cap']

        #Made a dictionary for the defi tokens
        coinDetails = {
            "name":name,
            "symbol":symbol,
            "price":price,
            "market_cap":market_cap
        }

        #Filter the defi tokens with over $20m marketcap
        if coin['quote']['USD']['market_cap']>20000000:

            #Add each defi token details to the array
            newCoin.append(coinDetails)

#print(newCoin)
#Create a DataFrame from your newCoin
df = pd.DataFrame(newCoin)

#Create an Excel writer object
writer = pd.ExcelWriter('defi_tokens.xlsx')

#Write your DataFrame to the Excel file
df.to_excel(writer, index=False, sheet_name='Defi Tokens')

#Close the Excel file
writer.close()