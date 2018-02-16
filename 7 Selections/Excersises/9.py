import is_even

x=input("Input:")
x=int(x)

if (x == 0):
    print("Error")
else:
    x=x-1
    is_even.is_even(x)
