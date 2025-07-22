import tkinter as tk
from tkinter import messagebox
from datetime import datetime

tasks = []

def add_task():
    task = entry.get()
    if task:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        full_task = f"{task} (added on {now})"
        
        tasks.append(full_task)
        update_list()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def remove_task():
    try:
        selected = listbox.curselection()[0]
        tasks.pop(selected)
        update_list()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove.")

def update_list():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

# Tkinter UI Setup
root = tk.Tk()
root.title("To-Do List with Date & Time")

entry = tk.Entry(root, width=50)
entry.pack(pady=10)

tk.Button(root, text="Add Task", width=20, command=add_task).pack(pady=5)
tk.Button(root, text="Remove Task", width=20, command=remove_task).pack(pady=5)

listbox = tk.Listbox(root, width=70, height=10)
listbox.pack(pady=10)

root.mainloop()
