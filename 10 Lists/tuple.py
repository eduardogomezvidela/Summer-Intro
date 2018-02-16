#tuple

#Tuples are useful for records

tuple = ("Gomez Videla", "Eduardo", 19, "Male", 1997, "Sao Paulo")

edu = (last_name, first_name, age, sex, birth_year, birth_location)  = tuple

print (edu)

#######################################

"""Tuples can also be used to switch values"""

a = 1
b = 2

(a,b) = (b, a)

print (a) #a is now 2
print(b) #b is now 1
