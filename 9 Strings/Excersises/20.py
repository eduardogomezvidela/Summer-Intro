#removes all duplicate letters

def remove_duplicates(string):

    banned = ''
    new_string = ''
    for char in string:
        if char not in banned:
            new_string = new_string + char
        if string.count(char) > 1 and char !=' ':
            banned = banned+char

    print (new_string)

remove_duplicates("remove all duplicates")
