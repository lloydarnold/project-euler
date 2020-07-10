## Tree traversal let's max it out

def getTree():
    fTree = open("res/prob_18_tree")
    tempTree = fTree.readlines()
    fTree.close()
    return formatTree(tempTree)

def formatTree(rawTree):
    newTree = []
    intRow = []
    for row in rawTree:
        tempRow = row.split(" ")
        for entry in tempRow:
            intRow.append(int(entry))
        newTree.append(intRow)
        intRow = []
    return newTree

def treeToMatrix(rawTree):
    paddedMatrix = []
    maxLen = len(rawTree[-1])
    for row in rawTree:
        for i in range(len(row), maxLen):
            row.append(0)
        paddedMatrix.append(row)
    return paddedMatrix

def compress(matrix):
    if len(matrix) == 1:
        print(matrix[0][0])
    else:
        for i, value in enumerate(matrix[-2]):
            if value == 0 : break
            value += max(matrix[-1][i], matrix[-1][i + 1] )
            matrix[-2][i] = value
        matrix = compress(matrix[0:-1])

def main():
    matrix = treeToMatrix(getTree())
    compress(matrix)

if __name__ == '__main__':
    main()
