import json
import tkinter as tk
from tkinter import messagebox
from password_manager import PasswordManager

def add_password():
    service = service_entry.get()
    password = password_entry.get()
    if service and password:
        pm.save_password(service, password)
        messagebox.showinfo("Success", f"Password for {service} added!")
        service_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Please fill in both fields.")

def retrieve_password():
    service = service_entry.get()
    if service:
        password = pm.retrieve_password(service)
        if password:
            messagebox.showinfo("Password Found", f"Password for {service}: {password}")
        else:
            messagebox.showerror("Error", f"No password found for {service}.")
    else:
        messagebox.showerror("Error", "Please enter a service name.")

# Set up main window
pm = PasswordManager()
root = tk.Tk()
root.title("Password Manager")

# Labels and entries
tk.Label(root, text="Service:").grid(row=0, column=0, padx=10, pady=10)
service_entry = tk.Entry(root)
service_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=10)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=10)


def show_services():
    with open(pm.data_file, "r") as file:
        data = json.load(file)
        services = list(data.keys())
    if services:
        services_list = "\n".join(services)
        messagebox.showinfo("Saved Services", f"Services:\n{services_list}")
    else:
        messagebox.showinfo("Saved Services", "No services saved yet.")

# Buttons
tk.Button(root, text="Add Password", command=add_password).grid(row=2, column=0, padx=10, pady=10)
tk.Button(root, text="Retrieve Password", command=retrieve_password).grid(row=2, column=1, padx=10, pady=10)
tk.Button(root, text="Show Saved Services", command=show_services).grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()

