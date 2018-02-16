#Write a fruitful function sumTo(n) that returns the sum of all integer numbers up to and including n.
#So sumTo(10) would be 1+2+3...+10 which would return the value 55. Use the equation (n * (n + 1)) / 2.

def sum_to():
    n=input("Number:")
    n=int(n)
    answer=(n*(n+1))/2
    return answer

print(sum_to())
