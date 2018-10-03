import random
class GenericTyle:
    def __init__(self, type, value):
        self.type = type
        self.value = value
        self.clicked = False

    def getType(self):
        return self.type

    def setType(self, type):
        self.type = type
        return True

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value
        return True

    def getClicked(self):
        return self.clicked

    def setClicked(self, clicked):
        self.clicked = clicked
        return True

    def toggleClicked(self):
        self.clicked = not self.clicked
        return True


class Bomb(GenericTyle):
    def __init__(self):
        self.Clicked = False
        self.type = "bomb"
        self.value = "b"

class Number(GenericTyle):
    def __init__(self, value):
        self.value = value
        self.type = "number"
        self.clicked = False

    def incrementValue(self):
        self.value+=1
        return self.value


# main code starts here
def getBoard():
    board = []
    length = 24  # user values here
    height = 30  # user values here
    bombNumber = 200  # user values here

    for i in range(height):
        board.append([])
        for j in range(length):
            board[i].append(Number(0))

    usedVals = []

    stuff = []
    for i in range(bombNumber):
        x = random.randint(0, length) - 1
        y = random.randint(0, height) - 1
        temp = [y, x]
        while usedVals.__contains__(temp) or temp[0] < 0 or temp[1] < 0:
            x = random.randint(0, length) - 1
            y = random.randint(0, height) - 1
            temp = [y, x]
        usedVals.append(temp)
        #print(temp[1])
        board[y][x] = Bomb()

        yp1 = y+1 >= 0 and y+1 < height
        ym1 = y-1 >= 0 and y-1 < height
        xp1 = x+1 >= 0 and x+1 < length
        xm1 = x-1 >= 0 and x-1 < length
        #print([y,x])
        #print(xp1)
        if xp1 and board[y][x+1].type != "bomb":
           board[y][x+1].incrementValue()
        if xm1 and board[y][x-1].type != "bomb":
            board[y][x-1].incrementValue()

        if yp1:
            if board[y+1][x].type != "bomb":
                board[y+1][x].incrementValue()
            if xp1 and board[y+1][x+1].type != "bomb":
                board[y+1][x+1].incrementValue()
            if xm1 and board[y+1][x-1].type != "bomb":
                board[y+1][x-1].incrementValue()

        if ym1:
            if board[y-1][x].type != "bomb":
                board[y-1][x].incrementValue()
            if xp1 and board[y-1][x+1].type != "bomb":
                board[y-1][x+1].incrementValue()
            if xm1 and board[y-1][x-1].type != "bomb":
                board[y-1][x-1].incrementValue()

    return board

def printBoard(board):
    bString = ""
    for y in range(len(board)):
        for x in range(len(board[y])):
            bString += str(board[y][x].getValue())
            bString += " "
        bString += "\n"
    print(bString)






