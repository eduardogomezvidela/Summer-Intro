#mirrors string

def mirror_string(string):

    new_string=""

    counter = 1

    for char in string:
        a = string[len(string)-counter]

        new_string = new_string + a

        counter+=1

    final_string = string+new_string

    print (final_string)

mirror_string("apple")
mirror_string("racecar")
mirror_string("okay")
