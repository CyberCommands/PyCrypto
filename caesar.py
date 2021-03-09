#!/usr/bin/env python3
import os
import pyperclip

os.system('cls' if os.name == 'nt' else 'clear')

# The string to be encrypted/decrypted.
message = input("[>] Enter a message: ")

key = 13    # The encryption/decryption key.

# Tells the program to encrypt or decrypt.
mode = 'encrypt'    # Set to 'encrypt' or 'decrypt'.

# Every possible symbol that can be encrypted.
alphabet = 'abcdefghijklmnopqrstuvwyzABCDEFGHIJKLMNOPQRSTUVWYZ'

translated = ''     # Stores the encrypted/decrypted form of the message.

#message = message.upper()   # Capitalize the string in message.

for symbol in message:
    if symbol in alphabet:
        # Get the encrypted (or decrypted) number for this symbol.
        num = alphabet.find(symbol)     # Get the number of the symbol.
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key
        
        # Alphabet of less than 0
        if num >= len(alphabet):
            num = num - len(alphabet)
        elif num < 0:
            num = num + len(alphabet)
        
        # Add encrypted/decrypted number's symbol at the end of translated.
        translated = translated + alphabet[num]
    
    else:
        # Just add the symbol without encryting/decrypting.
        translated = translated + symbol

print('\033[92m[*] Original Text : \033[0m',message)
print('\033[92m[+] Cipher Text   : \033[0m',translated)

# Copy the encrypted/decrypted string to the clipboard.
pyperclip.copy(translated)

quit()