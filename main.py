# script will run the password manager, letting users add or retrieve passwords.
from password_manager import PasswordManager 
def main():
    pm = PasswordManager()
    while True:
        action = input("Do you want to add a new password or retrieve an existing one? (add/retrieve/quit): ").lower()
        
        if action == "add":
            service = input("Enter the service name: ")
            password = input("Enter the password: ")
            pm.save_password(service, password)
            print(f"Password for {service} added successfully.")

        elif action == "retrieve":
            service = input("Enter the service name: ")
            password = pm.retrieve_password(service)
            if password:
                print(f"Password for {service} is {password}.")
            else:
                print(f"No password found for {service}.")

        elif action == "quit":
            break
        else:
            print("Invalid action. Please choose 'add', 'retrieve', or 'quit'.")

if __name__ == "__main__":
    main()
