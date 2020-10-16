import random

Board = []  # Array used to store board
whosTurn = 'W'  # Holds 'W' if whites turn and 'B' if Blacks turn
validmove = False  # Holds false if whole move is inf Checkmate or player q valid else True
gameOver = False  # Holds True i uits, used to terminate game loop
validCoords = False
castled = False
checkincheck = False
castlingallowed = 0b00000000
errormessage = ""
movetopiece = "  "

""" Create an 8*8 array for the board and then fill the correct squares with the pieces according to the row and Board 
   W = white    
  b = Black    
  R = Rook     
  N = Knight   
  B = Bishop   
  K = King    
  Q = Queen"""


def initialiseboard():
    for i in range(8):
        rows = []
        for j in range(8):
            if j == 1:
                rows.append("WP")
            elif j == 6:
                rows.append("bp")
            if i == 0 or i == 7:
                if j == 0:
                    rows.append("WR")
                elif j == 7:
                    rows.append("br")
            if i == 1 or i == 6:
                if j == 0:
                    rows.append("WN")
                elif j == 7:
                    rows.append("bn")
            if i == 2 or i == 5:
                if j == 0:
                    rows.append("WB")
                elif j == 7:
                    rows.append("bb")
            if i == 3:
                if j == 0:
                    rows.append("WQ")
                elif j == 7:
                    rows.append("bq")
            if i == 4:
                if j == 0:
                    rows.append("WK")
                elif j == 7:
                    rows.append("bk")
            if j != 0 and j != 5 and j != 6 and j != 7:
                rows.append("  ")
        Board.append(rows)


def testinitialiseboardcastleing():
    for i in range(8):
        rows = []
        for j in range(8):
            if j == 1:
                rows.append("WP")
            elif j == 6:
                rows.append("bp")
            if i == 0 or i == 7:
                if j == 0:
                    rows.append("WR")
                elif j == 7:
                    rows.append("br")
            if i == 1 or i == 6:
                if j == 0:
                    rows.append("  ")
                elif j == 7:
                    rows.append("bn")
            if i == 2 or i == 5:
                if j == 0:
                    rows.append("  ")
                elif j == 7:
                    rows.append("bb")
            if i == 3:
                if j == 0:
                    rows.append("WQ")
                elif j == 7:
                    rows.append("bq")
            if i == 4:
                if j == 0:
                    rows.append("WK")
                elif j == 7:
                    rows.append("bk")
            if j != 0 and j != 5 and j != 6 and j != 7:
                rows.append("  ")
        Board.append(rows)


def testinitialiseboardpawnpromotion():
    for i in range(8):
        rows = []
        for j in range(8):
            if j == 2:
                rows.append("bp")
            elif j == 6:
                rows.append("WP")
            if i == 0 or i == 7:
                if j == 0:
                    rows.append("  ")
                elif j == 7:
                    rows.append("  ")
            if i == 1 or i == 6:
                if j == 0:
                    rows.append("  ")
                elif j == 7:
                    rows.append("  ")
            if i == 2 or i == 5:
                if j == 0:
                    rows.append("  ")
                elif j == 7:
                    rows.append("  ")
            if i == 3:
                if j == 0:
                    rows.append("WQ")
                elif j == 7:
                    rows.append("bq")
            if i == 4:
                if j == 0:
                    rows.append("WK")
                elif j == 7:
                    rows.append("bk")
            if j != 0 and j != 5 and j != 6 and j != 7:
                rows.append("  ")
        Board.append(rows)


def testinitialiseboardcheck():
    for i in range(8):
        rows = []
        for j in range(8):
            if j == 1:
                rows.append("  ")
            elif j == 6:
                rows.append("  ")
            if i == 0 or i == 7:
                if j == 0:
                    rows.append("WR")
                elif j == 7:
                    rows.append("  ")
            if i == 1 or i == 6:
                if j == 0:
                    rows.append("WN")
                elif j == 7:
                    rows.append("  ")
            if i == 2 or i == 5:
                if j == 0:
                    rows.append("WB")
                elif j == 7:
                    rows.append("  ")
            if i == 3:
                if j == 0:
                    rows.append("  ")
                elif j == 7:
                    rows.append("  ")
            if i == 4:
                if j == 0:
                    rows.append("WK")
                elif j == 7:
                    rows.append("bk")
            if j != 0 and j != 5 and j != 6 and j != 7:
                rows.append("  ")
        Board.append(rows)


"""Loop through each element of the 2D array, board, and print to screen with row and Column numbers"""


def drawboard():
    for i in range(8):
        if i != 7:
            print("       " + chr(i + 97),end="")
        else:
            print("      " + chr(i + 97) + "\n")
    for i in range(8, 0, -1):
        if i != 8:
            print("     -----------------------------------------------------------\n")
        print(str(i) + "    ", end="")
        for j in range(8):
            if j != 7:
                print(Board[j][i - 1] + "  |   ", end="")
            else:
                print(Board[j][i - 1] + "    " + "\n")


"""Move the piece the user selected to where they want to go in the board array"""


