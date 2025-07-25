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
![image](https://github.com/user-attachments/assets/4a8d9af6-3cfc-42f1-b969-1a69506afbcb)
![image](https://github.com/user-attachments/assets/726f6766-b246-4e60-a3a3-040432b25d55)
![image](https://github.com/user-attachments/assets/5d5a5df1-ef0b-41af-9f4f-f2ce7a50eea8)
![image](https://github.com/user-attachments/assets/0b42005d-5baf-4a0d-aafc-7e37ac108da4)
![image](https://github.com/user-attachments/assets/bfcce205-2488-4ee4-be15-9f593c678f44)
![image](https://github.com/user-attachments/assets/8dbfc59f-16e5-4034-b0bf-a4fdb28a5aa5)






