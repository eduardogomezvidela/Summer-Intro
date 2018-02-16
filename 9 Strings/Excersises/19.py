#THE ENIGMA MACHINE

import cipher_machine

cipher = "plmkonhijbuvygtfcrxdeszwaq"
abc = "abcdefghijklmnopqrstuvwxyz"
ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

encrypted_message = (cipher_machine.cipher("It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief.", cipher))

decrypted_message = ''

print(encrypted_message)

for char in encrypted_message:
    if ord(char) > 96:
        decrypted_message = decrypted_message + abc[cipher.find(char)]

    elif ord(char) > 64:
        char = char.lower()
        decrypted_message = decrypted_message + ABC[cipher.find(char)].upper()

    else:
        decrypted_message = decrypted_message + char

print (decrypted_message, encrypted_message[len(decrypted_message):])
