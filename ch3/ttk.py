from tkinter import ttk
import tkinter as tk

root = tk.Tk()

root.title('Ttk Checker')
root.geometry('640x640+300+300')

message = ttk.Label(root, text='A label')
message.grid()

my_string_var = tk.StringVar()
msg_inp = ttk.Entry(root, textvariable='my_string_var', width=20)
msg_inp.grid()

my_combo_str = tk.StringVar()
mycombo = ttk.Combobox(
    root, textvariable=my_combo_str, 
    values=['this one', 'other one', 'last one']
)
mycombo.grid()

mylabelframe = ttk.Labelframe(
    root, 
    text='Button frame'
)

b1 = ttk.Button(
    mylabelframe,
    text='button 1'
)

b2 = ttk.Button(
    mylabelframe,
    text='button 2'
)

b1.pack()
b2.pack()

mylabelframe.grid()

root.mainloop()