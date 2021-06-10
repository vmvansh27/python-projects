'''
   |   |  
---+---+---
   |   |
---+---+---
   |   |
'''
dict={1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' ',}

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
    elif(dict[1]!=dict[2]!=dict[3]!=dict[4]!=dict[5]!=dict[6]!=dict[7]!=dict[8]!=dict[9]): # Draw
        return -1
    else:
        return 0 # Continue


def marking(position,turn):
    if(turn=='x'):
        if dict[position]==' ': # For checking if that postion is occupied or not
            dict[position]='x'
    else:
        if dict[position]==' ': # For checking if that postion is occupied or not
            dict[position]='o'


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
    printboard(dict)
    while(chkwin==0):
        val=inc%2
        if(val==1):
            turn="x"
            input_from_user=int(input("turn of player X: "))
            marking(input_from_user,turn)
        else:
            turn="o"
            input_from_user=int(input("Turn of player O: "))
            marking(input_from_user,turn)
        inc+=1

        printboard(dict)
        chkwin=checkwin()

        if chkwin==1:
            print(f"player {turn} won!!")

        elif chkwin==-1:
            print("Match Draw!!")


        



