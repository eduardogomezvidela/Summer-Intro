#Pi using Madhava
#Pi = sqrt(12)* ((1) - (1/3*3) + (1/5*3**2) - (1/7*3**3) + (.......))

import math

answer = 1
answer= float (answer)
x=1
x=int (x)
y=0
y= int (y)

for i in range (6000):
    x= x + 2
    y = y + 1
    answer = answer - (1 / (x * ( 3 ** y)))
    x= x + 2
    y = y + 1
    answer = answer + (1 / (x * ( 3 ** y)))




answer = answer *(math.sqrt(12))
answer =format(answer, '.50f')
print(answer)

#Correct PI
#3.14159265358979323846264338327950288419716939937510

#my Pi
#3.14159265358979400417638316866941750049591064453125
