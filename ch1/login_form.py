import tkinter as tk

# need to create Tk obj
root = tk.Tk()

# changes text at top of window
root.title('Login Form')

root.geometry('640x640+600+200')
root.resizable(False, True)

title = tk.Label(
    root, 
    text='Login Form',
    font=('Arial 16 bold'),
    bg='white',
    fg='black'
)

#username
username_var = tk.StringVar()
username_label = tk.Label(
    root,
    text='Username',
)
username_inp = tk.Entry(root, textvariable=username_var)

#email
email_var = tk.StringVar()
email_label = tk.Label(
    root,
    text='Email',
)
email_inp = tk.Entry(root, textvariable=email_var)

#password
psswd_var = tk.StringVar()
psswrd_label = tk.Label(
    root,
    text='Password',
)
psswd_inp = tk.Entry(root, textvariable=psswd_var)

#age
age_var = tk.IntVar(value=0)
age_label = tk.Label(
    root, 
    text='Input Age'
)
age_input = tk.Spinbox(root, from_=0, to_=100, increment=1, textvariable=age_var)

#newsletter
newslet_var = tk.BooleanVar()
newslet_inp = tk.Checkbutton(
    root, 
    text='Do you want to subscribe to our news letter?',
    variable=newslet_var
    )

#security question
secques_var = tk.StringVar(value='What was the name of your childhood pet?') #sec question choice
secanswr_var = tk.StringVar() #secquestion answer
secquest_choices = [
    'What was the name of your childhood pet?',
    'What is your mother\'s maiden name?',
    'What is your social security number'
]
secques_label = tk.Label(
    root,
    text='Select a security question'
)
secquest_inp = tk.OptionMenu(
    root,
    secques_var,
    *secquest_choices
)
secquest_answer = tk.Entry(
    root,
    textvariable=secanswr_var
)

login_btn = tk.Button(root, text='Login')

output_var = tk.StringVar()
output_line = tk.Label(root, text='', textvariable=output_var)

# placement on root frame
title.grid(columnspan=2, pady=10)

username_label.grid(row=1, column=0, pady=10)
username_inp.grid(row=1, column=1, pady=10)

email_label.grid(row=2, column=0, pady=10)
email_inp.grid(row=2, column=1, pady=10)

psswrd_label.grid(row=3, column=0, pady=10)
psswd_inp.grid(row=3, column=1, pady=10)

age_label.grid(row=4, column=0, pady=10)
age_input.grid(row=4, column=1, pady=10)

newslet_inp.grid(row=5, columnspan=2, pady=10)

secques_label.grid(row=6, column=0, pady=10)
secquest_inp.grid(row=6, column=1, pady=(10,0))

secquest_answer.grid(row=7, column=1, pady=(0, 10))

login_btn.grid(row=99, column=0, columnspan=2, pady=10)

output_line.grid(row=100, column=0, columnspan=2, sticky='w')


# helper func to obfuscate password in output
def obfuscate_psswd(password):
    obfs = ''
    for char in password:
        obfs += '*'
    return obfs

# callback function
def on_login():
    username = username_var.get()
    email = email_var.get()
    password = psswd_var.get()
    age = age_var.get()
    newslet = newslet_var.get()
    secques = secques_var.get()
    secanswr= secanswr_var.get()

    message = ''

    if username:
        message += f'Hello {username}\n'

    if email:
        message += f'Email: {email}\n'
    else:
        message += 'Email required!\n'

    if password:
        message += f'Password: {obfuscate_psswd(password)}\n'
    else:
        message += 'Paswword required!\n'

    if age:
        message += f'Age: {age}\n'
    
    if newslet:
        message += f'Thank you for signing up!\n'
    
    if secanswr:
        message += f'Secret for \"{secques}\" is safe with me.'

    output_var.set(message)

login_btn.configure(command=on_login)


# similar to while loop
root.mainloop()