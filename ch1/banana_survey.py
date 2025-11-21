# banana_survey.py
"""A banana preferences survey written in python with tkinter"""

import tkinter as tk

root = tk.Tk()

# title
root.title("Banana interest survey")

# set default root window size
root.geometry("640x480+300+300")
root.resizable(False, False)

title = tk.Label(
    root, 
    text='Please take the survey',
    font=('Arial 16 bold'),
    bg='brown',
    fg='#FF0'
)

name_var = tk.StringVar(root) 
name_label = tk.Label(root, text='What is your name?')
name_inp = tk.Entry(root, textvariable=name_var)


eater_var = tk.BooleanVar(root)
eater_inp = tk.Checkbutton(
    root, 
    text='Check this box if you eat bananas',
    variable=eater_var
)

num_var = tk.IntVar(root)
num_label = tk.Label(
    root, 
    text='How many bananas do you eat per day?'
)
num_inp = tk.Spinbox(root, from_=0, to_=1000, increment=1, textvariable=num_var)

color_var = tk.StringVar(root, value='Any')
color_label = tk.Label(
    root, 
    text='What is the best color for a banana?'
)
# add choices
color_choices = (
    'Any', 'Green', 'Green-Yellow', 'Yellow', 'Brown Spotted', 'Black'
)
color_inp = tk.OptionMenu(
    root,
    color_var, 
    *color_choices)

plantain_var = tk.BooleanVar(root)
plantain_label = tk.Label(root,text='Do you eat plantains?')
plantain_frame = tk.Frame(root)
plantain_yes_inp = tk.Radiobutton(plantain_frame, text='Yes', value=True, variable=plantain_var)
plantain_no_inp = tk.Radiobutton(plantain_frame, text='No', value=False, variable=plantain_var)

banana_haiku_label = tk.Label(
    root, 
    text='Write a haiku about bananas'
)
banana_haiku_inp = tk.Text(root, height=3)

submit_btn = tk.Button(root, text='Submit Survey')

output_var = tk.StringVar(root ,value='')
output_line = tk.Label(root, text='', textvariable=output_var, anchor='w', justify='left')

title.grid(columnspan=2)

name_label.grid(row=1, column=0)

name_inp.grid(row=1, column=1)

eater_inp.grid(row=2, columnspan=2, sticky='we')

num_label.grid(row=3, sticky=tk.W)
num_inp.grid(row=3, column=1, sticky=(tk.W))

color_label.grid(row=4, columnspan=2, sticky=tk.W, pady=10)
color_inp.grid(row=5, columnspan=2, sticky=tk.W, padx=25, pady=(0,10))

plantain_yes_inp.pack(side='left', fill='x', ipadx=10, ipady=5)
plantain_no_inp.pack(side='left', fill='x', ipadx=10, ipady=5)
plantain_label.grid(row=6, columnspan=6, sticky=tk.W)
plantain_frame.grid(row=7, columnspan=2, sticky=tk.W)

banana_haiku_label.grid(row=8, sticky=tk.W)
banana_haiku_inp.grid(row=9, columnspan=2, sticky='NSEW')

submit_btn.grid(row=99, sticky=tk.W)
output_line.grid(row=100, columnspan=2, sticky='NSEW')

root.rowconfigure(100, weight=1)

def on_submit():
    """To be run when user submits form"""
    name = name_var.get()
        
    
    try:
        number = num_var.get()
    except tk.TclError:
        number = 10000

    color = color_var.get()
    eater = eater_var.get()
    plantain_eater = plantain_var.get()

    
    haiku = banana_haiku_inp.get('1.0', tk.END)

    if name == '':
        message = (f'Thanks for taking the survey!\n')
    else:
        message = (f'Thanks for taking the survey, {name}.\n')
        
    if not eater:
        message += 'Sorry you don\'t like bananas!\n'
    else:
        message += f'Enjoy your {number} {color} bananas!\n'
    if plantain_eater:
        message += 'Enjoy your plantains!'
    else:
        message += 'May you successfully avoid plantains!'
    if haiku.strip():
        message += f'\n\nYour Haiku:\n{haiku}'

    output_var.set(message) # dynamically updates widget

submit_btn.configure(command=on_submit)


root.mainloop()