def movepiece(movefrom, moveto):
    global movetopiece

    movetopiece = Board[int(ord(moveto[:1])) - 97][int(moveto[1:]) - 1]
    for i in range(8):
        for j in range(8):
            if i + 97 == ord(movefrom[:1]) and j == int(movefrom[1:]) - 1:
                Board[ord(moveto[:1]) - 97][int(moveto[1:]) - 1] = Board[i][j]
                Board[i][j] = "  "


"""If inputCoords are between 0 and 7 call validsquaretomoveto(movefrom, moveto) else return False"""


def isThisAValidmove(movefrom, moveto):
    global errormessage

    try:
        if len(movefrom) == 2:
            if movefrom != moveto:
                if 97 <= ord(movefrom[:1]) < 105 and 0 <= int(movefrom[1:]) - 1 < 8:
                    if (Board[int(ord(movefrom[:1]) - 97)][int(movefrom[1:]) - 1])[:1] == whosTurn:
                        return validsquaretomoveto(movefrom, moveto)
                    else:
                        errormessage = "Please select one of your own pieces"
                        return False
                else:
                    errormessage = "Please select a piece on the board"
                    return False
            else:
                errormessage = "Cannot move to the same square"
                return False
        else:
            errormessage = "This is an invalid square"
            return False
    except ValueError:
        errormessage = "This is an invalid square to move from, please select another, must be a letter between a - h followed by a number between 1 - 8"


"""If outputCoords are between 0 and 7 and not your own piece call specific piece move, else return False"""


def validsquaretomoveto(movefrom, moveto):
    global errormessage

    try:
        if len(moveto) == 2:
            if 97 <= ord(moveto[:1]) < 105 and 0 <= int(moveto[1:]) - 1 < 8:
                if (Board[int(ord(moveto[:1]) - 97)][int(moveto[1:]) - 1])[:1] == whosTurn:
                    errormessage = "Cannot move to a square with your own piece already on it"
                    return False
                else:
                    if (Board[int(ord(movefrom[:1]) - 97)][int(movefrom[1:]) - 1])[1:].upper() == "R":
                        return rookValidMove(movefrom, moveto)
                    elif (Board[int(ord(movefrom[:1]) - 97)][int(movefrom[1:]) - 1])[1:].upper() == "N":
                        return knightValidMove(movefrom, moveto)
                    elif (Board[int(ord(movefrom[:1]) - 97)][int(movefrom[1:]) - 1])[1:].upper() == "B":
                        return bishopValidMove(movefrom, moveto)
                    elif (Board[int(ord(movefrom[:1]) - 97)][int(movefrom[1:]) - 1])[1:].upper() == "Q":
                        return queenValidMove(movefrom, moveto)
                    elif (Board[int(ord(movefrom[:1]) - 97)][int(movefrom[1:]) - 1])[1:].upper() == "K":
                        return kingValidMove(movefrom, moveto)
                    elif (Board[int(ord(movefrom[:1]) - 97)][int(movefrom[1:]) - 1])[1:].upper() == "P":
                        return pawnValidMove(movefrom, moveto)
            else:
                errormessage = "Cannot move to a square off the board"
                return False
        else:
            errormessage = "This is an invalid square to move to, Length of input must be 2"
            return False
    except ValueError:
        errormessage = "This is an invalid square to move to, please select another, must be a letter between a - h followed by a number between 1 - 8"


"""Check if move is valid for a rook, ie. any number of squares vertical or horizontal"""


def rookValidMove(movefrom, moveto):
    if int(ord(moveto[:1]) - 97) == int(ord(movefrom[:1]) - 97) or int(moveto[1:]) == int(movefrom[1:]):
        if nothingInTheWay(movefrom, moveto):
            setcastleingflags()
            return True
        else:
            return False
    else:
        return False


"""If move is valid for a King return True else return False"""


def kingValidMove(movefrom, moveto):
    global castled
    global castlingallowed
    global whosTurn

    if (abs(int(ord(moveto[:1]) - 97) - int(ord(movefrom[:1]) - 97)) == 1 and (
            abs(int(moveto[1:]) - int(movefrom[1:])) >= 0 and abs(int(moveto[1:]) - int(movefrom[1:])) < 2)) or (
            abs(int(moveto[1:]) - int(movefrom[1:])) == 1 and (
            abs(int(ord(moveto[:1]) - 97) - int(ord(movefrom[:1]) - 97)) >= 0 and abs(
            int(ord(moveto[:1]) - 97) - int(ord(movefrom[:1]) - 97)) < 2)):
        # if abs(int(moveto[1:]) - int(movefrom[1:])) == 1:
        if not checkincheck:
            if castlingallowed & 0b00000001 == 0b00000000:
                setcastleingflags()
                return True
            else:
                return True
        else:
            return True
            # else:
    #   return False
    elif abs(int(ord(moveto[:1]) - 97) - int(ord(movefrom[:1]) - 97)) == 2:
        if moveto[1:] == movefrom[1:] and (movefrom[1:] == "8" or movefrom[1:] == "1"):
            if not checkincheck:
                if (whosTurn == "W" and castlingallowed & 0b01000000 == 0b00000000) or (
                        whosTurn == "b" and castlingallowed & 0b10000000 == 0b00000000):
                    if castlingvalid():
                        if whosTurn == "W":
                            castlingallowed = castlingallowed | 0b01000000
                        else:
                            castlingallowed = castlingallowed | 0b10000000
                        setcastleingflags()
                        castled = True
                        return True
                    else:
                        return False
                else:
                    return False
        else:
            return False
    else:
        return False


