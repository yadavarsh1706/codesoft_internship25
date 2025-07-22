import tkinter as tk

def click(event):
    entry.insert(tk.END, event.widget.cget("text"))

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def clear():
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify="right")
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row, col = 1, 0
for b in buttons:
    cmd = lambda x=b: entry.insert(tk.END, x) if x not in ('C', '=') else clear() if x == 'C' else calculate()
    btn = tk.Button(root, text=b, width=5, height=2, font=("Arial", 18), command=cmd)
    btn.grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()