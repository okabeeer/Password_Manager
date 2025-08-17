from cryptography.fernet import Fernet
from Passwords import Passwords
import os
import json

ans = False
passwords: list[Passwords] = []

# [*] Key management
if os.path.exists("key.key"):
    with open("key.key", "rb") as f:
        key = f.read()
else:
    key = Fernet.generate_key()
    with open("key.key", "wb") as f:
        f.write(key)

cipher = Fernet(key)

# [*] Load saved passwords
if os.path.exists("passwords.json"):
    with open("passwords.json", "r") as f:
        data = json.load(f)
        for i in data:
            pw = i["password"]
            passwords.append(Passwords(i["name"], pw))

while not ans:
    print("_______________________")
    print("[*] Password Manager")
    print("1. [+] Add password")
    print("2. [DIR] View passwords")
    print("3. [*] Edit password")
    print("4. [X] Delete password")
    print("5. [#] Encrypt a password")
    print("6. [#] Decrypt a password")
    print("7. [*] Exit and save")
    print("_______________________")

    try:
        n = int(input("Choose an option: "))
    except ValueError:
        print("[X] Enter a valid number from the list!")
        continue

    if n == 1:
        name = input("Enter the platform name: ")
        pswd = input("Enter the password: ")
        passwords.append(Passwords(name, pswd))
        print(f"[OK] Password for {name} added.")

    elif n == 2:
        print("_______________________")
        print("[DIR] Stored Passwords")
        print("_______________________")
        if not passwords:
            print("[!] No passwords found!")
        else:
            for count, i in enumerate(passwords, start=1):
                print(f"{count}. [*] {i.name}: {i.pwrd}")
        print("_______________________")

    elif n == 3:
        try:
            nn = int(input("Enter the number of the password to edit: "))
            if 1 <= nn <= len(passwords):
                choice = input("What do you want to edit (name/password)? ").lower()
                if choice == "name":
                    namee = input("Enter the new name: ")
                    passwords[nn - 1].name = namee
                    print("[OK] Name updated.")
                elif choice == "password":
                    pswdd = input("Enter the new password: ")
                    passwords[nn - 1].pwrd = pswdd
                    print("[OK] Password updated.")
                else:
                    print("[X] Invalid choice.")
            else:
                print("[X] Invalid password number.")
        except ValueError:
            print("[X] Enter a valid number!")

    elif n == 4:
        try:
            nn = int(input("Enter the number of the password to delete: "))
            if 1 <= nn <= len(passwords):
                del passwords[nn - 1]
                print("[OK] Password deleted.")
            else:
                print("[X] Invalid password number.")
        except ValueError:
            print("[X] Enter a valid number!")

    elif n == 5:
        try:
            nn = int(input("Enter the number of the password to encrypt: "))
            if 1 <= nn <= len(passwords):
                pw_obj = passwords[nn - 1]
                if isinstance(pw_obj.pwrd, str):
                    pw_obj.pwrd = cipher.encrypt(pw_obj.pwrd.encode())
                    print("[#] Password encrypted.")
                else:
                    print("[!] Already encrypted.")
            else:
                print("[X] Invalid password number.")
        except ValueError:
            print("[X] Enter a valid number!")

    elif n == 6:
        try:
            nn = int(input("Enter the number of the password to decrypt: "))
            if 1 <= nn <= len(passwords):
                pw_obj = passwords[nn - 1]
                if isinstance(pw_obj.pwrd, bytes):
                    pw_obj.pwrd = cipher.decrypt(pw_obj.pwrd).decode()
                    print("[#] Password decrypted.")
                else:
                    print("[!] Password is not encrypted.")
            else:
                print("[X] Invalid password number.")
        except ValueError:
            print("[X] Enter a valid number!")

    elif n == 7:
        with open("passwords.json", "w") as f:
            json.dump(
                [
                    {
                        "name": i.name,
                        "password": i.pwrd.decode() if isinstance(i.pwrd, bytes) else i.pwrd,
                    }
                    for i in passwords
                ],
                f,
                indent=4,
            )
        print("[*] Passwords saved! Goodbye.")
        ans = True

    else:
        print("[X] Enter a number from 1 to 7!")
