USD_TO_PKR = 278.50  
EUR_TO_PKR = 299.75 
SAR_TO_PKR = 74.25   

def convert_currency(amount, currency):
    currency = currency.upper()
    
    if currency == "USD":
        return amount * USD_TO_PKR
    elif currency == "EUR":
        return amount * EUR_TO_PKR
    elif currency == "SAR":
        return amount * SAR_TO_PKR
    else:
        return None  

def main():
    print("Welcome to Simple Currency Converter!This program converts USD, EUR, or SAR to PKR")
    
    amount = float(input("Enter amount to convert: "))
    currency = input("Enter currency (USD/EUR/SAR): ")
    
    result = convert_currency(amount, currency)
    
    if result is not None:
        print(f"{amount} {currency.upper()} = {result} PKR")
    else:
        print("Error! Please enter USD, EUR, or SAR only.")

main()