#Takes a string and substring and counts the substrings

def substring_counter(string, substring):

    string = string.replace(substring, "ñ")

    counter= 0

    for char in string:
        if char == "ñ":
            counter+=1

    print(counter)

substring_counter("banana", "na")
substring_counter("apple", "pp")
substring_counter("suzuki", "u")
substring_counter("bananag na n a an na", "na")
