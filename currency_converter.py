with open("Harry_Practice_Problems_Playlist\currency_rates.txt", "r") as f:
    lines = f.read().splitlines()

currecyDict = {}
for line in lines:
    temp = line.split('\t')
    # print(temp)
    currecyDict[temp[0]] = float(temp[1])
print(currecyDict.keys())
try:
    currency = input("Enter currency from above: ")
    curr_value = currecyDict.get(currency) #currencyDict.get() return None if the Key is not present in the Dictionary, it does not return an error
    amount = float(input("Enter amount: "))
    converted = amount*curr_value #so, here an error will ne raised "unsupported operator * , because the type(curr_value) will be None". This error will be handled by except block saying that "Please enter valid currency or check the spelling"
    print(converted)
except:
    print("Please enter valid currency or check the spelling")
    # print(e)
finally:
    print("Thank You for using Currency Converter!")