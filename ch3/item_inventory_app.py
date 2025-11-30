# item_inventory_app.py

"""Item inventory app for tracking item's name, price, type, quantity, date added, barcode #"""

import tkinter as tk 
from tkinter import ttk
from datetime import datetime
from pathlib import Path 
import csv


variables = dict()
items_saved = 0

root = tk.Tk()
root.title('Item Inventory Management')
root.columnconfigure(0, weight=1)
root.geometry("640x640+650+200")
root.resizable(False, False) # x,y

ttk.Label(root, text='Inventory Management App', font=("TkDefaultFont", 16)).grid()

main_frame = ttk.Frame(root)
main_frame.grid(sticky=(tk.W + tk.E), padx=75, pady=25)
main_frame.columnconfigure(0, weight=1)
main_frame.rowconfigure(0, weight=2)

input_frame = ttk.Labelframe(
    main_frame, text='Inventory Management'
)
input_frame.grid(sticky=(tk.W + tk.E))
for i in range(2):
    input_frame.columnconfigure(i, weight=1)

# name entry
variables['Name'] = tk.StringVar()
ttk.Label(input_frame, text='Item Name').grid(row=0, column=0)
ttk.Entry(
    input_frame, textvariable=variables['Name']
).grid(row=1, column=0, sticky=(tk.W + tk.E), padx=10, pady=10)

# price entry
variables['Price'] = tk.DoubleVar()
ttk.Label(input_frame, text='Price').grid(row=0, column=1)
ttk.Entry(
    input_frame, textvariable=variables['Price']
).grid(row=1, column=1, sticky=(tk.W + tk.E), padx=10, pady=10)

# type entry
variables['Type'] = tk.StringVar()
type_values = ['Tech', 'Collectible', 'Clothing', 'Perishable']
ttk.Label(input_frame, text='Type').grid(row=2, column=0)
ttk.Combobox(
    input_frame, textvariable=variables['Type'], values=type_values
).grid(row=3, column=0, sticky=(tk.W + tk.E), padx=10, pady=10)

# Quantity entry
variables['Quantity'] = tk.IntVar()
ttk.Label(input_frame, text='Quantity').grid(row=2, column=1)
ttk.Spinbox(
    input_frame, textvariable=variables['Quantity'], from_=0, to=10000, increment=1
).grid(row=3, column=1, sticky=(tk.W + tk.E), padx=10, pady=10) 

# date entry 
variables['Date'] = tk.StringVar()
ttk.Label(input_frame, text='Date Added').grid(row=4, column=0)
ttk.Entry(
    input_frame, textvariable=variables['Date']
).grid(row=5, column=0, sticky=(tk.W + tk.E), padx=10, pady=10)

# barcode number
variables['Barcode'] = tk.IntVar()
ttk.Label(input_frame, text='Barcode Number').grid(row=4, column=1)
ttk.Entry(
    input_frame, textvariable=variables['Barcode']
).grid(row=5, column=1, sticky=(tk.W + tk.E), padx=10, pady=10)

output_variable = tk.StringVar()
ttk.Label(
    root, textvariable=output_variable
).grid(sticky=tk.W + tk.E, row=99, padx=75)

# submit button
buttons = tk.Frame(input_frame)
buttons.grid(sticky=tk.E + tk.W)
save_button = ttk.Button(buttons, text='Save')
save_button.pack(side=tk.RIGHT)

buttons.grid(row=6, column=1, padx=10)


def on_save():
    """called when user wants to save data"""
    datestring = datetime.today().strftime("%Y-%m-%d")
    filename = "item_inventory.csv"
    newfile = not Path(filename).exists()
    output_str = ""
    data = dict()
    for key, variable in variables.items():
        try:
            # data[key] = variable.get()
            output_str += f"{key}: {variable.get()}\n"
        except tk.TclError:
            output_variable.set(f"Error in field: {key}. Data not saved.")

    output_variable.set(output_str)

save_button.configure(command=on_save)
    

root.mainloop()