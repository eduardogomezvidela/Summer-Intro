"""2) Sudoku"""

game = [[None, None, 4, None, None, 8, 5, None, 1],
                [None, None, None, None, 9, 5, None, 3, None],
                [None, None, None, 3, None, 1, None, 6, None],
                [None, 7, None, None, 8, None, 1, 4, None],
                [1, 6, 9, None, 3, None, 8, 2, 7],
                [None, 4, 8, None, 7, None, None, 5, None],
                [None, 9, None, 4, None, 7, None, None, None],
                [None, 5, None, 9, 1, None, None, None, None],
                [2, None, 6, 8, None, None, 7, None, None]]



def get_square(game,n): #Gets the square n from the sudoku
    
    square_list = []
    if n==1:
        for sub_row in range (0,3):
            for cell in range(3):
                square_list = square_list + [game[sub_row][cell]]
    if n==2:
        for sub_row in range (0,3):
            for cell in range(3,6):
                square_list = square_list + [game[sub_row][cell]]
    if n==3:
        for sub_row in range (0,3):
            for cell in range(6,9):
                square_list = square_list + [game[sub_row][cell]]
    if n==4:
        for sub_row in range (3,6):
            for cell in range(3):
                square_list = square_list + [game[sub_row][cell]]
    if n==5:
        for sub_row in range (3,6):
            for cell in range(3,6):
                square_list = square_list + [game[sub_row][cell]]
    if n==6:
        for sub_row in range (3,6):
            for cell in range(6,9):
                square_list = square_list + [game[sub_row][cell]]
    if n==7:
        for sub_row in range (6,9):
            for cell in range(3):
                square_list = square_list + [game[sub_row][cell]]
    if n==8:
        for sub_row in range (6,9):
            for cell in range(3,6):
                square_list = square_list + [game[sub_row][cell]]
    if n==9:
        for sub_row in range (6,9):
            for cell in range(6,9):
                square_list = square_list + [game[sub_row][cell]]
    return (square_list)



def check_square(game,square):  #Will check if a number is repeated in a square
    square = get_square(game,square)
    for i in range (1,10):
        if square.count(i) > 1:
            return False

    else:
        return True


    
def check_column(start, end, sub_list, list):
    for i in range (end):   #1- This iteration together with #2 go through each number in each column

        string = ''

        for sub_list in list: #2- This iteration together with #1 go through each number in each column
            if sub_list[i] != 0:
                string = string + str(sub_list[i])  #Puts all the numbers of a single columng into a string

        for number in string:   #Checks if there is a number repeated in the column
            if string.count(number) > 1 and number != 0:
                return False

        return True



def check_sudoku(list):

    columns = len(list)

    for sub_list in list:   #Iterate through each nested list in the list
        
        rows = len(sub_list)
        
        if rows != columns: #If sudoku is not a square
            print("sudoku not a square")
            return (False)

        for element in sub_list:    #Iterate through each number in a row

            if element == 0: #Ignores 0 elements (This will be useful for completing partially empty sudokus)
                do_nothing = 0

            elif sub_list.count(element) > 1 and type(sub_list.count(element)) == int : #If a number is repeated in the same row
                print("number repeated in row")
                return (False)

            elif element > columns: #If any number is larger than columns
                print("number larger than columns")
                return (False)

            for i in range (1,10):
                if check_square(game, i) == False:
                    print("number repeated in square", i)
                    return False

    if check_column(0,columns, sub_list, list) == False:    #Will check for repeated numbers from column (0) to column (columns)
        print("number repeated in column")
        return (False)

    return (True) #if our sudoku survives all the False filters it must be correct



print(check_sudoku([[1]]))
print(check_sudoku([[1, 2, 3], [2, 3, 1], [3, 1, 2]]))
print(check_sudoku([[1, 2, 3, 4], [2, 3, 1, 4], [4, 1, 2, 3], [3, 4, 1, 2]]))


print("----------------------")
#--------------------------------------------------------------##--------------------------------------------------------------##--------------------------------------------------------------#
#--------------------------------------------------------------##--------------------------------------------------------------##--------------------------------------------------------------#

"""2) A) check_complete_sudoku"""

