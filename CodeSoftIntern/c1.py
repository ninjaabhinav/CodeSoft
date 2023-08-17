import tkinter as tk
from math import sqrt

def click(dem):
    current = display_var.get()
    if dem == 'C':
        current = ''
    elif dem == '=':
        try:
            current = str(eval(current))
        except Exception as e:
            current = 'Error'
    elif dem == '√':
        try:
            current = str(sqrt(eval(current)))
        except Exception as e:
            current = 'Error'
    else:
        current += dem
    display_var.set(current)

root = tk.Tk()
root.title("Simple Calculator")

display_var = tk.StringVar()
display_var.set('0')

display = tk.Entry(root, textvariable=display_var, font=('Arial', 24), bd=10, insertwidth=4, width=15, justify='right')
display.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0), ('√', 5, 1)
]

for button_text, row, col in buttons:
    tk.Button(root, text=button_text, font=('Arial', 20), width=5, height=2, command=lambda dem=button_text: click(dem)).grid(row=row, column=col)

root.mainloop()
