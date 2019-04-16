
columns = [] #Array used to store board
whosTurn = 'W' #Holds 'W' if whites turn and 'B' if Blacks turn
invalidMove = False #Holds true if whole move is invalid else True
validCoords = False #Holds true if inputCoords, outputCoords and specific piece move is valid
gameOver = False #Holds True if Checkmate or player quits, used to terminate game loop


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


def movepiece(moveFrom, moveTo):
    for i in range(8):
        for j in range(8):
            if i == int(moveFrom[:1]) and j == int(moveFrom[2:]):
                columns[int(moveTo[:1])][int(moveTo[2:])] = columns[i][j]
                columns[i][j] = "  "


"""If inputCoords are between 0 and 7 call validsquaretomoveto(moveFrom, moveTO) else return False"""


def isThisAValidmove(moveFrom, moveTo):
    if int(moveFrom[:1]) >= 0 and int(moveFrom[:1]) < 8 and int(moveFrom[2:]) >= 0 and int(moveFrom[2:]) < 8:
        if (columns[int(moveFrom[:1])][int(moveFrom[2:])])[:1] == whosTurn:
            return validsquaretomoveto(moveFrom, moveTo)
        else:
            print("Please select one of your own pieces")
            return False
    else:
        print("Please select a piece on the board")
        return False


"""If outputCoords are between 0 and 7 and not your own piece call specific piece move, else return False"""


def validsquaretomoveto(moveFrom, moveTo):
    if int(moveTo[:1]) >= 0 and int(moveTo[:1])< 8 and  int(moveTo[2:]) >= 0 and int(moveTo[2:])< 8:
        if (columns[int(moveTo[:1])][int(moveTo[2:])])[:1] == whosTurn:
            print("Cannot move to a square with your own piece already on it")
            return False
        else:
            if (columns[int(moveFrom[:1])][int(moveFrom[2:])])[1:] == "R":
                return rookValidMove(moveFrom, moveTo)
            elif(columns[int(moveFrom[:1])][int(moveFrom[2:])])[1:] == "N":
                return knightValidMove(moveFrom, moveTo)
            elif (columns[int(moveFrom[:1])][int(moveFrom[2:])])[1:] == "B":
                return bishopValidMove(moveFrom, moveTo)
            elif (columns[int(moveFrom[:1])][int(moveFrom[2:])])[1:] == "Q":
                return queenValidMove(moveFrom, moveTo)
            elif (columns[int(moveFrom[:1])][int(moveFrom[2:])])[1:] == "K":
                return kingValidMove(moveFrom, moveTo)
            elif (columns[int(moveFrom[:1])][int(moveFrom[2:])])[1:] == "P":
                return pawnValidMove(moveFrom, moveTo)
    else:
        print("Cannot move to a square off the board")
        return False


"""If move is valid for a rook call nothingInTheWay(moveFrom, moveTo), else return False"""


def rookValidMove(moveFrom, moveTo):
    if int(moveTo[:1]) == int(moveFrom[:1]) >= 0 or int(moveTo[2:]) == int(moveFrom[2:]):
        return nothingInTheWay(moveFrom, moveTo)
    else:
        return False


"""If move is valid for a King return True else return False"""


def kingValidMove(moveFrom, moveTo):
    if abs(int(moveTo[:1]) - int(moveFrom[:1])) >= 0 and abs(int(moveTo[:1]) - int(moveFrom[:1])) < 2:
        if abs(int(moveTo[2:]) - int(moveFrom[2:])) >= 0 and abs(int(moveTo[2:]) - int(moveFrom[2:])) < 2:
            return True
        else:
            return False
    else:
        return False


"""If move is valid for a Knight return True else return False"""


def knightValidMove(moveFrom, moveTo):
    if abs(int(moveTo[:1]) - int(moveFrom[:1])) == 1 and abs(int(moveTo[2:]) - int(moveFrom[2:])) == 2:
        return True
    elif abs(int(moveTo[:1]) - int(moveFrom[:1])) == 2 and abs(int(moveTo[2:]) - int(moveFrom[2:])) == 1:
        return True
    else:
        return False


"""If move is valid for a Bishop call nothingInTheWay(moveFrom, moveTo), else return False"""


def bishopValidMove(moveFrom, moveTo):
    if abs(int(moveTo[:1]) - int(moveFrom[:1])) == abs(int(moveTo[2:]) - int(moveFrom[2:])):
        return nothingInTheWay(moveFrom, moveTo)
    else:
        return False


