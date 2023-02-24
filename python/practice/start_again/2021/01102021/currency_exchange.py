#Exchange currency

import urllib.request
import json
import requests
#Method-1 ( Didn't work )
'''
def currency_exchange(a): 
    result = 0 
    curr_page = urllib.request.urlopen('http://openexchangerates.org/api/latest.json?app_id=9f0710764c064370932f4f2496968c62')
    obj = curr_page.read().decode(encoding ='UTF-8')
    content = json.loads(obj)
    try:
        _from = content['rates'][con_from]
        _to = content['rates'][con_to]
        convert_amt = _to/_from
        result = convert_amt * a
    except:
        raise NameError
    print (result)
'''
#method-2 ( Using request) - https://medium.com/@soumyabrataroy/creating-currency-converter-python-6a15b4e69fbb

def currency_exchange():
    old_or_latest = input("Do you want historical data ? \n if latest, please enter 'latest' or enter in this format '%Y-%m-%d' format:\t ")
    base_url = 'https://api.exchangeratesapi.io/'+old_or_latest
    response = requests.get(base_url, params='base=INR')
    if response.status_code == 200:
        data,base_value,date = response.json().items()
        print ("Available currency : ", data[1].keys())
        desired_currency = input("Please enter the INR or other currency ")
        print (f'{desired_currency}:{data[1] [desired_currency]}| base: {base_value[1]}| date:{date[1]}')
        convert = input('Do you want to convert the '+desired_currency+' value to USD? \t yes or no: ')
        if convert == 'yes' :
            value = float(input("value\n>>>"))
            print (data[1][desired_currency])
            USD_value = value/float(data[1][desired_currency])
            #print (f'The value is : \t ${USD_value}')
            print ("The value is : %.2f" %USD_value)
        else:
            print ("\n Thank You!")
    else:
        print("\n Please give the correct Data")

def main():
    #a = float(input("Enter the amount to convert: "))
    currency_exchange()

if __name__ == "__main__":
    main()