import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes

# Key Generation Logic (Using PBKDF2 for AES-256)
def generate_key(password, salt):
    return PBKDF2(password, salt, dkLen=32, count=1000000)

def encrypt_file(file_path, password):
    salt = get_random_bytes(16)
    key = generate_key(password, salt)
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)

    try:
        with open(file_path, 'rb') as f:
            plaintext = f.read()
        
        ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
        
        # Salt + IV + Data-va ".enc" file-a save pannuvom
        output_path = file_path + ".enc"
        with open(output_path, 'wb') as f:
            f.write(salt + iv + ciphertext)
        
        print(f"\n[+] Success! Encrypted file: {output_path}")
    except Exception as e:
        print(f"[-] Error: {e}")

def decrypt_file(file_path, password):
    try:
        with open(file_path, 'rb') as f:
            data = f.read()
        
        salt = data[:16]
        iv = data[16:32]
        ciphertext = data[32:]
        
        key = generate_key(password, salt)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        
        decrypted_data = unpad(cipher.decrypt(ciphertext), AES.block_size)
        
        # Original extension-a retain panna logic
        output_path = file_path.replace(".enc", "_decrypted.txt")
        with open(output_path, 'wb') as f:
            f.write(decrypted_data)
        
        print(f"\n[+] Success! Decrypted file: {output_path}")
    except (ValueError, KeyError):
        print("[-] Error: Incorrect password or corrupted file!")
    except Exception as e:
        print(f"[-] Error: {e}")

def main():
    print("="*30)
    print(" AES-256 ENCRYPTION TOOL ")
    print("="*30)
    
    choice = input("Enter 'E' to Encrypt or 'D' to Decrypt: ").upper()
    file_name = input("Enter the file name (e.g., sample_file.txt): ")
    
    if not os.path.exists(file_name):
        print("[-] Error: File not found!")
        return

    passphrase = input("Enter a strong password: ")

    if choice == 'E':
        encrypt_file(file_name, passphrase)
    elif choice == 'D':
        decrypt_file(file_name, passphrase)
    else:
        print("[-] Invalid selection!")

if __name__ == "__main__":
    main()