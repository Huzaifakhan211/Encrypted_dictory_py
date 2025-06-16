import json
import os
import hashlib
from cryptography.fernet import Fernet
from datetime import datetime
from tkinter import *
from tkinter import messagebox

# ======== SETTINGS ========= #
PASSWORD_FILE = 'password.hash'
KEY_FILE = 'key.key'
DIARY_FILE = 'diary.json'

# ======== UTILITIES ========= #
def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, 'wb') as f:
        f.write(key)
    return key

def load_key():
    if not os.path.exists(KEY_FILE):
        return generate_key()
    with open(KEY_FILE, 'rb') as f:
        return f.read()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def setup_password_gui():
    def save_password():
        new_pass = new_pass_entry.get()
        if new_pass:
            with open(PASSWORD_FILE, 'w') as f:
                f.write(hash_password(new_pass))
            messagebox.showinfo("Success", "Password set. Restart the app.")
            root.destroy()
    root = Tk()
    root.title("Set Password")
    Label(root, text="Set your diary password:").pack(pady=5)
    new_pass_entry = Entry(root, show="*")
    new_pass_entry.pack(pady=5)
    Button(root, text="Set Password", command=save_password).pack(pady=10)
    root.mainloop()

def verify_password_gui(password_input):
    if not os.path.exists(PASSWORD_FILE):
        setup_password_gui()
        return False
    with open(PASSWORD_FILE, 'r') as f:
        stored_hash = f.read()
    return hash_password(password_input) == stored_hash

# ======== DIARY FUNCTIONS ========= #
def encrypt_data(data, fernet):
    return fernet.encrypt(data.encode())

def decrypt_data(data, fernet):
    return fernet.decrypt(data).decode()

def load_diary(fernet):
    if not os.path.exists(DIARY_FILE):
        return {}
    with open(DIARY_FILE, 'rb') as f:
        encrypted = f.read()
    if not encrypted:
        return {}
    try:
        decrypted = decrypt_data(encrypted, fernet)
        return json.loads(decrypted)
    except:
        print("Failed to decrypt diary.")
        return {}

def save_diary(data, fernet):
    with open(DIARY_FILE, 'wb') as f:
        encrypted = encrypt_data(json.dumps(data), fernet)
        f.write(encrypted)

def add_entry_gui(diary, fernet):
    entry_window = Toplevel()
    entry_window.title("Add Entry")

    Label(entry_window, text="Category:").pack()
    categories = ["birthday", "anniversary", "foundation day", "goals", "achievements", "dreams", "travel", "other"]
    cat_var = StringVar(entry_window)
    cat_var.set(categories[0])
    OptionMenu(entry_window, cat_var, *categories).pack()

    Label(entry_window, text="Date (YYYY-MM-DD):").pack()
    date_entry = Entry(entry_window)
    date_entry.pack()

    Label(entry_window, text="Note:").pack()
    note_entry = Text(entry_window, height=5, width=40)
    note_entry.pack()

    def save_entry():
        category = cat_var.get()
        date = date_entry.get()
        note = note_entry.get("1.0", END).strip()
        if not date or not note:
            messagebox.showerror("Error", "Date and note cannot be empty.")
            return
        if category not in diary:
            diary[category] = []
        diary[category].append({
            "date": date,
            "note": note,
            "timestamp": datetime.now().isoformat()
        })
        save_diary(diary, fernet)
        messagebox.showinfo("Success", "Entry added successfully!")
        entry_window.destroy()

    Button(entry_window, text="Save Entry", command=save_entry).pack(pady=10)

def view_entries_gui(diary):
    view_window = Toplevel()
    view_window.title("View Entries")

    for category, entries in diary.items():
        Label(view_window, text=f"--- {category.upper()} ---", fg="blue", font=('Arial', 12, 'bold')).pack()
        for entry in entries:
            Label(view_window, text=f"{entry['date']}: {entry['note']} (added on {entry['timestamp']})").pack(anchor="w", padx=10)

# ======== MAIN APP ========= #
def main_gui():
    def attempt_login():
        pw = pw_entry.get()
        if verify_password_gui(pw):
            login_win.destroy()
            run_diary_app()
        else:
            messagebox.showerror("Login Failed", "Incorrect password.")

    login_win = Tk()
    login_win.title("Secure Personal Diary")

    Label(login_win, text="Enter Password", font=('Arial', 14)).pack(pady=10)
    pw_entry = Entry(login_win, show="*", width=30)
    pw_entry.pack(pady=5)
    Button(login_win, text="Login", command=attempt_login).pack(pady=10)

    login_win.mainloop()

def run_diary_app():
    key = load_key()
    fernet = Fernet(key)
    diary = load_diary(fernet)

    root = Tk()
    root.title("My Secure Diary")

    Button(root, text="Add Entry", command=lambda: add_entry_gui(diary, fernet), width=20).pack(pady=10)
    Button(root, text="View Entries", command=lambda: view_entries_gui(diary), width=20).pack(pady=10)
    Button(root, text="Exit", command=root.destroy, width=20).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main_gui()