"""Called when a king or rook moves and simply sets a flag showing that piece has moved during the game"""


def setcastleingflags():
    global moveto
    global movefrom
    global castlingallowed

    if Board[int(ord(movefrom[:1])) - 97][int(movefrom[1:]) - 1].lower() == "k":
        if whosTurn == "W":
            castlingallowed = castlingallowed | 0b00000001
        else:
            castlingallowed = castlingallowed | 0b00000010
    else:
        if whosTurn == "W":
            if movefrom[:1] == 'a':
                castlingallowed = castlingallowed | 0b00000100
            else:
                castlingallowed = castlingallowed | 0b00001000
        else:
            if movefrom[:1] == 'a':
                castlingallowed = castlingallowed | 0b00010000
            else:
                castlingallowed = castlingallowed | 0b00100000


"""If move is valid for a Knight return True else return False"""


def knightValidMove(movefrom, moveto):
    if abs(int(ord(moveto[:1]) - 97) - int(ord(movefrom[:1]) - 97)) == 1 and abs(
            int(moveto[1:]) - int(movefrom[1:])) == 2:
        return True
    elif abs(int(ord(moveto[:1]) - 97) - int(ord(movefrom[:1]) - 97)) == 2 and abs(
            int(moveto[1:]) - int(movefrom[1:])) == 1:
        return True
    else:
        return False


"""Checks if move is valid for a bishop, moves diagonally and cannot jump"""


def bishopValidMove(movefrom, moveto):
    if abs(int(ord(moveto[:1]) - 97) - int(ord(movefrom[:1]) - 97)) == abs(int(moveto[1:]) - int(movefrom[1:])):
        return nothingInTheWay(movefrom, moveto)
    else:
        return False


"""Queens can move the same as rooks and bishops combined 
    so if either is valid then queen is a valid move, else return False"""


def queenValidMove(movefrom, moveto):
    if bishopValidMove(movefrom, moveto) or rookValidMove(movefrom, moveto):
        return True
    else:
        return False


"""If move is valid for a pawn return True else return False"""


def pawnValidMove(movefrom, moveto):
    global whosTurn
    global checkincheck

    if whosTurn == 'W':
        if int(movefrom[1:]) == 2:
            if int(ord(moveto[:1]) - 97) == int(ord(movefrom[:1]) - 97):
                """"Check for white pawn making initial move"""
                if int(moveto[1:]) - int(movefrom[1:]) == 1 or int(moveto[1:]) - int(movefrom[1:]) == 2:
                    if (Board[int(ord(moveto[:1]) - 97)][int(moveto[1:]) - 1])[:1] != 'b':
                        if int(moveto[1:]) - int(movefrom[1:]) == 2:  # return nothingInTheWay
                            return nothingInTheWay(movefrom, moveto)
                        else:
                            return True
                    else:
                        return False
                else:
                    return False
        else:
            """Check for White pawn moving forward a square after initial move"""
            if int(ord(moveto[:1]) - 97) == int(ord(movefrom[:1]) - 97):
                if int(moveto[1:]) - int(movefrom[1:]) == 1:
                    if Board[int(ord(moveto[:1])) - 97][(int(moveto[1:]) - 1)][:1] != "b":
                        if checkincheck == False:
                            if movefrom[1:] == "7":
                                print("HERE : " + str(checkincheck))
                                pawnpromotion()
                                return True
                        return True
                    else:
                        return False
                else:
                    return False
        """Check for White pawn taking piece at any time"""
        if abs(int(ord(moveto[:1]) - 97) - int(ord(movefrom[:1]) - 97)) == 1:
            if int(moveto[1:]) - int(movefrom[1:]) == 1:
                if Board[int(ord(moveto[:1])) - 97][int(moveto[1:]) - 1][:1] == "b":
                    if checkincheck == False:
                        if movefrom[1:] == "7":
                            print("HERE1 : " + str(checkincheck))
                            pawnpromotion()
                            return True
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        """Same as above but for black pawns"""
        if int(movefrom[1:]) == 7:
            if int(ord(moveto[:1]) - 97) == int(ord(movefrom[:1]) - 97):
                if int(moveto[1:]) - int(movefrom[1:]) == -1 or int(moveto[1:]) - int(movefrom[1:]) == -2:
                    if Board[int(ord(moveto[:1])) - 97][int(moveto[1:]) - 1][:1] != 'W':
                        if int(moveto[1:]) - int(movefrom[1:]) == -2:  # return nothingInTheWay
                            return nothingInTheWay(movefrom, moveto)
                        else:
                            return True
                    else:
                        return False
                else:
                    return False
        else:
            """Check for Black pawn moving forward a square after initial move"""
            if int(ord(moveto[:1]) - 97) == int(ord(movefrom[:1]) - 97):
                if int(moveto[1:]) - int(movefrom[1:]) == -1:
                    if Board[int(ord(moveto[:1])) - 97][int(moveto[1:]) - 1][:1] != "W":
                        if checkincheck == False:
                            if movefrom[1:] == "2":
                                print("HERE2 : " + str(checkincheck))
                                pawnpromotion()
                                return True
                        return True
                    else:
                        return False
                else:
                    return False
        """Check for Black pawn taking piece at any time"""
        if abs(int(ord(moveto[:1]) - 97) - int(ord(movefrom[:1]) - 97)) == 1 and int(moveto[1:]) - int(
                movefrom[1:]) == -1:
            if Board[int(ord(moveto[:1])) - 97][int(moveto[1:]) - 1][:1] == "W":
                if checkincheck == False:
                    if movefrom[1:]:
                        print("HERE3 : " + str(checkincheck))
                        pawnpromotion()
                        return True
                return True
            else:
                return False
        else:
            return False

    """This routine changes the pawn to a major piece based on the users choice, the piece is then moved to a square on the back row later"""


