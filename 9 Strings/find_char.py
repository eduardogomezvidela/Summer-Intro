#Find a char and return value

def find_char (word,letter):
    counter=-1
    for char in word:
        counter = counter + 1
        if (char == letter):
            print (word[counter], counter)
            return True
        elif counter == len(word)-1:
            print("-1")

find_char("banane","e")

#Find the second iteration of a char and return value

def find_char2 (word,letter):
    counter=-1
    f=0
    for char in word:
        counter = counter + 1
        if (char == letter and f == 1):
            print (word[counter], counter)
            return True
        elif(char == letter):
            f=f+1

        elif counter == len(word)-1:
            print("-1")

find_char2("banana","a")

#Find a char (you can choose where to start and finish looking for it) and return value

def find_char3 (word,letter,start=0,end=None):

    char = letter
    counter=start-1

    if end==None:
        end=len(word)
    
    for char in word:

        counter = counter+1
        
        if char == letter:
            print(letter, counter)
            return True
        elif counter == len(word) or counter ==end:
            print("-1")
            return False

find_char3("banana","n",2,3)
find_char3("banana","a",2)
