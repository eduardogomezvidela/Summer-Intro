#Specific char counter

def char_counter(word,letter):
    counter = 0

    for char in (word):
         if char == letter:
             counter+=1

    return (counter)

print(char_counter("banana","n"))
print(char_counter("banana","a"))
print(char_counter("banana","s"))
