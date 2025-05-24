#   https://www.geeksforgeeks.org/built-in-modules-in-python/

import tkinter as tk
def button_click():
    label.config(text="hello")

root = tk.Tk()
root.title("Example")
label = tk.Label(root, text="Click the button below")
label.pack(pady = 40)
button = tk.Button(root, text="Click Me", command=button_click) 
button.pack(pady=40)  
root.mainloop() 