"""Queens can move the same as rooks and bishops combined so if either is valid then queen is a valid move, else return False"""


def queenValidMove(moveFrom, moveTo):
    if bishopValidMove(moveFrom, moveTo) or rookValidMove(moveFrom, moveTo):
        return True
    else:
        return False


"""If move is valid for a pawn return True else return False"""


def pawnValidMove(moveFrom, moveTo):
    if whosTurn == 'W':
        if int(moveFrom[:1]) == 1:
            if int(moveTo[2:]) == int(moveFrom[2:]):
                """"Check for white pawn making initial move"""
                if (int(moveTo[:1]) - int(moveFrom[:1]) == 1 or int(moveTo[:1]) - int(moveFrom[:1]) == 2) and columns[int(moveTo[:1])][int(moveTo[2:])][:1] != 'B':
                    return True
                else:
                    return False
            else:
                """Allow White pawn to take black pawn in initial move"""
                if int(moveTo[:1]) == 2 and abs(int(moveTo[2:]) - int(moveFrom[2:])) == 1:
                    if columns[int(moveTo[:1])][int(moveTo[2:])][:1] == "B":
                        return True
                    else:
                        return False
                else:
                    return False
        else:
            """Check for White pawn moving forward a square after initial move"""
            if int(moveTo[2:]) == int(moveFrom[2:]):
                if int(moveTo[:1]) - int(moveFrom[:1]) == 1 and columns[int(moveTo[:1])][int(moveTo[2:])][:1] != "B":
                    return True
                else:
                    return False
            else:
                """Check for White pawn taking piece after initial move"""
                if int(moveTo[:1]) == int(moveFrom[:1]) + 1 and abs(int(moveTo[2:]) - int(moveFrom[2:])) == 1:
                    if columns[int(moveTo[:1])][int(moveTo[2:])][:1] == "B":
                        return True
                    else:
                        return False
                else:
                    return False
    else:
        """Same as above but for black pawns"""
        if int(moveFrom[:1]) == 6:
            if int(moveTo[2:]) == int(moveFrom[2:]):
                if (int(moveTo[:1]) - int(moveFrom[:1]) == -1 or int(moveTo[:1]) - int(moveFrom[:1]) == -2) and columns[int(moveTo[:1])][int(moveTo[2:])][:1] != 'W':
                    return True
                else:
                    return False
            else:
                if int(moveTo[:1]) == 5 and abs(int(moveTo[2:]) - int(moveFrom[2:])) == 1:
                    if columns[int(moveTo[:1])][int(moveTo[2:])][:1] == "W":
                        return True
                    else:
                        return False
                else:
                    return False
        else:
            if int(moveTo[2:]) == int(moveFrom[2:]):
                if int(moveTo[:1]) - int(moveFrom[:1]) == -1 and columns[int(moveTo[:1])][int(moveTo[2:])][:1] != 'W':
                    return True
                else:
                    return False
            else:
                if int(moveTo[:1]) == int(moveFrom[:1]) - 1 and abs(int(moveTo[2:]) - int(moveFrom[2:])) == 1:
                    if columns[int(moveTo[:1])][int(moveTo[2:])][:1] == "W":
                        return True
                    else:
                        return False
                else:
                    return False


"""This routine checks that their is no piece inbetween the start square and destination square for a rook, bishop or queen"""


