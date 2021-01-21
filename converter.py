import requests as reqst


def api(currency):
    response = reqst.get(f"http://api.shaycryptoco.in/price/{currency}")#requesting api to {currency} 
    json = response.json() #api-json

    json = json[currency] #checking specific currency

    text = f"The value of sccn to {currency} is {json}"  # formmating text

    return text #returning final value

#print(api('usd'))# change currency to currency of choice