#replace a string with another
#replace (string, old, new)

def  replace(string,old,new):
    list = string.split()
    print(list)
    new_string = ''
    
    for word in list:
        if old in word:
            new_string= new_string + ' ' + word.replace(old,new)

        else:
            new_string = new_string + ' ' + word

    return new_string



string = 'I love spam! Yum, spam sure is great, spam, spam, spam! Yummy!'

print(replace (string,'am','um'))

string = 'Every day I er at the market. But I rer to er again.'

print(replace(string,'er','w'))
