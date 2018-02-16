#3 criteria must be taken into account to identify leap years:
#The year is evenly divisible by 4; CHECK
#If the year can be evenly divided by 100, it is NOT a leap year, unless;
#The year is also evenly divisible by 400. Then it is a leap year.
#Write a function that takes a year as a parameter and returns True if the year is a leap year, False otherwise.

def leap_year(year):

    if (year == 0):                                 #Year 0 is not a leap year (I think?)
        return False

    else:
        if (year % 4 == 0 ):
            if (year < 100):                            #For values smaller than 100
                return True
            
            if (year % 100 != 0 and year > 100 and year < 400):         #For values between 100 and 400
                return True
            
            if (year % 400 == 0  or year % 100 != 0 and year >= 400):           #For valuse larger than 400 (and 400)
                return True

            elif (year % 100 == 0 and year % 400 != 0):
                return False
            
        else:
            return False

def main():
    year = input("Year:")
    year=int(year)

    leap_year(year)

    print (leap_year(year))
