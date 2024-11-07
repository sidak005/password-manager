# module to manage storing, retrieving, and generating passwords
import json
from encryption import EncryptionManager
import os

class PasswordManager:
    def __init__(self):
        self.encryption_manager = EncryptionManager(EncryptionManager.load_key())
        self.data_file = "passwords.json"
        if not os.path.exists(self.data_file):
            with open(self.data_file, 'w') as file:
                json.dump({}, file)

    def save_password(self, service, password):
        encrypted_password = self.encryption_manager.encrypt(password)
        with open(self.data_file, "r+") as file:
            data = json.load(file)
            data[service] = encrypted_password.decode()
            file.seek(0)
            json.dump(data, file)

    def retrieve_password(self, service):
        with open(self.data_file, "r") as file:
            data = json.load(file)
            encrypted_password = data.get(service)
            if encrypted_password:
                return self.encryption_manager.decrypt(encrypted_password)
            return None
