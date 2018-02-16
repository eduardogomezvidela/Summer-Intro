#Easter Calculator
# (1954, 1981, 2049, or 2076)

year = input("Year (1900-2099):")
year=int(year)

if (year < 1900 or year > 2099):
    print("Error")

else:
    a = year % 19
    b = year % 4
    c = year % 7
    d = (19 * a + 24) % 30
    e = (2 * b + 4 * c + 6 * d + 5) % 7
    dateofeaster = 22 + d + e

    if(year == 1954 or year == 1981 or year == 2049 or year == 2076):
        dateofeaster=dateofeaster-7

    if (dateofeaster - 31 < 1):
        dateofeaster = 31 + (dateofeaster - 31)
        print("March", dateofeaster)
    else:
        print ("April", dateofeaster-31)
