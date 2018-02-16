#Removes all instances of substring from a string

def remove_substring(string,substring):

    string = string.replace(substring,"")

    print (string)

remove_substring("banana","na")
remove_substring("bamboo nozzle", "o")
remove_substring("education for edu and eddy", "ed")
