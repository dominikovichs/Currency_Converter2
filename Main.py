import time

# Dictionary with all conversion rates
Currency_amount = {
    "USD": 0.59,
    "JPY": 87.53,
    "ZAR": 11.19,
    "BRL": 2.88,
    "GBP": 0.48,
    "AUD": 0.92, 	
	"CNY": 4.31,	
	"IDR": 9095.04,			
    "INR": 49.12,
    "THB": 21.39, 
	"EUR": 0.56
}

# Dictionary that changes the Currencies abbreviation to the Currencies full name
currency_rates = {       
    "USD": "1.  United States Dollar",                  
    "JPY": "2.  Japanese Yen",                    
    "ZAR": "3.  South African Rand",                    
    "BRL": "4.  Brazilian Real", 
    "GBP": "5.  Great British Pound",
    "AUD": "6.  Australian Dollar",	
	"CNY": "7.  Chinese Yuan",		
	"IDR": "8.  Indonesian Rupiah",			
    "INR": "9.  Indian Rupee",
    "THB": "10. Thai Baht",
	"EUR": "11. Euro"
}

# List that uses the currency symbols from the selected countries
currency_nums = ["USD", "JPY", "ZAR", "BRL", "GBP", "AUD", "CNY", "IDR", "INR", "THB", "EUR"]
currency_symbols = ["$", "J¥", "R", "R$", "£", "A$", "C¥", "Rp", "₹", "฿", "€"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

def check_for_invalid_characters(str: str):
    chars = []
    invalid = False
    for line in str:
        chars.extend(line)
    for char in chars:
        if not char in numbers:
            if char != "$" and char != ",":
                invalid = True
    return invalid

def check_for_dollar_sign(str: str):
    # Removing any dollar signs or commas in the string and returning the new string
    s1 = str.replace("$", "")
    s2 = s1.replace(",", "")
    return int(s2)

def currency_amount():
    # Function to make sure that the amount is under $10,000
    currency_amount_input_str = input("Enter an amount from New Zealand Dollar under $10,000: ")
    if check_for_invalid_characters(currency_amount_input_str):
        print("Invalid input, try again!")
        currency_amount()
    currency_amount_input = check_for_dollar_sign(currency_amount_input_str)
    if currency_amount_input > 10000:
        print("You exceeded the maximum amount, Please try again.")
        currency_amount()
    return currency_amount_input

def get_input():
    # Function that gets a currency chosen by the User and gets the exchange rate with the forex module
    currency = input("Select a number from the list: ")
    if [k for k, v in currency_rates.items() if currency in v]:
        currency_amount_int = currency_amount()
        currency_abbrev = currency_nums[int(currency)-1]
        conversion_rate = Currency_amount[str(currency_abbrev)]
        converted_amount = currency_amount_int * conversion_rate
        print(f"The converted amount of money from NZD to {currency_abbrev} is {currency_symbols[int(currency)-1]}" + "{:,}".format(round(converted_amount, 1)))
    else:
        print("This number does not work, please try again.")
        get_input()

def end_program():
    # Gets input to end or start the program
    user_input = input("Would you like to choose another currency Y/N? ").lower()
    if user_input == "n":
        return True
    elif user_input != "y":
        print("invalid input")
        end_program()
   
while True:
    # Adds a note for Users to read
    print("Note: Conversion rates added on the 21st of September 2:30pm 2023")
    time.sleep(2)
     # Prints Dictionary into the terminal
    for v in currency_rates.values():
        print(v)

    get_input()
    if end_program():
        break
