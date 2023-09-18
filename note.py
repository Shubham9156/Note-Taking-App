import os
from cryptography.fernet import Fernet

# Function to generate a random encryption key
def generate_key():
    return Fernet.generate_key()

# Function to encrypt data using a key
def encrypt_data(key, data):
    f = Fernet(key)
    encrypted_data = f.encrypt(data.encode())
    return encrypted_data

# Function to decrypt data using a key
def decrypt_data(key, encrypted_data):
    f = Fernet(key)
    decrypted_data = f.decrypt(encrypted_data)
    return decrypted_data.decode()

# Function to save a note to a file
def save_note(key, filename, note):
    encrypted_note = encrypt_data(key, note)
    with open(filename, 'wb') as file:
        file.write(encrypted_note)

# Function to load a note from a file
def load_note(key, filename):
    try:
        with open(filename, 'rb') as file:
            encrypted_note = file.read()
            decrypted_note = decrypt_data(key, encrypted_note)
            return decrypted_note
    except FileNotFoundError:
        return None

if __name__ == "__main__":
    key = generate_key()
    notes_directory = "notes"
    os.makedirs(notes_directory, exist_ok=True)

    while True:
        print("\nSecure Note-Taking App")
        print("1. Create Note")
        print("2. View Note")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            note_title = input("Enter the note title: ")
            note_content = input("Enter the note content: ")
            note_filename = os.path.join(notes_directory, note_title + ".txt")
            save_note(key, note_filename, note_content)
            print("Note saved successfully.")

        elif choice == '2':
            note_title = input("Enter the note title: ")
            note_filename = os.path.join(notes_directory, note_title + ".txt")
            note_content = load_note(key, note_filename)
            if note_content:
                print(f"Note: {note_content}")
            else:
                print("Note not found.")

        elif choice == '3':
            break
