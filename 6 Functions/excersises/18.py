#adds all numbers from 1 to n



def sum_to(n):
    x=0
    y=0
    for i in range(n):
        x=i+1
        y=y+x
    return y

print(sum_to(10))
