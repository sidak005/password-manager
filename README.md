# password-manager


A simple, secure password manager built with Python and Tkinter.  
Store, retrieve, and manage your service passwords easily through a graphical interface!

- 🔐 **Encrypts passwords** securely using Fernet symmetric encryption.
- 💾 **Stores encrypted passwords** locally in a `passwords.json` file.
- 🖥️ **User-friendly GUI** built with Tkinter
- 🗝️ **Auto-generates a secret encryption key** if missing

## How It Works
- When you add a password, it is encrypted and saved in `passwords.json`.
- When you retrieve a password, it is decrypted and displayed in a pop-up window.
- The secret encryption key is saved securely as `secret.key`.
- GUI built using Tkinter allows easy adding and retrieving without Terminal usage.
- View all saved services through a convenient button!

## Installation 
- **Clone this repository:**
   ```bash
   git clone https://github.com/yourusername/password-manager.git
   cd password-manager
python3 main.py
