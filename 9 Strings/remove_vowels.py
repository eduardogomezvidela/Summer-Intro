#This program removes the vowels from a string

word = input ("Word: ")
vowels = "aAeEiIoOuU"

new_word=""

for each_char in word:
    if each_char not in vowels:
        new_word = new_word + each_char

print (new_word)
