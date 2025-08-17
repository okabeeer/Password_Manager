# 📂 Password Manager

A simple Python-based password manager that allows you to securely store, encrypt, and manage your passwords locally.  
It uses **Fernet encryption** (AES under the hood) from the `cryptography` library to protect your data and stores everything in a JSON file for easy access.

## ✨ Features

- ➕ Add new passwords for any platform or service  
- 📜 View saved passwords (plain or encrypted)  
- ✏️ Edit existing passwords or platform names  
- ❌ Delete passwords you no longer need  
- 🔐 Encrypt & Decrypt passwords using a stored key  
- 💾 Automatically saves data in `passwords.json` so nothing is lost between sessions  

## 🛠 Tech Stack

- Python 3  
- `cryptography` (Fernet) for encryption/decryption  
- JSON for lightweight local storage  

## 🚀 Planned Improvements

- Master password for extra security 🔑  
- CLI arguments instead of only menu input ⚡  
- Option to export/import data securely  
- Cross-platform GUI version in the future  

## 💻 Usage

1. Install dependencies:  
   ```bash
   pip install cryptography
