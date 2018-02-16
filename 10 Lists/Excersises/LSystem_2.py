#A = B
#B = AB

#L-System

def LSystem (iterations,axiom):
    org_string = axiom                              #The org_string starts as the axiom that we input
    new_string= ''

    for i in range (iterations):                        #This will make our new_string update itself accordingly and the right amount of times
        new_string = process(org_string)
        org_string = new_string

    return new_string

def process(org_string): #This will need to iterate through each char in the org_string, return a new_string and call the rules
    new_string = ''
    
    for char in org_string:
        new_string = new_string + apply_rules(char)

    return new_string

def apply_rules(char):
    new_string=''

    if char == 'F':
        new_string = 'F[-F]F[+F]F'
    elif char == 'X':
        new_string = 'X[-FFF][+FFF]FX'
    else:
        new_string = char

    return new_string


def main():
    print(LSystem(4,'H'))

if (__name__ == "__main__"):
    main()
