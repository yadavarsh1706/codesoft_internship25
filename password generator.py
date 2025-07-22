import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showwarning("Too Short", "Password length must be at least 4 characters.")
            return

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))

        password_var.set(password)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

def copy_to_clipboard():
    password = password_var.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("No Password", "Generate a password first!")

# Initialize the GUI window
root = tk.Tk()
root.title("🔐 Password Generator")
root.geometry("400x250")
root.config(bg="#f0f0f0")

# Title
tk.Label(root, text="Password Generator", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=10)

# Input for length
tk.Label(root, text="Enter password length:", font=("Arial", 12), bg="#f0f0f0").pack()
length_entry = tk.Entry(root, font=("Arial", 12), justify='center')
length_entry.pack(pady=5)

# Generate Button
tk.Button(root, text="Generate Password", font=("Arial", 12), bg="#4CAF50", fg="white",
          command=generate_password).pack(pady=10)

# Output field
password_var = tk.StringVar()
password_entry = tk.Entry(root, textvariable=password_var, font=("Arial", 12), justify='center', state="readonly")
password_entry.pack(pady=5)

# Copy button
tk.Button(root, text="Copy to Clipboard", font=("Arial", 12), bg="#2196F3", fg="white",
          command=copy_to_clipboard).pack(pady=10)

root.mainloop()