game_completed = [[9, 3, 4, 2, 6, 8, 5, 7, 1],
                                        [6, 2, 1, 7, 9, 5, 4, 3, 8],
                                        [7, 8, 5, 3, 4, 1, 2, 6, 9],
                                        [5, 7, 2, 6, 8, 9, 1, 4, 3],
                                        [1, 6, 9, 5, 3, 4, 8, 2, 7],
                                        [3, 4, 8, 1, 7, 2, 9, 5, 6],
                                        [8, 9, 3, 4, 2, 7, 6, 1, 5],
                                        [4, 5, 7, 9, 1, 6, 3, 8, 2],
                                        [2, 1, 6, 8, 5, 3, 7, 9, 4]]



def square(game, start_rows, end_rows, start_columns, end_columns): #Checks if a number is repeated in each square
    
    square = []

    for list in game[start_rows:end_rows]:    #Square rows
        square = square + (list[start_columns:end_columns])   #Square columns
    for num in square:
        if square.count(num) > 1:
            return (False)

    return (True)



"""Should make a function to iterate through each square"""
def check_complete_sudoku(game):    #Goes through each square  
    game_completed = game
    if (square(game_completed, 0, 3, 0, 3)) == True and (square(game_completed, 0 , 3, 3, 6)) == True and (square(game_completed, 0 , 3, 6, 9)) == True:
        if (square(game_completed, 3, 6, 0, 3)) == True and (square(game_completed, 3 , 6, 3, 6)) == True and (square(game_completed, 3 , 6, 6, 9)) == True:
            if (square(game_completed, 6, 9, 0, 3)) == True and (square(game_completed, 6 , 9, 3, 6)) == True and (square(game_completed, 6 , 9, 6, 9)) == True:
                print(True)
            else:
                print(False)
        else:
            print(False)
    else:
        print(False)



check_complete_sudoku(game_completed)

game_completed[0][0] = 1
check_complete_sudoku(game_completed)

print("----------------------")
#--------------------------------------------------------------##--------------------------------------------------------------##--------------------------------------------------------------#
#--------------------------------------------------------------##--------------------------------------------------------------##--------------------------------------------------------------#

"""2) C) solve_sudoku"""



def print_sudoku(game):
        z = 0
        for sub_list in game:
            print(game[z])
            z=z+1
        print("-------")



print_sudoku(game)

for sub_row in game:    #Replaces None with 0
    for cell in sub_row:
        if cell == None:
            position = sub_row.index(cell)
            sub_row.pop(position)
            sub_row.insert(position,0)


print_sudoku(game)


"""
for sub_row in game:    #Iterates through entire sudoku
    for cell in sub_row:

        if cell == 0:   #Replaces 0 with 1 and checks
            position = sub_row.index(cell)
            sub_row.pop(position)
            sub_row.insert(position,1)

        print_sudoku(game)

        for i in range (2,10):  #Replaces number with  number+1 and checks
            
            if (check_sudoku(game)) == False:
                sub_row.pop(position)
                sub_row.insert(position,i)

            if i == 9 and check_sudoku(game) == False:
                print("TIME TO BACKTRACK!!!!!!!!!!!!!")
"""
for sub_row in game:    #Iterates through entire sudoku
    for cell in sub_row:

        if cell == 0:   #Replaces 0 with 1 and checks
            position = sub_row.index(cell)
            sub_row.pop(position)
            sub_row.insert(position,1)

        print_sudoku(game)

        #Get number

        for i in range (2,10):  #Replaces number with  number+1 and checks
            
            if (check_sudoku(game)) == False:
                sub_row.pop(position)
                sub_row.insert(position,i)

            if i == 9 and check_sudoku(game) == False:
                print("TIME TO BACKTRACK!!!!!!!!!!!!!")



"""if(check_sudoku(game)) == False:"""
            #Make cell 0, go back to previous cell and add 1 to it, check_sudoku

print_sudoku(game)

                
print("Square 1", get_square(game,1))
print("Square 2", get_square(game,2))
print("Square 3", get_square(game,3))
print("Square 4", get_square(game,4))
print("Square 5", get_square(game,5))
print("Square 6", get_square(game,6))
print("Square 7", get_square(game,7))
print("Square 8", get_square(game,8))
print("Square 9", get_square(game,9))

print("-------")

for i in range (1,10):
    print("CHECK", i,  check_square(game,i))