def nothingInTheWay(moveFrom, moveTo):
    if moveFrom[:1] == moveTo[:1]:
        if int(moveFrom[2:]) > int(moveTo[2:]):
            for i in range((int(moveFrom[2:]) - int(moveTo[2:])) - 1):
                if columns[int(moveFrom[:1])][int(moveFrom[2:]) - (i + 1)] != "  ":
                    return False
            return True
        else:
            for i in range((int(moveTo[2:]) - int(moveFrom[2:])) - 1):
                if columns[int(moveFrom[:1])][int(moveFrom[2:]) + (i + 1)] != "  ":
                    return False
            return True
    elif moveFrom[2:] == moveTo[2:]:
        if int(moveFrom[:1]) > int(moveTo[:1]):
            for i in range((int(moveFrom[:1]) - int(moveTo[:1])) - 1):
                if columns[int(moveFrom[:1]) - (i + 1)][int(moveFrom[2:])] != "  ":
                    return False
            return True
        else:
            for i in range((int(moveTo[:1]) - int(moveFrom[:1])) - 1):
                if columns[int(moveFrom[:1]) + (i + 1)][int(moveFrom[2:])] != "  ":
                    return False
            return True
    else:
        if int(moveFrom[:1]) > int(moveTo[:1]) and int(moveFrom[2:]) > int(moveTo[2:]):
            for i in range((int(moveTo[:1]) - int(moveFrom[:1])) - 1):
                if columns[int(moveFrom[:1]) - (i + 1)][int(moveFrom[2:]) - (i + 1)] != "  ":
                    return False
            return True
        elif int(moveFrom[:1]) < int(moveTo[:1]) and int(moveFrom[2:]) > int(moveTo[2:]):
            for i in range((int(moveFrom[:1]) - int(moveTo[:1])) - 1):
                if columns[int(moveFrom[:1]) - (i + 1)][int(moveFrom[2:]) + (i + 1)] != "  ":
                    return False
            return True
        elif int(moveFrom[:1]) < int(moveTo[:1]) and int(moveFrom[2:]) < int(moveTo[2:]):
            for i in range((int(moveTo[:1]) - int(moveFrom[:1])) - 1):
                if columns[int(moveFrom[:1]) + (i + 1)][int(moveFrom[2:]) + (i + 1)] != "  ":
                    return False
            return True
        else:
            for i in range((int(moveFrom[:1]) - int(moveTo[:1])) - 1):
                if columns[int(moveTo[:1]) + (i + 1)][int(moveTo[2:]) - (i + 1)] != "  ":
                    return False
            return True


"""This routine simply undoes the last move by switching the pieces in the board array"""

def undoLastMove():
    columns[int(moveFrom[:1])][int(moveFrom[2:])] = columns[int(moveTo[:1])][int(moveTo[2:])]
    columns[int(moveTo[:1])][int(moveTo[2:])] = "  "


"""This routine checks that if by making your move will you put yourself in check, if so return True"""
"""makeMove is called before this routine but after valid coordinates have been given"""


def amIInCheck():
    global invalidMove
    global whosTurn

    inCheckFlag = False
    kingX = 0
    kingY = 0


    """Get position coordinaes of your king"""

    for i in range(8):
        for j in range(8):
            if columns[i][j][:1] == whosTurn and columns[i][j][1:] == "K":
                kingX = j
                kingY = i

    if whosTurn == 'W':
        whosTurn = 'B'
    else:
        whosTurn = 'W'

    invalidMove = False

    """Change whos turn it is and see if any of their pieces have a valid move to your King, if so set Flag"""

    for i in range(8):
        for j in range(8):
            if columns[i][j][:1] == whosTurn:
                invalidMove = isThisAValidmove(str(i) + "," + str(j), str(kingY) + "," + str(kingX))
                if invalidMove == True:
                    inCheckFlag = True


    """Change whos turn it is back"""

    if whosTurn == 'W':
        whosTurn = 'B'
    else:
        whosTurn = 'W'


    """If Flag set then You are in check and this is therefore an invalid move and Return False"""


    if inCheckFlag == True:
        print("YOU ARE IN CHECK")
        return False
    else:
        print("\n YOU ARE NOT IN CHECK \n")
        return True


def inCheck():
    global invalidMove

    kingX = 0
    kingY = 0
    attackingPieces = 0

    """Get coordinates of opponents King"""

    for i in range(8):
        for j in range(8):
            if columns[i][j][:1] != whosTurn and columns[i][j][:1] != " " and columns[i][j][1:] == "K":
                kingX = j
                kingY = i

    """If opponents King is a valid move for any of your pieces add one to attackingPieces"""

    for i in range(8):
        for j in range(8):
            if columns[i][j][:1] == whosTurn:
                invalidMove = isThisAValidmove(str(i) + "," + str(j), str(kingY) + "," + str(kingX))
                if invalidMove:
                    attackingPieces = attackingPieces + 1

    if attackingPieces > 0:
        """ return inCheckMate(kingY, kingX, attackingPieces)"""
        print("\nCHECK\n")
    else:
        return False


