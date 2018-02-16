#censor

curse_words = ['fuck','shit', 'hell', 'crap', 'whore', 'bitch']

string = 'banana fuck shit fly hell potato crap tomato blue whore bitch'

start_point = 0

for word in curse_words:
    string = string.replace(word, 'censored')

print(string)
