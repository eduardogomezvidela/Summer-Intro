#multiplication table 12x12

for i in range(1,13):
    print('\t', i, end=" ")

for x in range(1,13):
    print('\n', '\n', x)
    for y in range(1,13):
        solution=x*y
        print ('\t', solution,   end=" ")
