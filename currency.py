import requests
import tkinter as tk

def exchange_rate(amount, current_rate, is_usd):
    if is_usd:
        converted_amount = amount * current_rate
    else:
        converted_amount = amount / current_rate
    return converted_amount

def update_exchange_rate():
    # Fetch the latest exchange rate from a reliable API
    response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
    data = response.json()
    current_rate = data['rates']['OMR']
    # Update the exchange rate label
    exchange_rate_label.config(text=f"Current exchange rate: 1 USD = {current_rate:.2f} OMR")
    # Update the exchange rate variable
    exchange_rate_var.set(current_rate)

def convert_currency():
    # Retrieve the user input
    is_usd = currency_var.get() == "USD"
    amount = float(amount_entry.get())
    current_rate = exchange_rate_var.get()
    # Calculate the conversion
    converted_amount = exchange_rate(amount, current_rate, is_usd)
    # Update the result label
    if is_usd:
        result_label.config(text=f"{amount:.2f} USD is equivalent to {converted_amount:.2f} OMR")
    else:
        result_label.config(text=f"{amount:.2f} OMR is equivalent to {converted_amount:.2f} USD")

# Create the main window
root = tk.Tk()
root.title("Currency Converter")

# Add a title label
title_label = tk.Label(root, text="Currency Converter", font=("Arial", 16))
title_label.pack(pady=10)

# Add a label to display the current exchange rate
exchange_rate_var = tk.DoubleVar()
exchange_rate_label = tk.Label(root, text="Current exchange rate: N/A")
exchange_rate_label.pack()

# Add a label to display the conversion result
result_label = tk.Label(root, text="Conversion result: N/A")
result_label.pack(pady=10)

# Add a label to prompt the user to input the currency they want to convert from
currency_label = tk.Label(root, text="Convert from:")
currency_label.pack()

# Add radiobuttons to allow the user to select the currency they want to convert from
currency_var = tk.StringVar(value="USD")
usd_radio = tk.Radiobutton(root, text="USD", variable=currency_var, value="USD")
omr_radio = tk.Radiobutton(root, text="OMR", variable=currency_var, value="OMR")
usd_radio.pack()
omr_radio.pack()

# Add a label to prompt the user to input the amount in the chosen currency
amount_label = tk.Label(root, text="Amount:")
amount_label.pack()

# Add an entry widget to allow the user to input the amount in the chosen currency
amount_entry = tk.Entry(root)
amount_entry.pack()

# Add a button to initiate the conversion
convert_button = tk.Button(root, text="Convert", command=convert_currency)
convert_button.pack(pady=10)

# Schedule the update_exchange_rate function to run every hour
root.after(0, update_exchange_rate)
root.after(3600000, lambda: root.after(0, update_exchange_rate))

# Start the GUI
root.mainloop()