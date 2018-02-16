#Caesar's Cipher

message = "Hello World"     #uryyb jbeyq

encrypted_message = ''

for char in message:
    o_char = char
    char = ord(char)
    
    if char + 13 < 122 and char + 13 > 104:          #lowercase letters
        char = (char) +13
        encrypted_message = encrypted_message + chr(char)
    elif (char) + 13 > 122:
        char = 96 + char + 13 - 122
        encrypted_message = encrypted_message + chr(char)
        
    elif char + 13 < 90 and char + 13 > 64:         #uppercase letters
        char = (char) +13
        encrypted_message = encrypted_message + chr(char)
    elif (char) + 13 > 90:
        char = 64 + char + 13 - 90
        encrypted_message = encrypted_message + chr(char)

    else:
        encrypted_message = encrypted_message + o_char  #spaces and grammar

print(encrypted_message)