def pawnpromotion():
    newpiece = input("please select what piece you would like : \n  1: Rook \n 2: Knight \n 3: Bishop \n 4: Queen\n")
    if newpiece == "1":
        if whosTurn == "W":
            Board[int(ord(movefrom[:1])) - 97][int(movefrom[1:]) - 1] = "WR"
        else:
            Board[int(ord(movefrom[:1])) - 97][int(movefrom[1:]) - 1] = "br"
    elif newpiece == "2":
        if whosTurn == "W":
            Board[int(ord(movefrom[:1])) - 97][int(movefrom[1:]) - 1] = "WN"
        else:
            Board[int(ord(movefrom[:1])) - 97][int(movefrom[1:]) - 1] = "bn"
    elif newpiece == "3":
        if whosTurn == "W":
            Board[int(ord(movefrom[:1])) - 97][int(movefrom[1:]) - 1] = "WB"
        else:
            Board[int(ord(movefrom[:1])) - 97][int(movefrom[1:]) - 1] = "bb"
    else:
        if whosTurn == "W":
            Board[int(ord(movefrom[:1])) - 97][int(movefrom[1:]) - 1] = "WQ"
        else:
            Board[int(ord(movefrom[:1])) - 97][int(movefrom[1:]) - 1] = "bq"

    """This routine returns True if castleing is allowed for the selected move"""


def castlingvalid():
    """ both haven't moved
        not moving into Check
        not moving through check"""

    global movefrom
    global moveto

    # White castleing Queen side

    if whosTurn == "W":
        if int(ord(moveto[:1])) - int(ord(movefrom[:1])) == 2:
            if castlingallowed & 0b00001001 == 0b00000000:
                if nothingInTheWay(movefrom, moveto):
                    for i in range(8):
                        for j in range(8):
                            if Board[i][j][:1] == "b":
                                for k in range(3):
                                    if isThisAValidmove(str(chr(i + 97)) + str(j + 1),
                                                        chr(int(ord(movefrom[:1])) + k) + movefrom[1:]):
                                        return False
                                return True
        else:
            # White castleing King side
            if castlingallowed & 0b00000101 == 0b00000000:
                if nothingInTheWay(movefrom, moveto):
                    for i in range(8):
                        for j in range(8):
                            if Board[i][j][:1] == "b":
                                for k in range(3):
                                    if isThisAValidmove(str(chr(i + 97)) + str(j + 1),
                                                        chr(int(ord(movefrom[:1])) - k) + movefrom[1:]):
                                        return False
                                return True
    else:
        # Black castleing Queen side
        if int(ord(moveto[:1])) - int(ord(movefrom[:1])) == 2:
            if castlingallowed & 0b00100010 == 0b00000000:
                if nothingInTheWay(movefrom, moveto):
                    for i in range(8):
                        for j in range(8):
                            if Board[i][j][:1] == "W":
                                for k in range(3):
                                    if isThisAValidmove(str(chr(i + 97)) + str(j + 1),
                                                        chr(int(ord(movefrom[:1]) + k)) + movefrom[1:]):
                                        return False
                                return True
        else:
            # Black castleing King side
            if castlingallowed & 0b00100010 == 0b00000000:
                if nothingInTheWay(movefrom, moveto):
                    for i in range(8):
                        for j in range(8):
                            if Board[i][j][:1] == "W":
                                for k in range(3):
                                    if isThisAValidmove(str(chr(i + 97)) + str(j + 1),
                                                        chr(int(ord(movefrom[:1]) - k)) + movefrom[1:]):
                                        return False
                                return True


"""This routine checks there is no piece inbetween the start square and destination square for rook,bishop, queen or pawn moving 2 squares"""


