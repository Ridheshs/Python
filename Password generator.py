import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length, complexity):
    # Define character sets
    character_sets = {
        "Low": string.ascii_lowercase,
        "Medium": string.ascii_letters + string.digits,
        "High": string.ascii_letters + string.digits + string.punctuation
    }
    
    # Select the appropriate character set based on complexity
    characters = character_sets.get(complexity, string.ascii_letters + string.digits + string.punctuation)
    
    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password
def on_generate_button_click():
    try:
        # Get the length and complexity from the user input
        length = int(length_entry.get())
        complexity = complexity_var.get()
        
        if length <= 0:
            raise ValueError("Password length must be a positive integer.")
        
        # Generate the password
        password = generate_password(length, complexity)
        
        # Display the generated password
        password_var.set(password)
    
    except ValueError as e:
        messagebox.showerror("Invalid input", str(e))
# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create and place the length label and entry
length_label = tk.Label(root, text="Enter the desired length of the password:")
length_label.pack(pady=5)

length_entry = tk.Entry(root)
length_entry.pack(pady=5)

# Create and place the complexity label and dropdown
complexity_label = tk.Label(root, text="Select the complexity of the password:")
complexity_label.pack(pady=5)

complexity_var = tk.StringVar(value="Medium")
complexity_dropdown = tk.OptionMenu(root, complexity_var, "Low", "Medium", "High")
complexity_dropdown.pack(pady=5)

# Create and place the generate button
generate_button = tk.Button(root, text="Generate Password", command=on_generate_button_click)
generate_button.pack(pady=10)

# Create and place the label to display the generated password
password_var = tk.StringVar()
password_label = tk.Label(root, textvariable=password_var, font=("Helvetica", 12))
password_label.pack(pady=5)

# Run the main event loop
root.mainloop()