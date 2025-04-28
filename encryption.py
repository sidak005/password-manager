# module to handle encryption and decryption of passwords.
from cryptography.fernet import Fernet
import os

class EncryptionManager:
    def __init__(self, key=None):
        if key is None:
            self.key = Fernet.generate_key()
            with open("secret.key", "wb") as key_file:
                key_file.write(self.key)
        else:
            self.key = key
        self.cipher_suite = Fernet(self.key)
    
    @staticmethod
    def load_key():
        if not os.path.exists("secret.key"):
            # Generate a new key if it doesn't exist
            key = Fernet.generate_key()
            with open("secret.key", "wb") as key_file:
                key_file.write(key)
            return key
        else:
            with open("secret.key", "rb") as key_file:
                return key_file.read()
    
    def encrypt(self, data):
        return self.cipher_suite.encrypt(data.encode())
    
    def decrypt(self, encrypted_data):
        return self.cipher_suite.decrypt(encrypted_data).decode()
