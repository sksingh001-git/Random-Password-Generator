import tkinter as tk
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())  # get length from entry box
        if length <= 0:
            password_var.set("Length must be > 0")
            return
    except ValueError:
        password_var.set("Enter a valid number")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    password_var.set(password)

def copy_password():
    window.clipboard_clear()                # clear clipboard
    window.clipboard_append(password_var.get())  # copy password
    window.update()                         # keep it in clipboard even after app closes
    
# Main window
window = tk.Tk()
window.title("Random Password Generator")
window.geometry("600x400+700+300")
window.resizable(False, False)

#length of the pass
tk.Label(window, text="Enter password length:").pack(pady=5)
length_entry = tk.Entry(window)
length_entry.pack(pady=5)
length_entry.insert(0, "12")  # default length

# Generate button
generate_btn = tk.Button(window, text="Generate", command=generate_password)
generate_btn.pack(pady=5)

# Password display
password_var = tk.StringVar()
password_label = tk.Label(window, textvariable=password_var, font=("Arial", 12), fg="blue")
password_label.pack(pady=10)

# Copy button
copy_btn = tk.Button(window, text="Copy Password", command=copy_password)
copy_btn.pack(pady=5)

# Quit button
quit_btn = tk.Button(window, text="Quit", command=window.destroy)
quit_btn.pack(side="bottom", pady=10)
quit_btn.focus_set()  # focus on Quit when opened




window.mainloop()