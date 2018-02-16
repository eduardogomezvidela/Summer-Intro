



#Write a program that will convert degrees fahrenheit to degrees celsius.
#Deduct 32, then multiply by 5, then divide by 9

str_f=input("Temperature in fahrenheit:")
fahrenheit=int(str_f)

celsius=((fahrenheit-32)*5)/9
print(celsius)
