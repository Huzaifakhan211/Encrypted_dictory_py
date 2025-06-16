# Encrypted_dictory_py

# Secure Personal Diary (Python, Encrypted, GUI)

This is a Python-based personal diary application that includes password protection, AES-based encryption (via Fernet), and a graphical interface using Tkinter. Entries are organized into categories like birthdays, anniversaries, goals, and more.

## Features

* Password-protected login system
* Encrypted diary entries using the `cryptography` library
* GUI interface for adding and viewing entries
* Support for categories such as birthdays, goals, travel, etc.
* Data saved locally in encrypted JSON format

## Technologies Used

* Python 3
* tkinter (for GUI)
* cryptography (for encryption)
* hashlib (for password hashing)
* json and datetime modules

---

## Project Structure
secure-diary/
│
├── main.py           # Main application script
├── diary.json        # Encrypted diary data
├── key.key           # Fernet key for encryption/decryption
├── password.hash     # Stored hashed password

## How to Run

1. Install required packages:

   pip install cryptography
   
2. Run the application:

   python main.py

3. On the first run, you will be asked to set a password. This will generate the required key and password files.

4. After logging in, you can add entries by selecting a category, setting a date, and writing your note.

## Categories Included

 Birthday
 Anniversary
 Foundation Day
 Goals
 Achievements
 Dreams
 Travel
 Other

## Possible Future Enhancements

* Edit or delete existing entries
* Search functionality
* Backup or cloud sync
* Dark mode or theme customization

