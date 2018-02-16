def pop (x,y):
    print(x+y)
    print(__name__)                             #This is just to show that when we run the program this will be "__main__" but if
                                                                  #we import it and call it in from somewhere else it will be "soda" (the name of the program)
def main():
    pop(9,5)

if (__name__ == "__main__"):            #Will only run the actual program (for testing in this case) if we run this program and not
    main()                                                      #import it and call it in from another program

