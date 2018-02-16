def cipher(message,cipher):

    new_message = ''

    for char in message:
        if ord(char) > 96:
            encrypt = ord(char) - 97
            new_message = new_message + cipher[encrypt]

        elif ord(char) < 96 and ord(char) > 64:
            encrypt = ord(char) - 65
            new_message = new_message + cipher[encrypt].upper()

        else:
            new_message = new_message + char

    return(new_message)
