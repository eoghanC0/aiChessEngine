
columns = []
whosTurn = 'W'
validMove = False
gameOver = False

""" Create an 8*8 array for the board and then fill the correct squares with the pieces according to the row and column
   W = white
   B = Black
   R = Rook 
   N = Knight
   B = Bishop
   K = King
   Q = Queen"""


def initialiseboard():
    for i in range(8):
        rows = []
        for j in range(8):
            if i == 0:
                if j == 0:
                    rows.append("WR")
                elif j == 1:
                    rows.append("WN")
                elif j == 2:
                    rows.append("WB")
                elif j == 3:
                    rows.append("WK")
                elif j == 4:
                    rows.append("WQ")
                elif j == 5:
                    rows.append("WB")
                elif j == 6:
                    rows.append("WN")
                elif j == 7:
                    rows.append("WR")
            elif i == 1:
                rows.append("WP")
            elif i == 7:
                if j == 0:
                    rows.append("BR")
                elif j == 1:
                    rows.append("BN")
                elif j == 2:
                    rows.append("BB")
                elif j == 3:
                    rows.append("BK")
                elif j == 4:
                    rows.append("BQ")
                elif j == 5:
                    rows.append("BB")
                elif j == 6:
                    rows.append("BN")
                elif j == 7:
                    rows.append("BR")
            elif i == 6:
                rows.append("BP")
            else:
                rows.append("  ")
        columns.append(rows)


"""Loop through each element of the 2D array, board, and print to screen with row and column numbers"""


def drawboard():
    for i in range(8):
        if i != 7:
            print("      " + str(i), end="")
        else:
            print("      " + str(i) + "\n")

    for i in range(8):
        print(str(i) + "    ", end="")
        for j in range(8):
            if j != 7:
                print(columns[i][j] + "     ", end="")
            else:
                print(columns[i][j] + "    " + "\n")


"""Move the piece the user selected to where they want to go in the board array"""


def movepiece():

    for i in range(8):
        for j in range(8):
            if i == int(inputCoordinates[:1]) and j == int(inputCoordinates[2:]):
                columns[int(outputCoordinates[:1])][int(outputCoordinates[2:])] = columns[i][j]
                columns[i][j] = "  "


def validmove():
    global validMove
    global inputCoordinates
    global outputCoordinates

    validMove = False
    while validMove == False:
        validMove = True
        if int(inputCoordinates[:1]) >= 0 and int(inputCoordinates[:1]) < 8 and int(inputCoordinates[2:]) >= 0 and int(inputCoordinates[2:]) < 8:
            if (columns[int(inputCoordinates[:1])][int(inputCoordinates[2:])])[:1] == whosTurn:
                validMove = validsquaretomoveto()
            else:
                print("Please select one of your own pieces")
                validMove = False
        else:
            print("Please select a piece on the board")
            validMove = False
        if validMove == False:
            inputCoordinates = input("Please enter the coordinates of the piece you are moving, row first, eg. 3,4 \n")
            outputCoordinates = input("Please enter the coordinates of where you wish to move to, row first, eg. 5,4 \n")


def validsquaretomoveto():
    global validMove
    global outputCoordinates
    global inputCoordinates

    if int(outputCoordinates[:1]) >= 0 and int(outputCoordinates[:1])< 8 and  int(outputCoordinates[2:]) >= 0 and int(outputCoordinates[2:])< 8:
        if (columns[int(outputCoordinates[:1])][int(outputCoordinates[2:])])[:1] == whosTurn:
            print("Cannot move to a square with your own piece already on it")
            return False
        else:
            if (columns[int(inputCoordinates[:1])][int(inputCoordinates[2:])])[1:] == "R":
                validMove = rookValidMove()
            elif(columns[int(inputCoordinates[:1])][int(inputCoordinates[2:])])[1:] == "N":
                validMove = knightValidMove()
            elif (columns[int(inputCoordinates[:1])][int(inputCoordinates[2:])])[1:] == "B":
                validMove = bishopValidMove()
            elif (columns[int(inputCoordinates[:1])][int(inputCoordinates[2:])])[1:] == "Q":
                validMove = queenValidMove()
            elif (columns[int(inputCoordinates[:1])][int(inputCoordinates[2:])])[1:] == "K":
                validMove = kingValidMove()
            elif (columns[int(inputCoordinates[:1])][int(inputCoordinates[2:])])[1:] == "P":
                validMove = pawnValidMove()
    else:
        print("Cannot move to a square off the board")
        return False
    return validMove


