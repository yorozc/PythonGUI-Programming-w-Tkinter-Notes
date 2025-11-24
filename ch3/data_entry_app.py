# data_entry_app.py
"""The ABQ Data Entry application"""

import tkinter as tk 
from tkinter import ttk
from datetime import datetime
from pathlib import Path 
import csv 

variables = dict()
records_saved = 0

root = tk.Tk()
root.title('ABQ Data Entry App')
root.columnconfigure(0, weight=1) # causes column to say centered

ttk.Label(
    root, text='ABQ Data Entry App',
    font=("TkDefaultFont", 16)
).grid() 

# data record form
# put widgets in container so main container (root) can stay centered
drf = ttk.Frame(root)
drf.grid(padx=10, sticky=(tk.E + tk.W))
drf.columnconfigure(0, weight=1)

# record info (parent to date, time and technician)
r_info = ttk.Labelframe(drf, text='Record Information')
r_info.grid(sticky=(tk.W + tk.E))
for i in range(3):
    r_info.columnconfigure(i, weight=1)

variables['Date'] = tk.StringVar()
ttk.Label(r_info, text='Date').grid(row=0, column=0)
ttk.Entry(
    r_info, textvariable=variables['Date']
).grid(row=1, column=0, sticky=(tk.W + tk.E))

variables['Time'] = tk.StringVar()
time_values = ['8:00', '12:00', '16:00', '20:00']
ttk.Label(r_info, text='Time').grid(row=0, column=1)
ttk.Combobox(
    r_info, textvariable=variables['Time'], values=time_values
).grid(row=1, column=1, sticky=(tk.W + tk.E))

variables['Technician'] = tk.StringVar()
ttk.Label(r_info, text='Technician').grid(row=0, column=2)
ttk.Entry(
    r_info, textvariable=variables['Technician']
).grid(row=1, column=2, sticky=(tk.W + tk.E))




root.mainloop()