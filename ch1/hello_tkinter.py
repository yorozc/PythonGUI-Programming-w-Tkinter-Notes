"""Hello World application for Tkinter"""

import tkinter as tk

root = tk.Tk()

label = tk.Label(root, text="Hello World")
btn = tk.Button(root, text="Button")

label.pack()
btn.pack()

root.mainloop()