def nothingInTheWay(movefrom, moveto):
    if movefrom[1:] == moveto[1:]:  # checks all 4 vertical or horizontal directions
        if int(ord(movefrom[:1])) - 97 > int(ord(moveto[:1])) - 97:  # horizontal h -> a
            for i in range((int(ord(movefrom[:1]) - 97) - int(ord(moveto[:1]) - 97)) - 1):
                if Board[int(ord(movefrom[:1]) - 97) - (i + 1)][int(movefrom[1:]) - 1] != "  ":
                    return False
            return True
        else:  # horizontal a -> h
            for i in range((int(ord(moveto[:1]) - 97) - int(ord(movefrom[:1]) - 97)) - 1):
                if Board[int(ord(movefrom[:1]) - 97) + (i + 1)][int(movefrom[1:]) - 1] != "  ":
                    return False
            return True
    elif int(ord(movefrom[:1])) - 97 == int(ord(moveto[:1])) - 97:
        if int(movefrom[1:]) > int(moveto[1:]):  # vertical 8 -> 1
            for i in range((int(movefrom[1:]) - int(moveto[1:])) - 1):
                if Board[int(ord(movefrom[:1]) - 97)][(int(movefrom[1:]) - 1) - (i + 1)] != "  ":
                    return False
            return True
        else:  # vertical 1 -> 8
            for i in range((int(moveto[1:]) - int(movefrom[1:])) - 1):
                if Board[int(ord(movefrom[:1]) - 97)][(int(movefrom[1:]) - 1) + (i + 1)] != "  ":
                    return False
            return True
    else:  # checks all 4 diagonal moves
        if int(movefrom[1:]) > int(moveto[1:]) and int(ord(movefrom[:1]) - 97) > int(ord(moveto[:1]) - 97):  # >>
            for i in range((int(movefrom[1:]) - int(moveto[1:])) - 1):
                if Board[int(ord(movefrom[:1]) - 97) - (i + 1)][(int(movefrom[1:]) - 1) - (i + 1)] != "  ":
                    return False
            return True
        elif int(movefrom[1:]) < int(moveto[1:]) and int(ord(movefrom[:1]) - 97) > int(ord(moveto[:1]) - 97):  # <>
            for i in range((int(moveto[1:]) - int(movefrom[1:])) - 1):
                if Board[int(ord(movefrom[:1]) - 97) - (i + 1)][(int(movefrom[1:]) - 1) + (i + 1)] != "  ":
                    return False
            return True
        elif int(movefrom[1:]) < int(moveto[1:]) and int(ord(movefrom[:1]) - 97) < int(ord(moveto[:1]) - 97):  # <<
            for i in range((int(moveto[1:]) - int(movefrom[1:])) - 1):
                if Board[int(ord(movefrom[:1]) - 97) + (i + 1)][(int(movefrom[1:]) - 1) + (i + 1)] != "  ":
                    return False
            return True
        else:
            for i in range((int(movefrom[1:]) - int(moveto[1:])) - 1):
                if Board[int(ord(movefrom[:1]) - 97) + (i + 1)][(int(movefrom[1:]) - 1) - (i + 1)] != "  ":  # ><
                    return False
            return True


"""This routine checks that if by making your move will you put yourself in check, if so return True"""
"""makeMove is called before this routine but after valid coordinates have been given"""


def amINotInCheck():
    global whosTurn
    global checkincheck

    inCheckFlag = False
    kingX = 0
    kingY = 0

    """Get position coordinates of your king"""

    for i in range(8):
        for j in range(8):
            if Board[i][j][:1] == whosTurn and Board[i][j][1:].upper() == "K":
                kingX = j
                kingY = i

    if whosTurn == 'W':
        whosTurn = 'b'
    else:
        whosTurn = 'W'

    invalidMove = False

    """Change whos turn it is and see if any of their pieces have a valid move to your King, if so set Flag"""
    checkincheck = True
    for i in range(8):
        for j in range(8):
            if Board[i][j][:1] == whosTurn:
                invalidMove = isThisAValidmove(str(chr(i + 97)) + str(j + 1), str(chr(kingY + 97)) + str(kingX + 1))
                if invalidMove:
                    inCheckFlag = True
                    break
        if inCheckFlag:
            break

    """Change whos turn it is back"""

    if whosTurn == 'W':
        whosTurn = 'b'
    else:
        whosTurn = 'W'

    """If Flag set then You are in check and this is therefore an invalid move and Return False"""

    if inCheckFlag:
        if not checkincheck:
            print("YOU ARE NOT ALLOWED TO MOVE INTO CHECK")
        checkincheck = False
        return False
    else:
        checkincheck = False
        return True


"""This routine simply undoes the last move by switching the pieces in the board array"""


def undoLastMove(moveFromSquare, moveToSquare):
    global movetopiece

    Board[int(ord(moveFromSquare[:1])) - 97][int(moveFromSquare[1:]) - 1] = Board[int(ord(moveToSquare[:1])) - 97][
        int(moveToSquare[1:]) - 1]
    Board[int(ord(moveToSquare[:1])) - 97][int(moveToSquare[1:]) - 1] = movetopiece


