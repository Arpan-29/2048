import random

def startGame() :
    # creating a 4X4 matrix with all 0's initially
    mat = []
    for i in range(4) :
        mat.append([0] * 4)
    
    return mat

def addNew24(mat) : 
    # finding all empty cells
    options = []
    for i in range(4) :
        for j in range(4) :
            if mat[i][j] == 0 :
                options.append((i, j))

    # choosing a random cell to fill in 2 or 4
    randCell = random.randint(0, len(options) - 1)
    r = options[randCell][0]
    c = options[randCell][1]

    # choosing either 2 or 4 with 90 and 10 percent probability respectively
    num = random.randint(0, 9)
    if num == 0 : 
        num = 4
    else :
        num = 2

    # filling that random cell with the chosen number
    mat[r][c] = num 

    return mat

def currentState(mat) :
    # checking for 2048
    for i in range(4) :
        for j in range(4) :
            if mat[i][j] == 2048 :
                return 'WON'

    # checking for 0
    for i in range(4) :
        for j in range(4) :
            if mat[i][j] == 0 :
                return 'GAME NOT OVER'
    
    # checking for same number in adjacent cells
    for i in range(3) :
        for j in range(3) :
            if (mat[i][j] == mat[i + 1][j]) or (mat[i][j] == mat[i][j + 1]) :
                return 'GAME NOT OVER'

    # checking the last row
    for j in range(3) :
        if mat[3][j] == mat[3][j + 1] :
            return 'GAME NOT OVER'
    
    # checking the last column
    for i in range(3) :
        if mat[i][3] == mat[i + 1][3] :
            return 'GAME NOT OVER'

    return 'LOST'

def copyMatrix(mat) :
    newMat = []
    
    for i in range(4) :
        newMat.append(mat[i])

    return newMat

def changedOrNot(oldMat, newMat) :
     # checking for any change
    for i in range(4) :
        for j in  range(4) :
            if oldMat[i][j] != newMat[i][j] :
                return True
    
    return False

def compress(mat) :
    # creating a new matrix with all 0's
    newMat = []
    for i in range(4) :
        newMat.append([0] * 4)

    # shifting all non-zero elements to the left
    for i in range(4) :
        pos = 0
        for j in range(4) :
            if mat[i][j] != 0 :
                newMat[i][pos] = mat[i][j]
                pos += 1
    
    return newMat

def merge(mat) :
    # combining 2 adjacent elements of a row if they are same
    for i in range(4) :
        for j in range(3) :
            if mat[i][j] != 0  and (mat[i][j] == mat[i][j + 1]) :
                mat[i][j] = 2 * mat[i][j]
                mat[i][j + 1] = 0

    return mat

def reverse(mat) :
    # Laterally reversing a matrix
    newMat = []
    for i in range(4) :
        newMat.append([0] * 4)

    for i in range(4) :
        for j in range(4) :
            newMat[i][j] = mat[i][4 - j - 1]

    return newMat

def transpose(mat) :
    # element at (i, j)th position is swapped with element at (j, i)th position
    newMat = []
    for i in range(4) :
        newMat.append([0] * 4)

    for i in range(4) :
        for j in range(4) :
            newMat[i][j] = mat[j][i]

    return newMat

def moveLeft(mat) :
    oldMat = copyMatrix(mat)

    mat = compress(mat)
    mat = merge(mat)
    mat = compress(mat)

    changed = changedOrNot(oldMat, mat)

    return mat, changed

def moveRight(mat) :
    oldMat = copyMatrix(mat)

    mat = reverse(mat)
    mat, c = moveLeft(mat)
    mat = reverse(mat)

    changed = changedOrNot(oldMat, mat)

    return mat, changed

def moveUp(mat) :
    oldMat = copyMatrix(mat)

    mat = transpose(mat)
    mat, c = moveLeft(mat)
    mat = transpose(mat)

    changed = changedOrNot(oldMat, mat)

    return mat, changed

def moveDown(mat) :
    oldMat = copyMatrix(mat)

    mat = transpose(mat)
    mat, c = moveRight(mat)
    mat = transpose(mat)

    changed = changedOrNot(oldMat, mat)

    return mat, changed