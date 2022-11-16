# Currency Calculator 😊
with open ('currencyData.txt') as f:
    lines = f.readlines()

currencyDict = {}
for line in lines:
    parsed = line.split("\t")
    currencyDict[parsed[0]] = parsed[1]

amount = int(input("Enter The Amount : "))
print("Enter The Name Of Currency You Want To Convert This Amount ? Available Option : \n")
print([print(item) for item in currencyDict.keys()])
currency = input("Enter One Of These Value : ")
print(f"{amount} INR Is Equal To {amount *float(currencyDict[currency])} {currency}")