#Removes first instance of a substring from the string

def remove_first_substring(string,substring):

    string = string.replace(substring,"",1)

    print(string)

remove_first_substring("banana","na")
remove_first_substring("ma la la lakila", "la")
remove_first_substring("racecars are fast racecars","cars")
