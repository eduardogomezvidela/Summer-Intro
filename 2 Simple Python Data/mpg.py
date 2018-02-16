#Write a program that will compute MPG for a car.
#Prompt the user to enter the number of miles driven and the number of gallons used.
#Print a nice message with the answer.

str_miles=input("How many miles did you drive?")
str_gallons=input("How many gallons did you consume?")

miles=int(str_miles)
gallons=int(str_gallons)

mpg=miles/gallons
print("Your car drives", mpg, "miles per gallon")
