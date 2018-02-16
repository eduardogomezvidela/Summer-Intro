#Will print the sum of 2 different squared numbers

def square_sum (a,b):                       #Define the function
    x=square(a)                                     #Call the other function (note that I still have not defined it)
    y=square(b)
    result=x+y
    return result

def square (a):                                 #Define the other function
    result = a*a
    return result

num1=input("First number:")             #Get user input for the two arguments we will use
num1=int(num1)

num2=input("Second number:")
num2=int(num2)

answer = square_sum(num1,num2)          #Call the square_sum function and pass it arguments

print (answer)
