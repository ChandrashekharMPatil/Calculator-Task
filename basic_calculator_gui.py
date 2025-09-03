import tkinter as tk

def click(button_text):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + button_text)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = str(eval(entry.get()))   # evaluate the expression
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")


root = tk.Tk()
root.title("Basic Calculator")


entry = tk.Entry(root, width=25, font=('Arial', 16), borderwidth=3, relief="solid")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("+", 4, 2), ("=", 4, 3),
]


for (text, row, col) in buttons:
    if text == "=":
        action = calculate
    else:
        action = lambda t=text: click(t)
    tk.Button(root, text=text, width=5, height=2, font=("Arial", 14), command=action).grid(row=row, column=col, padx=5, pady=5)

tk.Button(root, text="C", width=22, height=2, font=("Arial", 14), command=clear).grid(row=5, column=0, columnspan=4, padx=5, pady=5)


root.mainloop()
