
# Welcome to the Tic Tac Toe game 
# By Karabo Mamabolo

def sum(a, b, c):
    return a + b + c 

def printBoard(xState, yState):
    one = 'X'if xState[1] else ('O' if yState[1] else 1)
    two = 'X'if xState[2] else ('O' if yState[2] else 2)
    three = 'X'if xState[3] else ('O' if yState[3] else 3)
    four = 'X'if xState[4] else ('O' if yState[4] else 4)
    five = 'X'if xState[5] else ('O' if yState[5] else 5)
    six = 'X'if xState[6] else ('O' if yState[6] else 6)
    seven = 'X'if xState[7] else ('O' if yState[7] else 7)
    eight = 'X'if xState[8] else ('O' if yState[8] else 8)
    nine = 'X'if xState[9] else ('O' if yState[9] else 9)

    print(f"{one} | {two} | {three}")
    print(f"--+---+---")
    print(f"{four} | {five} | {six}")
    print(f"--+---+---")
    print(f"{seven} | {eight} | {nine}")
    



def checkWin(xState, yState):
    wins = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for win in wins:
        if(sum(xState[win[0]], xState[win[1]], xState[win[2]]) ==3):
            print('X is the winner!')
            return 1
        if(sum(yState[win[0]], yState[win[1]], yState[win[2]]) ==3):
            print('O is the winner!')
            return 0
    return -1

if __name__ == "__main__":
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    yState = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1 #1 for X  nbbcv  and 0 for O

    print()

    while(True):
        printBoard(xState, yState)
        print()
        if (turn == 1):
            value = int(input("X's turn to choose a square (1-9): "))
            print()
            xState[value] = 1
        else:
            value = int(input("O's turn to choose a square (1-9): "))
            print()
            yState[value] = 1
        cwin = checkWin(xState, yState)
        if (cwin != -1):
            print('Match Over')
            break

        turn = 1 - turn