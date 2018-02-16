#Largest Palindrome from the product of two 3-digit numbers

biggest = 0

for a in range (100,1000):          #Iterate through all possible multiplications
    for b in range (100,1000):

        num = str(a*b)  #Convert the result of a*b into a string

        num = list(num) #Separate the string of ints into a list. This will allow us to check if the number is a palindrome

        length = len(num)

        if length == 6 and num[0] == num[-1] and num[1] == num[-2] and num[2] == num[-3]: #This way we can access all palindromes 6 ints long
            
            num = "".join(num)  #Glues back the palindrome into a single string
            
            num = int(num)  #Converts the palindrome back to an int

            if num > biggest:   #Updates largest palindrome
                biggest = num

print(biggest)

"""We could also add an if length == 5 statement to check for palindromes that are 5 digits long, but since any palindrome that is
6 digits long will be bigger, we don't need to."""
