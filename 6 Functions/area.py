#square_area will return the area of a square that will be determined by the input

def square_area (length):                       #Define the fruitful function
    length=int(length)
    area=length*length
    return area

result=square_area(input("Length?"))        #Call the fruitful function and assing what it returns to 'result'

print("Area:", result)                                           #These last two lines are different ways of printing the result


print("Area:", square_area(input("Length?")))
