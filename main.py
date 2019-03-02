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
            rows.append(" ")
    columns.append(rows)

for i in range(8):
    if i != 7:
        print("      " + str(i), end="")
    else:
        print("      " + str(i) + "\n")

for i in range(8):
    if i == 0 or i == 1 or i == 6 or i == 7:
        print(str(i) + "    ", end="")
    else:
        print(str(i) + "    ")
    for j in range(8):
        if j != 7:
            print(columns[i][j] + "     ", end="")
        else:
            print(columns[i][j] + "    " + "\n")

print("Please enter the coordinates of the piece you are moving, column first, eg. 3,4")