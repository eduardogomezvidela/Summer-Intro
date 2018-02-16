#reverses string

def reverse_string(string):

    new_string=""

    counter=1

    for char in string:
        new_string=new_string+string[len(string)-counter]

        counter+=1
        
    return (new_string)


def main():
    print(reverse_string("apple"))
    print(reverse_string("this is so cool"))
    print(reverse_string("racecar"))

if (__name__ == "__main__"):
    main()
