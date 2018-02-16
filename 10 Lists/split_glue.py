#Splitting and Gluing


song = 'The wheels on the bus'

song_list = song.split()    #Returns a list (from a string) SPLITS A LIST

print(song_list)

new = ' '.join(song_list)   #Returns a  string (from a list) JOINS TOGETHER
         
print (new)

for word in song_list:  #Returns initial of each word
    print(word[0])
