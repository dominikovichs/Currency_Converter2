
from forex_python.converter import CurrencyRates
from tkinter import *

root = Tk()
root.title("Currency Converter")
root.geometry('1000x700')

frame = LabelFrame(root, borderwidth=0, highlightthickness=0)
frame.pack()
w = Label(frame, text="Currency Converter", height=3, width=15, borderwidth=0, highlightthickness=0)
w.pack()
box = Entry(frame)
box.pack()
print(box)

root.mainloop()

#Dictionary
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



rates = CurrencyRates()
currency_nums = ["USD", "JPY", "ZAR", "BRL", "GBP", "AUD", "CNY", "IDR", "INR", "THB", "EUR"]
currency_symbols = ["$", "J¥", "R", "R$", "£", "A$", "C¥", "Rp", "₹", "฿", "€"]

for v in currency_rates.values():
    print(v)

def currency_amount():
    currency_amount_input = float(input("Enter an amount in New Zealand Dollar under $10,000: "))
    if currency_amount_input > 10000:
        print("You exceeded the maximum amount, Please try again.")
        currency_amount()
    return currency_amount_input

def get_input():
    currency = input("Select a number from the list: ")
    if [k for k, v in currency_rates.items() if currency in v]:
        currency_amount_int = currency_amount()
        currency_abbrev = currency_nums[int(currency)-1]
        conversion_rate = rates.get_rate("NZD", str(currency_abbrev))
        converted_amount = currency_amount_int * conversion_rate
        print(f"The converted amount of money from NZD to {currency_abbrev} is {currency_symbols[int(currency)-1]}" + "{:,}".format(round(converted_amount, 1)))
    else:
        print("This number does not work, please try again.")
        get_input()

get_input()

