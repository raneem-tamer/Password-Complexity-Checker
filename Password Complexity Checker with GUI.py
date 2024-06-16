import re
import tkinter as tk   # for creating the GUI
from tkinter import messagebox  # for displaying feedback

def check_password_strength(password):
    # Define the criteria
    min_length = 8
    upper = re.search(r'[A-Z]', password)
    lower = re.search(r'[a-z]', password)
    digit = re.search(r'[0-9]', password)
    special = re.search(r'[!@#$%^&*(),.?":{}|<>]', password)

    # Initialize feedback list
    feedback = []

    # Check each criterion
    if len(password) < min_length:
        feedback.append(f"Password should be at least {min_length} characters long.")
    if not upper:
        feedback.append("Password should include at least one uppercase letter.")
    if not lower:
        feedback.append("Password should include at least one lowercase letter.")
    if not digit:
        feedback.append("Password should include at least one number.")
    if not special:
        feedback.append("Password should include at least one special character.")

    # Assess strength
    if len(feedback) == 0:
        strength = "Strong"
        feedback.append("Your password is strong.")
    elif len(feedback) == 1:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, feedback

def on_check_password():
    password = password_entry.get()
    strength, feedback = check_password_strength(password)
    message = f"Password strength: {strength}\n" + "\n".join(feedback)
    messagebox.showinfo("Password Strength", message)

# Create the main window
root = tk.Tk()
root.title("Password Strength Checker")

# Create and place the widgets
tk.Label(root, text="Enter Password:").grid(row=0, column=0, padx=10, pady=10)
password_entry = tk.Entry(root, show="*", width=30)
password_entry.grid(row=0, column=1, padx=10, pady=10)

check_button = tk.Button(root, text="Check Strength", command=on_check_password)
check_button.grid(row=1, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
