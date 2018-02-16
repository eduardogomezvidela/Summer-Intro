#THE ENIGMA MACHINE

import time
import cipher_machine

def print_slow(str,str2):
    for letter in str:
        sys.stdout.write(letter)
    for letter in str2:
        sys.stdout.write(letter)


cipher = "plmkonhijbuvygtfcrxdeszwaq"
abc = "abcdefghijklmnopqrstuvwxyz"
ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

encrypted_message = (cipher_machine.cipher("It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief.", cipher))

decrypted_message = ''

print('\n' * 6)
print("Encrypted Message:")
print()
print(encrypted_message)
print()

begin = input("")
if begin == "decrypt":

    for char in encrypted_message:
        if ord(char) > 96:
            decrypted_message = decrypted_message + abc[cipher.find(char)]

        elif ord(char) > 64:
            char = char.lower()
            decrypted_message = decrypted_message + ABC[cipher.find(char)].upper()

        else:
            decrypted_message = decrypted_message + char

        print (decrypted_message, encrypted_message[len(decrypted_message):])
        time.sleep(0.025)
