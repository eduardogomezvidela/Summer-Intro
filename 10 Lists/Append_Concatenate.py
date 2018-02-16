#Append vs Concatenate

original = [1,2,3]

print (original)

new = original + ["cat"]    #Concatenation . Needs two lists to work

original = original +["cat"] 

print (new)



original = [1,2,3]

original.append("cat")    #Append

print (original)

#Concatenation creates a new list
#Append just adds an element to it
