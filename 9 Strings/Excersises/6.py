#reverses string

def reverse_string(string):

    new_string=""

    counter=1

    for char in string:
        new_string=new_string+string[len(string)-counter]

        counter+=1
        
    print (new_string)


reverse_string("apple")
reverse_string("this is so cool")
reverse_string("racecar")
