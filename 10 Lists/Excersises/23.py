#5 char word counter

list = ['no','umm', 'crazy', 4, 'banana', 'scuba', 'apple', 1, 'nope', 'bloke'] #4 5 letter words

five_letters = 0
counter = 0


for word in list:

    counter = 0
    if (type(word)) == int:     #In case of ints in list
        x = 0

    else:                                                   #Counts 5 letter words
        for letter in word:
            counter = counter +1
        if counter == 5:
            five_letters = five_letters + 1

print(five_letters)
