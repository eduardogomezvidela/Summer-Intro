#Strings
#A small list of all string methods I have seen

string = ("Hello, world")

print(string)

print(string.upper())
print(string.lower())

print("-------------------------")

heyo = ("     Heyo     ")

print(heyo)
print("*",heyo.strip(),"*")
print("*",heyo.lstrip(),"*")
print("*",heyo.rstrip(),"*")

print("-------------------------")

like = ("I LIKE IKE")

print(like.count("i"))
print(like.count("I"))

print(like.replace("I","U"))


print("-------------------------")

guille=("Guillermo Maldonado")

print(guille)
new_guille = guille
new_guille = new_guille.replace("u","o")
new_guille = new_guille.replace("i","o")
new_guille = new_guille.replace("e","o")
new_guille = new_guille.replace("a","o")
print(new_guille)

print("-------------------------")

print(guille.center(25))
print(guille.ljust(25))
print(guille.rjust(25))

print("-------------------------")

print(guille.find("o"))
print(guille.rfind("o"))

print("-------------------------")

print(guille.find("x"))

print(guille.index("x"))            #Returns runtime error
