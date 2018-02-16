a = input("Side a:")
a=float(a)

b= input("Side b:")
b= float(b)

c= input("Side c:")
c=float(c)

x=a**2+b**2
y=c**2

if  (abs(x-y) < 0.1):           #This is used because the exact number will not be the same. But if they are close enough then we accept them.
    print(True)
else:
    print(False)
