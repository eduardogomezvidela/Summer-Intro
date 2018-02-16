a = input("Side a:")
a=float(a)

b= input("Side b:")
b= float(b)

c= input("Side c:")
c=float(c)

if (a > b and a > c):
    short1 = b
    short2 = c
    hypot = a
elif (b>a and b>c):
    short1=a
    short2=c
    hypot=b
elif (c > a and c > b):
    short1=a
    short2=b
    hypot=c

x=short1**2+short2**2
y=hypot**2

if  (abs(x-y) < 0.1):           #This is used because the exact number will not be the same. But if they are close enough then we accept them.
    print(True)
else:
    print(False)
