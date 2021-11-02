# The first game


a = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
b = [' ', '1', '2', '3', '4', '5', '6', '7', '8', '9']
count: int = 0
winrivel: int = 0
player: int = 0

while count < 9:

    print(" {0} | {1} | {2} ".format(a[1], a[2], a[3]))
    print("-----------")
    print(" " + str(a[4]) + " | " + str(a[5]) + " | " + str(a[6]) + " ")
    print("-----------")
    print(" " + str(a[7]) + " | " + str(a[8]) + " | " + str(a[9]) + " ")

    if count % 2 == 0:
        mark = 'x'
        player = 1
    else:
        mark = 'o'
        player = 2

    print("\tPlayer {0} enter any number from 1 to 9 .".format(player))
    choice = int(input("\t: "))

    if a[choice] == 'x' or a[choice] == 'o':
        print("\tPosition is already Occupied")
        continue

    if choice == 1 and a[1] == ' ':
        a[1] = mark
        b[1] = mark
    elif choice == 2 and a[2] == ' ':
        a[2] = mark
        b[2] = mark
    elif choice == 3 and a[3] == ' ':
        a[3] = mark
        b[3] = mark
    elif choice == 4 and a[4] == ' ':
        a[4] = mark
        b[4] = mark
    elif choice == 5 and a[5] == ' ':
        a[5] = mark
        b[5] = mark
    elif choice == 6 and a[6] == ' ':
        a[6] = mark
        b[6] = mark
    elif choice == 7 and a[7] == ' ':
        a[7] = mark
        b[7] = mark
    elif choice == 8 and a[8] == ' ':
        a[8] = mark
        b[8] = mark
    elif choice == 9 and a[9] == ' ':
        a[9] = mark
        b[9] = mark

    if ((b[1] == b[2] and b[2] == b[3]) or (b[4] == b[5] and b[5] == b[6]) or (b[7] == b[8] and b[8] == b[9]) or (
            b[1] == b[4] and b[4] == b[7]) or (b[2] == b[5] and b[5] == b[8]) or (b[3] == b[6] and b[6] == b[9]) or (
            b[1] == b[5] and b[5] == b[9]) or (b[3] == b[5] and b[5] == b[7])):
        winrivel = 1
        break

    count = count + 1

print(" {0} | {1} | {2} ".format(a[1], a[2], a[3]))
print("-----------")
print(" {0} | {1} | {2} ".format(str(a[4]), str(a[5]), str(a[6])))
print("-----------")
print(" {1} | {1} | {2} ".format(str(a[7]), str(a[8]), str(a[9])))

if winrivel == 1:
    print("\tGame Over")
    print("\tPlayer {0} Wins the Game.".format(player))
    print("\tCongratulations")
else:
    print("\tGame Draw")