"""This routine creates a list of spaces in between to given pieces, this is used in inCheckMate() to see what spaces to try and block a check, works the same way as nothingInTheWay()"""


def createListOfSpacesInBetween2Pieces(movefrom, moveto):
    spacesInBetween = []

    if movefrom[1:] == moveto[1:]:
        if int(ord(movefrom[:1]) - 97) > int(ord(moveto[:1]) - 97):  # horizontal h -> a
            for i in range((int(ord(movefrom[:1]) - 97) - int(ord(moveto[:1]) - 97)) - 1):
                spacesInBetween.append(str(chr(int(ord(movefrom[:1])) - (i + 1))) + str(int(movefrom[1:])))
        else:  # horizontal a -> h
            for i in range((int(ord(moveto[:1]) - 97) - int(ord(movefrom[:1]) - 97)) - 1):
                spacesInBetween.append(str(chr(int(ord(movefrom[:1])) + (i + 1))) + str(int(movefrom[1:])))
    elif int(ord(movefrom[:1])) - 97 == int(ord(moveto[:1])) - 97:
        if int(movefrom[1:]) > int(moveto[1:]):  # vertical 8 -> 1
            for i in range((int(movefrom[1:]) - int(moveto[1:])) - 1):
                spacesInBetween.append(str(chr(int(ord(movefrom[:1])))) + str(int(movefrom[1:]) - (i + 1)))
        else:  # vertical 1 -> 8
            for i in range((int(moveto[1:]) - int(movefrom[1:])) - 1):
                spacesInBetween.append(str(chr(int(ord(movefrom[:1])))) + str(int(movefrom[1:]) + (i + 1)))
    else:  # check all 4 diagonal directions
        if int(movefrom[1:]) > int(moveto[1:]) and int(ord(movefrom[:1])) - 97 > int(ord(moveto[:1])) - 97:  # >>
            for i in range((int(movefrom[1:]) - int(moveto[1:])) - 1):
                spacesInBetween.append(str(chr(int(ord(movefrom[:1])) - (i + 1))) + str(int(movefrom[1:]) - (i + 1)))
        elif int(movefrom[1:]) < int(moveto[1:]) and int(ord(movefrom[:1]) - 97) > int(ord(moveto[:1]) - 97):  # <>
            for i in range((int(moveto[1:]) - int(movefrom[1:])) - 1):
                spacesInBetween.append(str(chr(int(ord(movefrom[:1])) - (i + 1))) + str(int(movefrom[1:]) + (i + 1)))
        elif int(movefrom[1:]) < int(moveto[1:]) and int(ord(movefrom[:1]) - 97) < int(ord(moveto[:1]) - 97):  # <<
            for i in range((int(moveto[1:]) - int(movefrom[1:])) - 1):
                spacesInBetween.append(str(chr(int(ord(movefrom[:1])) + (i + 1))) + str(int(movefrom[1:]) + (i + 1)))
        else:  # ><
            for i in range((int(movefrom[1:]) - int(moveto[1:])) - 1):
                spacesInBetween.append(str(chr(int(ord(movefrom[:1])) + (i + 1))) + str(int(movefrom[1:]) - (i + 1)))
    return spacesInBetween


"""This routine checks whether the opposition is in check as a result of the last move"""


def inCheck():
    global checkincheck

    attackingPieces = 0

    """Get coordinates of opponents King"""

    for i in range(8):
        for j in range(8):
            if Board[i][j][:1] != whosTurn and Board[i][j][:1] != "  " and (
                    Board[i][j][1:] == "K" or Board[i][j][1:] == "k"):
                kingX = j
                kingY = i

    """If opponents King is a valid move for any of your pieces add one to attackingPieces"""
    checkincheck = True
    for i in range(8):
        for j in range(8):
            if Board[i][j][:1] == whosTurn:
                validMove = isThisAValidmove(str(chr(i + 97)) + str(j + 1), str(chr(kingY + 97)) + str(kingX + 1))
                if validMove:
                    attackingPieces = attackingPieces + 1

    """If in check call inCheckMate()"""
    if attackingPieces > 0:
        print("\nCHECK\n")
        return inCheckMate(kingY, kingX, attackingPieces)
    else:
        checkincheck = False
        return False


