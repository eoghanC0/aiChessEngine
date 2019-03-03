columns = []
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


drawboard()
inputCoordinates = input("Please enter the coordinates of the piece you are moving, row first, eg. 3,4 \n")
outputCoordinates = input("Please enter the coordinates of where you wish to move to, row first, eg. 5,4 \n")


def movepiece():
    for i in range(8):
        for j in range(8):
            if i == int(inputCoordinates[:1]) and j == int(inputCoordinates[2:]):
                columns[int(outputCoordinates[:1])][int(outputCoordinates[2:])] = columns[i][j]
                columns[i][j] = "  "


movepiece()
drawboard()