#Write a function called mySqrt that will approximate the square root of a number, call it n,
#by using Newtow's algorithm. Newton's approach is an iterative guessing algorithm where
#the initial guess is n/2 and each subsequent guess is computed using the formula: newguess = (1/2) * (oldguess + (n/oldguess)).

#Newton's algorithm
#once the guesses start repeating you have gotten the correct result

def newton(n):
    
    #n=input("Number:")
    n=int(n)

    oldguess=n/2
    print("Guess 1", oldguess)

    for i in range(100):
        newguess=(1/2)*(oldguess+(n/oldguess)) #does the Newton calculation

        if (oldguess==newguess):                                    #Checks if we have arrived at the answer
            exit=input("Press enter to close")
            quit()
        oldguess=newguess
        print("Better Guess", i+1, ":", newguess)


newton(25)