def rookValidMove():
    if int(outputCoordinates[:1]) == int(inputCoordinates[:1]) >= 0 or int(outputCoordinates[2:]) == int(inputCoordinates[2:]):
        return nothingInTheWay()
    else:
        return False


def kingValidMove():
    if abs(int(outputCoordinates[:1]) - int(inputCoordinates[:1])) >= 0 and abs(int(outputCoordinates[:1]) - int(inputCoordinates[:1])) < 2:
        if abs(int(outputCoordinates[2:]) - int(inputCoordinates[2:])) >= 0 and abs(int(outputCoordinates[2:]) - int(inputCoordinates[2:])) < 2:
            return True
        else:
            return False
    else:
        return False


def knightValidMove():
    if abs(int(outputCoordinates[:1]) - int(inputCoordinates[:1])) == 1 and abs(int(outputCoordinates[2:]) - int(inputCoordinates[2:])) == 2:
        return True
    elif abs(int(outputCoordinates[:1]) - int(inputCoordinates[:1])) == 2 and abs(int(outputCoordinates[2:]) - int(inputCoordinates[2:])) == 1:
        return True
    else:
        return False


def bishopValidMove():
    if abs(int(outputCoordinates[:1]) - int(inputCoordinates[:1])) == abs(int(outputCoordinates[2:]) - int(inputCoordinates[2:])):
        return nothingInTheWay()
    else:
        return False


def queenValidMove():
    if bishopValidMove() or rookValidMove():
        return True
    else:
        return False

def pawnValidMove():
    if whosTurn == 'W':
        if int(inputCoordinates[:1]) == 1:
            if int(outputCoordinates[2:]) == int(inputCoordinates[2:]):
                if (int(outputCoordinates[:1]) - int(inputCoordinates[:1]) == 1 or int(outputCoordinates[:1]) - int(inputCoordinates[:1]) == 2) and columns[int(outputCoordinates[:1])][int(outputCoordinates[2:])][:1] != 'B':
                    return True
                else:
                    return False
            else:
                if int(outputCoordinates[:1]) == 2 and abs(int(outputCoordinates[2:]) - int(inputCoordinates[2:])) == 1:
                    if columns[int(outputCoordinates[:1])][int(outputCoordinates[2:])][:1] == "B":
                        return True
                    else:
                        return False
                else:
                    return False
        else:
            if int(outputCoordinates[2:]) == int(inputCoordinates[2:]):
                if int(outputCoordinates[:1]) - int(inputCoordinates[:1]) == 1 and columns[int(outputCoordinates[:1])][int(outputCoordinates[2:])][:1] != "B":
                    return True
                else:
                    return False
            else:
                if int(outputCoordinates[:1]) == int(inputCoordinates[:1]) + 1 and abs(int(outputCoordinates[2:]) - int(inputCoordinates[2:])) == 1:
                    if columns[int(outputCoordinates[:1])][int(outputCoordinates[2:])][:1] == "B":
                        return True
                    else:
                        return False
                else:
                    return False
    else:
        if int(inputCoordinates[:1]) == 6:
            if int(outputCoordinates[2:]) == int(inputCoordinates[2:]):
                if (int(outputCoordinates[:1]) - int(inputCoordinates[:1]) == -1 or int(outputCoordinates[:1]) - int(inputCoordinates[:1]) == -2) and columns[int(outputCoordinates[:1])][int(outputCoordinates[2:])][:1] != 'W':
                    return True
                else:
                    return False
            else:
                if int(outputCoordinates[:1]) == 5 and abs(int(outputCoordinates[2:]) - int(inputCoordinates[2:])) == 1:
                    if columns[int(outputCoordinates[:1])][int(outputCoordinates[2:])][:1] == "W":
                        return True
                    else:
                        return False
                else:
                    return False
        else:
            if int(outputCoordinates[2:]) == int(inputCoordinates[2:]):
                if int(outputCoordinates[:1]) - int(inputCoordinates[:1]) == -1 and columns[int(outputCoordinates[:1])][int(outputCoordinates[2:])][:1] != 'W':
                    return True
                else:
                    return False
            else:
                if int(outputCoordinates[:1]) == int(inputCoordinates[:1]) - 1 and abs(int(outputCoordinates[2:]) - int(inputCoordinates[2:])) == 1:
                    if columns[int(outputCoordinates[:1])][int(outputCoordinates[2:])][:1] == "W":
                        return True
                    else:
                        return False
                else:
                    return False