def inCheckMate(kingY, kingX, attackingPieces):
    # Has king any vaild moves
    # Can the attacking piece be blocked
    # Can the attacking piece be taken
    # Need attacking piece Square coordinates

    global whosTurn
    global gameOver
    global checkincheck

    validMove = False

    if whosTurn == 'W':
        whosTurn = 'b'
    else:
        whosTurn = 'W'

    """Check if the king has a valid move to any of the 8 surrounding squares"""

    for i in range(3):
        if isThisAValidmove(str(chr(kingY + 97)) + str(kingX + 1), str(chr(kingY + 97)) + str(kingX + 1 + (i - 1))):
            movepiece(str(chr(kingY + 97)) + str(kingX + 1), str(chr(kingY + 97)) + str(kingX + 1 + (i - 1)))
            validMove = amINotInCheck()
            undoLastMove(str(chr(kingY + 97)) + str(kingX + 1), str(chr(kingY + 97)) + str(kingX + 1 + (i - 1)))

    for i in range(3):
        if isThisAValidmove(str(chr(kingY + 97)) + str(kingX + 1), str(chr(kingY + 98)) + str(kingX + 1 + (i - 1))):
            movepiece(str(chr(kingY + 97)) + str(kingX + 1), str(chr(kingY + 98)) + str(kingX + 1 + (i - 1)))
            validMove = amINotInCheck()
            undoLastMove(str(chr(kingY + 97)) + str(kingX + 1), str(chr(kingY + 98)) + str(kingX + 1 + (i - 1)))

    for i in range(3):
        if isThisAValidmove(str(chr(kingY + 97)) + str(kingX + 1), str(chr(kingY + 96)) + str(kingX + 1 + (i - 1))):
            movepiece(str(chr(kingY + 97)) + str(kingX + 1), str(chr(kingY + 96)) + str(kingX + 1 + (i - 1)))
            validMove = amINotInCheck()
            undoLastMove(str(chr(kingY + 97)) + str(kingX + 1), str(chr(kingY + 96)) + str(kingX + 1 + (i - 1)))

    """The king moving is the only way out of check if more than 1 piece is attacking it directly"""
    """If king has no valid moves check if the 1 attacking piece can either be taken or blocked"""

    if not validMove:
        if attackingPieces == 1:
            for i in range(8):
                if validMove:
                    break
                for j in range(8):
                    if Board[i][j][:1] == whosTurn:
                        """Check if any piece can take the oppossing attacking piece,
                        this is done by calling isThisAValidMove() on every piece in your team to the attacking square"""
                        validMove = isThisAValidmove(str(chr(i + 97)) + str(j + 1), moveto)
                        if validMove:
                            """If it is a valid move to take the attacking piece makesure that doing so does not put you in check from somewhere else"""
                            movepiece(str(chr(i + 97)) + str(j + 1), moveto)
                            validMove = amINotInCheck()
                            undoLastMove(str(chr(i + 97)) + str(j + 1), moveto)
                        if validMove:
                            break
                        else:
                            """Check if any piece can block the oppossing attacking piece from putting the king in check"""
                            spacestoblock = createListOfSpacesInBetween2Pieces(moveto, str(chr(kingY + 97)) + str(
                                int(kingX + 1)))
                            for x in spacestoblock:
                                validMove = isThisAValidmove(str(chr(i + 97)) + str(j + 1), x)
                                if validMove:
                                    """If it is a valid move to take the attacking piece makesure that doing so does not put you in check from somewhere else"""
                                    movepiece(str(chr(i + 97)) + str(j + 1), x)
                                    validMove = amINotInCheck()
                                    undoLastMove(str(chr(i + 97)) + str(j + 1), x)
                                if validMove:
                                    break

    if whosTurn == 'W':
        whosTurn = 'b'
    else:
        whosTurn = 'W'

    checkincheck = False

    if validMove:
        return False
    else:
        print("\n CHECKMATE GAME OVER " + whosTurn + " WINS \n")
        gameOver = True
        return True


def scores():
    whitescore = 0
    blackscore = 0

    for i in range(8):
        for j in range(8):
            if (Board[i][j])[:1] == "W":
                if (Board[i][j])[1:] == "R":
                    whitescore = whitescore + 5
                elif (Board[i][j])[1:] == "N" or (Board[i][j])[1:] == "B":
                    whitescore = whitescore + 3
                elif (Board[i][j])[1:] == "Q":
                    whitescore = whitescore + 9
                elif (Board[i][j])[1:] == "K":
                    whitescore = whitescore + 1000
                else:
                    whitescore = whitescore + 1
            elif (Board[i][j])[:1] == "b":
                if (Board[i][j])[1:] == "r":
                    blackscore = blackscore + 5
                elif (Board[i][j])[1:] == "n" or (Board[i][j])[1:] == "b":
                    blackscore = blackscore + 3
                elif (Board[i][j])[1:] == "q":
                    blackscore = blackscore + 9
                elif (Board[i][j])[1:] == "k":
                    blackscore = blackscore + 1000
                else:
                    blackscore = blackscore + 1

    print("WHITE : " + str(whitescore))
    print("BLACK : " + str(blackscore))


