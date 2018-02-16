#Leap year list

import lp


x = 0

for i in range (3000):
    lp.leap_year(i)
    if (lp.leap_year(i) == True):
        print (i)
