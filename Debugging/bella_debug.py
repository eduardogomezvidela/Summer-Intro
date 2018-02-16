import math

def myPi(iters):
    sign = 1
    denominator = 1
    initial = 0

    for i in range(iters):
        initial = initial + (sign/denominator)
        sign = sign * -1
        denominator = (denominator + 2) * 3**(initial)

    piapprox = initial * math.sqrt(12)

    return piapprox

t = myPi(1000)

print(t)
