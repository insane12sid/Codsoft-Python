import random
import string
import tkinter as tk
from tkinter import ttk

def generatePswrd(length, use_uppercase, use_lowercase, use_digits, use_special):
    characters=""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        return "Please select at least one option for the password."

    password = "".join(random.choices(characters, k=length))
    return password

def displayPswrd(l_entry, upper_var, lower_var, digits_var, special_var, password_display):
    try:
        length = int(l_entry.get())
        if length <= 0:
            raise ValueError("Length must be a positive integer.")

        use_uppercase = upper_var.get()
        use_lowercase = lower_var.get()
        use_digits = digits_var.get()
        use_special = special_var.get()

        password = generatePswrd(length, use_uppercase, use_lowercase, use_digits, use_special)
        password_display.config(text=f"Generated Password: {password}")
    except ValueError as e:
        password_display.config(text=str(e))

def create_gui():
    #create main window
    window = tk.Tk()
    window.title("Password Generator")
    window.geometry("450x250")
    
    #apply style
    style = ttk.Style()
    style.theme_use("clam")

    #create widgets
    label = ttk.Label(window, text="Enter Password Length:")
    label.pack(pady=10)

    l_entry = ttk.Entry(window)
    l_entry.pack()

    options_frame = ttk.Frame(window)
    options_frame.pack(pady=10)

    upper_var = tk.BooleanVar()
    upper_checkbox = ttk.Checkbutton(options_frame, text="Uppercase", variable=upper_var)
    upper_checkbox.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    lower_var = tk.BooleanVar()
    lower_checkbox = ttk.Checkbutton(options_frame, text="Lowercase", variable=lower_var)
    lower_checkbox.grid(row=0, column=1, padx=10, pady=10, sticky="w")

    digits_var = tk.BooleanVar()
    digits_checkbox = ttk.Checkbutton(options_frame, text="Digits", variable=digits_var)
    digits_checkbox.grid(row=1, column=0, padx=10, pady=10, sticky="w")

    special_var = tk.BooleanVar()
    special_checkbox = ttk.Checkbutton(options_frame, text="Special Characters", variable=special_var)
    special_checkbox.grid(row=1, column=1, padx=10, pady=10, sticky="w")

    password_display = ttk.Label(window, text="")
    password_display.pack()

    gnrt_button = ttk.Button(window, text="Generate Password", command=lambda: displayPswrd(l_entry, upper_var, lower_var, digits_var, special_var, password_display))
    gnrt_button.pack(pady=10)

    window.mainloop()

if __name__ == "__main__":
    create_gui()
