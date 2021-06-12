'''
Tic Tac Toe game
Game Board:
   |   |  
---+---+---
   |   |
---+---+---
   |   |
'''
dict={1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' ',}

# for checking win and draw conditions
def checkwin():
    if(dict[1]==dict[2]==dict[3]!=' '): # Horizontal line
        return 1
    elif(dict[4]==dict[5]==dict[6]!=' '): # Horizontal line
        return 1
    elif(dict[7]==dict[8]==dict[9]!=' '): # Horizontal line
        return 1
    elif(dict[1]==dict[4]==dict[7]!=' '): # Vertical line
        return 1
    elif(dict[2]==dict[5]==dict[8]!=' '): # Vertical line
        return 1
    elif(dict[3]==dict[6]==dict[9]!=' '): # Vertical line
        return 1
    elif(dict[1]==dict[5]==dict[9]!=' '): # Diagnal line
        return 1
    elif(dict[3]==dict[5]==dict[7]!=' '): # Diagnal line
        return 1
    elif(dict[1]!=' ' and dict[2]!=' ' and dict[3]!=' ' and dict[4]!=' ' and dict[5]!=' ' and dict[6]!=' ' and dict[7]!=' ' and dict[8]!=' ' and dict[9]!=' '): # Draw
        return -1 # Draw
    else:
        return 0 #  To Continue

# for marking positions provided by the player 
def marking(position,turn):
    if(turn=='x'):
        if dict[position]==' ': # For checking if that postion is occupied or not
            dict[position]='x'
            return 1
        else:
            print("\nplace already occupied!! Please select empty box")
            return -1
    else:
        if dict[position]==' ': # For checking if that postion is occupied or not
            dict[position]='o'
            return 1
        else:
            print("place already occupied!! Please select empty box")
            return -1

# For printing the game board
def printboard(board):
    print(f" {board[1]} | {board[2]} | {board[3]}")
    print("---+---+---")
    print(f" {board[4]} | {board[5]} | {board[6]}")
    print("---+---+---")
    print(f" {board[7]} | {board[8]} | {board[9]}")
    
    
if __name__=='__main__':
    inc=1
    chkwin=0
    print("___Tic Tac toe___\n")
    print('''
    1 | 2 | 3
    ---+---+---
    4 | 5 | 6
    ---+---+---
    7 | 8 | 9
    ''')
    while(chkwin==0):
        val=inc%2 #logic for getting turns of both player alternatively
        if(val==1):
            turn="x" 
            input_from_user=int(input("turn of player X: "))
            occupied=marking(input_from_user,turn)
        else:
            turn="o"
            input_from_user=int(input("Turn of player O: "))
            occupied=marking(input_from_user,turn)

        printboard(dict)
        if occupied==1:
            inc+=1
        chkwin=checkwin()

        if chkwin==1:
            print(f"player {turn} won!!")

        elif chkwin==-1:
            print("Match Draw!!")
