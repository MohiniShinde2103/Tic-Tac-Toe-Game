#Implementation of Two Player Tic-Tac-Toe game in Python.

theBoard = {'1': ' ' , '2': ' ' , '3': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '7': ' ' , '8': ' ' , '9': ' ' }

board_keys = []

for key in theBoard:
    board_keys.append(key)

def printBoard(board):
    print("\n")
    print('           '+board['1'] + ' | ' + board['2'] + ' | ' + board['3'])
    print('          ---+---+---')
    print('           '+board['4'] + ' | ' + board['5'] + ' | ' + board['6'])
    print('          ---+---+---')
    print('           '+board['7'] + ' | ' + board['8'] + ' | ' + board['9'])
    print("\n")

# Now we'll write the main function which has all the gameplay functionality.
def game():

    turn = 'X'
    count = 0


    for i in range(10):
        printBoard(theBoard)
        move=input("It's your turn," + turn + ". Move to which place?   ")
            
        #move = input()        

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("THAT PLACE IS ALREADY FILLED.\nMove to which place?")
            continue

        # Now we will check if player X or O has won,for every move after 5 moves. 
        if count >= 5:
            if theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': # across the top
                printBoard(theBoard)
                print("\nGAME OVER.\n\n")                
                print(" ****** CONGRATULATIONS!  " +turn + " YOU WON THE GAME ******\n\n")                
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': # across the middle
                printBoard(theBoard)
                print("\nGAME OVER.\n\n")
                print(" ****** CONGRATULATIONS!  " +turn + " YOU WON THE GAME ******\n\n") 
                break
            elif theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': # across the bottom
                printBoard(theBoard)
                print("\nGAME OVER.\n\n")                
                print(" ****** CONGRATULATIONS!  " +turn + " YOU WON THE GAME ******\n\n") 
                break
            elif theBoard['7'] == theBoard['4'] == theBoard['1'] != ' ': # down the left side
                printBoard(theBoard)
                print("\nGAME OVER.\n\n")                
                print(" ****** CONGRATULATIONS!  " +turn + " YOU WON THE GAME ******\n\n") 
                break
            elif theBoard['8'] == theBoard['5'] == theBoard['2'] != ' ': # down the middle
                printBoard(theBoard)
                print("\nGAME OVER.\n\n")                
                print(" ****** CONGRATULATIONS!  " +turn + " YOU WON THE GAME ******\n\n") 
                break
            elif theBoard['9'] == theBoard['6'] == theBoard['3'] != ' ': # down the right side
                printBoard(theBoard)
                print("\nGAME OVER.\n\n")                
                print(" ****** CONGRATULATIONS!  " +turn + " YOU WON THE GAME ******\n\n") 
                break 
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': # diagonal
                printBoard(theBoard)
                print("\nGAME OVER.\n\n")                
                print(" ****** CONGRATULATIONS!  " +turn + " YOU WON THE GAME ******\n\n") 
                break
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': # diagonal
                printBoard(theBoard)
                print("\nGAME OVER.\n\n")                
                print(" ****** CONGRATULATIONS!  " +turn + " YOU WON THE GAME ******\n\n") 
                break 

        # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == 9:
            print("\nGAME OVER.\n\n")                
            print("***  IT'S A TIE!!  ***\n\n")
            break

        # Now we have to change the player after every move.
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    
    # Now we will ask if player wants to restart the game or not.
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":  
        for key in board_keys:
            theBoard[key] = " "

        game()

if __name__ == "__main__":
    game()
