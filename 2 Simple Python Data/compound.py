
#Write a Python program that assigns the principal amount of 10,000 to variable P,
#assign to n the value 12, and assign to r the interest rate of 8% (0.08). Then
#have the program prompt the user for the number of years, t, that the
#money will be compounded for. Calculate and print the final amount after t years.

#     a = p(1+(r/n))**(n*t)

t_string=input("What is t?")
t=int(t_string)

print(type(t))

a = 10000*(1+(0.08/12))**(12*t)

print(a)
