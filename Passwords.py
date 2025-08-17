from cryptography.fernet import Fernet

class Passwords:
    def __init__(self,name:str,pwrd:str):
        self.name=name
        self.pwrd=pwrd