def createListOfSpacesInBetween2Pieces(moveFrom, moveTo):
    spacesInBetween = []

    if moveFrom[:1] == moveTo[:1]:
        if int(moveFrom[2:]) > int(moveTo[2:]):
            for i in range((int(moveFrom[2:]) - int(moveTo[2:])) - 1):
                spacesInBetween.append(columns[int(moveFrom[:1])][moveFrom[2:] - (i + 1)])
        else:
            for i in range((int(moveTo[2:]) - int(moveFrom[2:])) - 1):
                spacesInBetween.append(columns[int(moveFrom[:1])][moveFrom[2:] + (i + 1)])
    elif moveFrom[2:] == moveTo[2:]:
        if int(moveFrom[:1]) > int(moveTo[:1]):
            for i in range((int(moveFrom[:1]) - int(moveTo[:1])) - 1):
                spacesInBetween.append(columns[int(moveFrom[:1]) - (i + 1)][int(moveFrom[2:])])
        else:
            for i in range((int(moveTo[:1]) - int(moveFrom[:1])) - 1):
                spacesInBetween.append(columns[int(moveFrom[:1]) + (i + 1)][int(moveFrom[2:])])
    else:
        if int(moveFrom[:1]) > int(moveTo[:1]) and int(moveFrom[2:]) > int(moveTo[2:]):
            for i in range((int(moveTo[:1]) - int(moveFrom[:1])) - 1):
                spacesInBetween.append(columns[int(moveFrom[:1]) - (i + 1)][int(moveFrom[2:]) - (i + 1)])
        elif int(moveFrom[:1]) < int(moveTo[:1]) and int(moveFrom[2:]) > int(moveTo[2:]):
            for i in range((int(moveFrom[:1]) - int(moveTo[:1])) - 1):
                spacesInBetween.append(columns[int(moveFrom[:1]) - (i + 1)][int(moveFrom[2:]) + (i + 1)])
        elif int(moveFrom[:1]) < int(moveTo[:1]) and int(moveFrom[2:]) < int(moveTo[2:]):
            for i in range((int(moveTo[:1]) - int(moveFrom[:1])) - 1):
                spacesInBetween.append(columns[int(moveFrom[:1]) + (i + 1)][int(moveFrom[2:]) + (i + 1)])
        else:
            for i in range((int(moveFrom[:1]) - int(moveTo[:1])) - 1):
                spacesInBetween.append(columns[int(moveTo[:1]) + (i + 1)][int(moveTo[2:]) - (i + 1)])
    return spacesInBetween


def inCheckMate(kingY, kingX, attackingPieces):
        # Has king any vaild moves
        # Can the attacking piece be blocked
        # Can the attacking piece be taken
        # Need attacking piece Square coordinates

        global whosTurn

        if whosTurn =='W':
            whosTurn = 'B'
        else:
            whosTurn = 'W'

        for i in range(3):
            if isThisAValidmove(str(kingY) + "," + str(kingX), str(kingY) + "," + str(kingX + (i - 1))):
                return False

        for i in range(3):
            if isThisAValidmove(str(kingY) + "," + str(kingX), str(kingY + 1) + "," + str(kingX + (i - 1))):
                return False

        for i in range(3):
            if isThisAValidmove(str(kingY) + "," + str(kingX), str(kingY - 1) + "," + str(kingX + (i - 1))):
                return False

        if attackingPieces == 1:
            for i in range(8):
                if validMove:
                    return False
                for j in range(8):
                    validMove = isThisAValidmove(str(i) + "," + str(j), moveTo)
                    if validMove:
                        return False

        #if NOT validMove:
        createListOfSpacesInBetween2Pieces(moveFrom, str(kingY) + "," + str(kingX))
        # can I block
        # call valid move for every piece to every square in between

        if whosTurn == 'W':
            whosTurn = 'B'
        else:
            whosTurn = 'W'

        if validMove:
            print("\n NOT CHECKMATE \n")
            return False
        else:
            print("\n CHECKMATE GAME OVER " + whosTurn + " WINS \n")
            return True


initialiseboard()
drawboard()

while gameOver == False:
    if whosTurn == 'W':
        print("\n WHITE'S TURN \n")
    else:
        print("\n BLACK'S TURN \n")

    while invalidMove == False:
        while validCoords == False:
            moveFrom = input("Please enter the coordinates of the piece you are moving, row first, eg. 3,4 \n")
            moveTo = input("Please enter the coordinates of where you wish to move to, row first, eg. 5,4 \n")
            validCoords = isThisAValidmove(moveFrom, moveTo)

        movepiece(moveFrom, moveTo)
        invalidMove = amIInCheck()
        if invalidMove == False:
            validCoords = False
            undoLastMove()

    invalidMove = False
    validCoords = False
    #Clear spaces in between list

    inCheck()
    #Check if opposition is in check
    #If so check Checkmate

    drawboard()
    if whosTurn == 'W':
        whosTurn = 'B'
    else:
        whosTurn = 'W'