#Write a function areaOfCircle(r) which returns the area of a circle of radius r. Make sure you use the math module in your solution.

#Calculates the area of a circle

def circle_area(r):
    import math
    pi=math.pi
    area=pi*r**2
    return area

print(circle_area(5))
