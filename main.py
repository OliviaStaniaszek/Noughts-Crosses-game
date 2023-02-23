import pygame

# data structures
valid = False  # move later
grid = {
    "1": " ",
    "2": " ",
    "3": " ",
    "4": " ",
    "5": " ",
    "6": " ",
    "7": " ",
    "8": " ",
    "9": " ",
}

# -------------functions------------------


def validCheck(grid, module):
    modVal = grid.get(str(module))
    if modVal == " ":
        valid = True
    else:
        valid = False
    return valid


def getModule(grid, module):
    modVal = grid.get(str(module))
    return modVal


def checkRow(grid, a, b, c, add):
    # print('TEST - add:',add)
    modVala = getModule(grid, a + add)
    # print('TEST',modVala, a + add)
    modValb = getModule(grid, b + add)
    # print('TEST',modValb, b + add)
    modValc = getModule(grid, c + add)
    # print('TEST',modValc, c + add)

    # print('TEST- row',modVala, modValb, modValc)
    if modVala == modValb == modValc == 'X' or modVala == modValb == modValc == 'O':
        win = True
    else:
        win = False
    return win


def checkWin(grid):
    win = False
    # print('TEST- win in checkwin',win)
    # print('TEST - checkwin start')

    if win == False:
        # print('\nTEST - horizontal')
        for i in range(0, 7, 3):
            # print('add',i)
            win = checkRow(grid, 1, 2, 3, i)
            # print('TEST - win after checkrow:',win)
            if win == True:
                return win
            # print('TEST - win after checkrow:',win)

        if win == False:
            # print('\nTEST - vertical')
            for i in range(0, 3):
                # print('add',i)
                win = checkRow(grid, 1, 4, 7, i)
                # print('TEST - win after checkrow:',win)
                if win == True:
                    return win
                # print('TEST - win after checkrow:',win)

            if win == False:
                # print('\nTEST - diagonal')
                win = checkRow(grid, 1, 5, 9, 0)
                # print('TEST - win after checkrow:',win)

                if win == True:
                    return win
                else:
                    win = checkRow(grid, 3, 5, 7, 0)
                    # print('TEST - win after checkrow:',win)
                    return win


def boardFull(grid):
    for i in range(10):
        modVal = getModule(grid, i)
        # print('TEST - modVal:',modVal)
        if modVal == ' ':
            return False
    #else:
    return True


def changeModule(grid, module):
    # print('TEST - change module')
    if player == 1:
        grid.update({str(module): 'X'})
        # grid[str(module)] = 'x'
    else:
        grid.update({str(module): 'O'})
        # grid[str(module)] = 'o'


# --------------game flow-------------------
player = 1
win = False
