#Recognize palindromes

import reverse

def palindrome_test(string):

    new_string = reverse.reverse_string(string)

    if string == new_string:
        print("Pass")
    else:
        print("Fail")

palindrome_test("apple")            #Should fail
palindrome_test("racecar")          #Should pass
