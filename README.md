# ADVANCED-ENCRYPTION-TOOL

**COMPANY**: CODTECH IT SOLUTIONS
**NAME**: S. HARINI
**INTERN ID**: CTIS6595
**DOMAIN**: CYBER SECURITY & ETHICAL HACKING
**DURATION**: 4 WEEKS
**MENTOR**: NEELA SANTHOSH

## Project Overview
This project is developed as part of my Cybersecurity Internship at CodTech IT Solutions. The goal of this task was to build a robust and secure tool capable of encrypting and decrypting files using the Advanced Encryption Standard (AES-256) algorithm. This tool provides a high level of data confidentiality, ensuring that sensitive information remains protected through strong cryptographic techniques.

## Features
 * Strong Encryption: Implements AES-256 in CBC (Cipher Block Chaining) mode.
 * Secure Key Derivation: Uses PBKDF2 (Password-Based Key Derivation Function 2) with 1,000,000 iterations to derive a secure 256-bit key from a user password.
 * Salt & IV: Randomly generates a 16-byte salt and initialization vector (IV) for every encryption process to prevent pattern-based attacks.
 * User-Friendly Interface: A simple command-line interface (CLI) for easy interaction.
 * Error Handling: Built-in checks for incorrect passwords or corrupted files during decryption.
   
## Technical Stack
 * Language: Python 3.x
 * Library: pycryptodome
 * Algorithm: AES-256-CBC
   
## Project Structure
Encryption_Project/
│
├── main.py              # The core application logic
├── requirements.txt     # Necessary Python libraries
└── README.md            # Project documentation

## Installation & Usage

cd Advanced-Encryption-Tool

 * Install dependencies:
   pip install -r requirements.txt

 * Run the tool:
   python main.py

 * Workflow:
   * Select 'E' to encrypt a file. Provide the file name and a strong password.
   * The tool will generate a .enc file (e.g., data.txt.enc).
   * Select 'D' to decrypt. Provide the .enc file name and the correct password to retrieve the original content.
     
## Implementation Details
The tool utilizes the Crypto.Cipher module for AES implementation. To ensure maximum security, the password provided by the user is not used directly. Instead, it is combined with a unique salt and passed through the PBKDF2 function. The final encrypted file is a concatenation of the salt, IV, and the actual ciphertext, allowing for seamless decryption later.

## Conclusion
This project demonstrates the practical application of symmetric encryption in securing local files. It highlights the importance of key management and robust algorithm selection in modern cybersecurity workflows.

## OUTPUT
<img width="1920" height="1020" alt="Image" src="https://github.com/user-attachments/assets/65543836-707a-4305-9b3c-e4a319f86e77" />

<img width="1920" height="1020" alt="Image" src="https://github.com/user-attachments/assets/23668cb4-d75f-4fa3-9c6a-9b082b64ca48" />
