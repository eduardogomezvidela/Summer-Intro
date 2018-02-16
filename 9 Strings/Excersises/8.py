#Removes a certain char from a string

def remove_char(string,remove):

    for char in string:
        if char == remove:
            print("working")
            string = string.replace(remove,"")

    print(string)

remove_char("amazing", "z")
remove_char("amazing", "a")
remove_char("amazing", "g")