def createlistofvalidmoves(colour):
    global whosTurn
    global checkincheck
    defaultboardscore = 0
    bestmove = -1
    counter = -1

    whosTurn = "b"

    listofvalidmoves = []
    for i in range(8):
        for j in range(8):
            if Board[i][j][:1] == whosTurn:
                for k in range(8):
                    for l in range(8):
                        checkincheck = True
                        if isThisAValidmove(str(chr(i + 97)) + str(j + 1), str(chr(k + 97)) + str(l + 1)):
                            movepiece(str(chr(i + 97)) + str(j + 1), str(chr(k + 97)) + str(l + 1))
                            validMove = amINotInCheck()
                            undoLastMove(str(chr(i + 97)) + str(j + 1), str(chr(k + 97)) + str(l + 1))
                            if validMove:
                                listofvalidmoves.append(
                                    str(chr(i + 97)) + str(j + 1) + "," + str(chr(k + 97)) + str(l + 1))

    checkincheck = False
    return listofvalidmoves

    # if len(listofvalidmoves) == 0:
    #     print("NO VALID MOVES")
    # else:
    #     for x in listofvalidmoves:
    #         counter = counter + 1
    #         movepiece(x[:2], x[3:])
    #         currentscore = evaluateboard()
    #         if currentscore < defaultboardscore:
    #             defaultboardscore = currentscore
    #             bestmove = counter
    #         undoLastMove(x[:2], x[3:])
    #     if bestmove != -1:
    #         movepiece(listofvalidmoves[bestmove][:2], listofvalidmoves[bestmove][3:])
    #     else:
    #         randomMove = random.randint(0, len(listofvalidmoves) - 1)
    #         print(randomMove)
    #         movepiece(listofvalidmoves[randomMove][:2], listofvalidmoves[randomMove][3:])
    # checkincheck = False


def minimax(depth, colour, isMaximizingPlayer):

  #base case to terminate recursion
  if depth == 0:
    boardvalue = evaluateboard()
    return(boardvalue) # might need to return NULL as well

  bestMove = None
  possiblemoves = createlistofvalidmoves(colour)
  if isMaximizingPlayer:
    best = float("-inf")
    for x in possiblemoves:
        movepiece(x[:2], x[3:])
        best = max(best,minimax(depth-1,'W',not isMaximizingPlayer))
        undoLastMove(x[:2], x[3:])
    return best
  else:
    best = float("inf")
    for x in possiblemoves:
        movepiece(x[:2], x[3:])
        best = min(best,minimax(depth-1,'b',not isMaximizingPlayer))
        undoLastMove(x[:2], x[3:])
    return best


#using minimax function to look 3 moves ahead and find optimal move
def findBestMove():
    bestMove = ""
    bestVal = float("inf")

    possiblemoves = createlistofvalidmoves(whosTurn)
    for x in possiblemoves:
        movepiece(x[:2], x[3:])
        moveVal = minimax(0,'W',False)
        undoLastMove(x[:2], x[3:])

        if moveVal < bestVal:
            bestMove = x
            bestVal = moveVal

    print(bestMove)
    print(bestVal)
    return bestMove







def evaluateboard():
    boardvalue = 0

    for i in range(8):
        for j in range(8):
            if (Board[i][j])[:1] == "W":
                if (Board[i][j])[1:] == "R":
                    boardvalue = boardvalue + 5
                elif (Board[i][j])[1:] == "N" or (Board[i][j])[1:] == "B":
                    boardvalue = boardvalue + 3
                elif (Board[i][j])[1:] == "Q":
                    boardvalue = boardvalue + 9
                elif (Board[i][j])[1:] == "K":
                    boardvalue = boardvalue + 1000
                else:
                    boardvalue = boardvalue + 1
            elif (Board[i][j])[:1] == "b":
                if (Board[i][j])[1:] == "r":
                    boardvalue = boardvalue - 5
                elif (Board[i][j])[1:] == "n" or (Board[i][j])[1:] == "b":
                    boardvalue = boardvalue - 3
                elif (Board[i][j])[1:] == "q":
                    boardvalue = boardvalue - 9
                elif (Board[i][j])[1:] == "k":
                    boardvalue = boardvalue - 1000
                else:
                    boardvalue = boardvalue - 1

    return boardvalue


initialiseboard()
# testinitialiseboardcastleing()
# testinitialiseboardpawnpromotion()
# testinitialiseboardcheck()
drawboard()

while not gameOver:
    if whosTurn == 'W':
        print("\n WHITE'S TURN \n")
    else:
        print("\n BLACK'S TURN \n")

    while not validmove:
        while not validCoords:
            movefrom = input("Please enter the coordinates of the piece you are moving, column first, eg. e2 \n").lower()
            moveto = input("Please enter the coordinates of where you wish to move to, column first, eg. e4 ").lower()
            validCoords = isThisAValidmove(movefrom, moveto)
            if not validCoords:
                print(errormessage)

                # valid coordinates at this point but could now be in check because of the move
        validCoords = False
        if castled:
            castled = False
            if whosTurn == "W":
                if moveto[:1] == "g":
                    movepiece("h1", "f1")
                else:
                    movepiece("a1", "d1")
            else:
                if moveto[:1] == "g":
                    movepiece("h8", "f8")
                else:
                    movepiece("a8", "d8")

        movepiece(movefrom, moveto)
        validmove = amINotInCheck()
        if not validmove:
            undoLastMove(movefrom, moveto)
            # valid move at this point and not in check
    validmove = False
    inCheck()
    drawboard()
    #find best move for opposition (ie.black, minimizing)
    oppositionMove = findBestMove()
    movepiece(oppositionMove[:2], oppositionMove[3:])
    #createlistofvalidmoves(whosTurn)

    if not gameOver:
        scores()
        drawboard()

        if whosTurn == 'W':
            whosTurn = 'b'
        else:
            whosTurn = 'W'
