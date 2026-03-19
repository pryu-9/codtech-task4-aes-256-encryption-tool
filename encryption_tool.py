
#!/usr/bin/env python3
"""
CODTECH TASK 4: AES-256 Advanced Encryption Tool
Cybersecurity Intern: Pratiksha Bhusare
"""

from cryptography.fernet import Fernet
import base64
import os
import getpass

class EncryptionTool:
    def __init__(self):
        self.key_file = "secret_key.key"
    
    def banner(self):
        print("""
╔══════════════════════════════════════════════╗
║      🔐 AES-256 ENCRYPTION TOOL v2.0         ║
║           CODTECH CYBERSECURITY TASK 4       ║
╚══════════════════════════════════════════════╝
        """)
    
    def create_key(self):
        """Generate AES-256 key"""
        key = Fernet.generate_key()
        with open(self.key_file, 'wb') as key_file:
            key_file.write(key)
        print("✅ AES-256 Key created: secret_key.key")
        return key
    
    def load_key(self):
        """Load encryption key"""
        if os.path.exists(self.key_file):
            return open(self.key_file, 'rb').read()
        return None
    
    def encrypt(self, input_file, encrypted_file):
        """Encrypt file"""
        key = self.load_key()
        if not key:
            print("❌ No key! Create key first.")
            return
        
        f = Fernet(key)
        
        with open(input_file, 'rb') as file:
            file_data = file.read()
        
        encrypted_data = f.encrypt(file_data)
        
        with open(encrypted_file, 'wb') as file:
            file.write(encrypted_data)
        
        print(f"✅ Encrypted: {input_file} → {encrypted_file}")
    
    def decrypt(self, encrypted_file, decrypted_file):
        """Decrypt file"""
        key = self.load_key()
        if not key:
            print("❌ No key found!")
            return
        
        f = Fernet(key)
        
        with open(encrypted_file, 'rb') as file:
            encrypted_data = file.read()
        
        decrypted_data = f.decrypt(encrypted_data)
        
        with open(decrypted_file, 'wb') as file:
            file.write(decrypted_data)
        
        print(f"✅ Decrypted: {encrypted_file} → {decrypted_file}")
    
    def menu(self):
        self.banner()
        
        while True:
            print("\n📋 MENU:")
            print("1. 🔑 Create AES-256 Key")
            print("2. 📁 Encrypt File")
            print("3. 🔓 Decrypt File")
            print("4. 📊 Status Check")
            print("0. ❌ Exit")
            
            choice = input("Choose: ")
            
            if choice == '1':
                self.create_key()
            
            elif choice == '2':
                infile = input("Input file (test.txt): ") or "test.txt"
                outfile = input("Output file (test.enc): ") or "test.enc"
                self.encrypt(infile, outfile)
            
            elif choice == '3':
                infile = input("Encrypted file (test.enc): ") or "test.enc"
                outfile = input("Output file (test.txt): ") or "test_decrypted.txt"
                self.decrypt(infile, outfile)
            
            elif choice == '4':
                if os.path.exists(self.key_file):
                    print("✅ Key ready!")
                else:
                    print("❌ Create key first!")
            
            elif choice == '0':
                break

if __name__ == "__main__":
    app = EncryptionTool()
    app.menu()
