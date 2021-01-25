import requests as reqst


def convert(currency):
    response = reqst.get(f"http://api.shaycryptoco.in/price/{currency}")#requesting api to {currency} 
    json = response.json() #api-json

    json = json[currency] #checking specific currency

    text = f"The value of sccn to {currency} is {json}"  # formmating text

    if text == f"The value of sccn to {currency} is Invalid ticker":
        text = "Error, Please change it to the following: \"s<convert \{a currency code\}\" "

    return text #returning final value

#print(api('usd'))# change currency to currency of choice