def nothingInTheWay():
    if inputCoordinates[:1] == outputCoordinates[:1]:
        if int(inputCoordinates[2:]) > int(outputCoordinates[2:]):
            for i in range((int(inputCoordinates[2:]) - int(outputCoordinates[2:])) - 1):
                if columns[int(inputCoordinates[:1])][inputCoordinates[2:] - (i + 1)] != "  ":
                    return False
            return True
        else:
            for i in range((int(outputCoordinates[2:]) - int(inputCoordinates[2:])) - 1):
                if columns[int(inputCoordinates[:1])][inputCoordinates[2:] + (i + 1)] != "  ":
                    return False
            return True
    elif inputCoordinates[2:] == outputCoordinates[2:]:
        if int(inputCoordinates[:1]) > int(outputCoordinates[:1]):
            for i in range((int(inputCoordinates[:1]) - int(outputCoordinates[:1])) -1):
                if columns[int(inputCoordinates[:1]) - (i + 1)][int(inputCoordinates[2:])] != "  ":
                    return False
            return True
        else:
            for i in range((int(outputCoordinates[:1]) - int(inputCoordinates[:1])) - 1):
                if columns[int(inputCoordinates[:1]) + (i + 1)][int(inputCoordinates[2:])] != "  ":
                    return False
            return True
    else:
        if int(inputCoordinates[:1]) > int(outputCoordinates[:1]) and int(inputCoordinates[2:]) > int(outputCoordinates[2:]):
            for i in range((int(outputCoordinates[:1]) - inputCoordinates[:1]) - 1):
                if columns[int(inputCoordinates[:1]) - (i + 1)][int(inputCoordinates[2:]) - (i + 1)] != "  ":
                    return False
            return True
        elif int(inputCoordinates[:1]) < int(outputCoordinates[:1]) and int(inputCoordinates[2:]) > int(outputCoordinates[2:]):
            for i in range((int(inputCoordinates[:1]) - int(outputCoordinates[:1])) - 1):
                if columns[int(inputCoordinates[:1]) - (i + 1)][int(inputCoordinates[2:]) + (i + 1)] != "  ":
                    return False
            return True
        elif int(inputCoordinates[:1]) < int(outputCoordinates[:1]) and int(inputCoordinates[2:]) < int(outputCoordinates[2:]):
            for i in range((int(outputCoordinates[:1]) - int(inputCoordinates[:1])) - 1):
                if columns[int(inputCoordinates[:1]) + (i + 1)][int(inputCoordinates[2:]) + (i + 1)] != "  ":
                    return False
            return True
        else:
            for i in range((int(inputCoordinates[:1]) - int(outputCoordinates[:1])) - 1):
                if columns[int(outputCoordinates[:1]) + (i + 1)][int(outputCoordinates[2:]) - (i + 1)] != "  ":
                    return False
            return True

initialiseboard()
drawboard()

while gameOver == False:
    if whosTurn == 'W':
        print("\n WHITE'S TURN \n")
    else:
        print("\n BLACK'S TURN \n")

    print("Enter 'q' to quit : ")
    inputCoordinates = input("Please enter the coordinates of the piece you are moving, row first, eg. 3,4 \n")
    outputCoordinates = input("Please enter the coordinates of where you wish to move to, row first, eg. 5,4 \n")

    if inputCoordinates == 'q':
        gameOver = True
    validmove()
    movepiece()
    drawboard()
    if whosTurn == 'W':
        whosTurn = 'B'
    else:
        whosTurn = 'W'