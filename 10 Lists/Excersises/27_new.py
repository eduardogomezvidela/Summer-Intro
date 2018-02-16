#custom replace function

def replace(string,old,new):
    

    list = string.split(old)

    new_list = ''

    for word in list:
        new_word = word
        if word != list[-1]:
            new_word = new_word + new
            

        new_list = new_list + new_word

    return (new_list)





string = 'I love clothes'

print(replace(string,'lo','xo'))

print(replace(string,'o','u'))

print(replace(string,'the','zym'))

string = 'It was the best of times, it was the worst of times, and as I walked through the aisle I asked myself: am I an ass?'

print(replace(string, 'as', 'x'))




#Cursing censor

curse_words = ['fuck','shit', 'hell', 'crap', 'whore', 'bitch']

string = 'banana fuck shit fly hell potato crap tomato blue whore bitch'

start_point = 0
answer = ''

for word in curse_words:
    string = replace(string, word, 'censored')

print(string)
