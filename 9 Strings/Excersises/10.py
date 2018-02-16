#Substring Counter

string = "na nana na"

substring = "na"

counter = 0


for char in string:
        
    if  substring in string:
         counter+=1
         string = string [ len(substring) :]

print(counter)
