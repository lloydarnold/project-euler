def multiply(list):
    prod = 1
    for char in list:
        prod *= int(char)
    return prod


def read_grid():
    fEuler = open("res/prob_11_grid")
    grid = []
    for line in fEuler:
        tempLine = []
        for item in line[:-1]:
            if item != " ":
                tempLine.append(item)
        grid.append(tempLine)
    return grid


def vertical_seq(grid, root=(0,0), runLength=4):
    product = 1
    for i in range(0, runLength):
        try:
            product *= grid[root[0]][root[1] + i]
        except Exception as e:
            return product
    return product


def horizontal_seq(grid, root=(0,0), runLength=4):
    product = 1
    for i in range(0, runLength):
        try:
            print(grid[root[0] + i][root[1]])
            product *= grid[root[0] + i][root[1]]
        except Exception as e:
            return product
    print(product)
    return product


def diagl_seq(grid, root=(0,0), runLength=4):
    product = 1
    for i in range(0, runLength):
        try:
            product *= grid[root[0] - i][root[1] + i]
        except Exception as e:
            return product
    return product


def diagr_seq(grid, root=(0,0), runLength=4):
    product = 1
    for i in range(0, runLength):
        try:
            product *= grid[root[0] + i][root[1] + i]
        except Exception as e:
            return product
    return product


def move_pointers(grid, runLength=4):
    width = len(grid[0])
    height = len(grid)
    max = 0
    for i in range(0, width):
        for j in range(height):
            # i = x coord, j = y coord
            temp = horizontal_seq(grid, (i,j))
            if temp == max:
                 max = temp
            temp = vertical_seq(grid, (i,j), runLength)
            if temp > max : max = temp
            temp = diagl_seq(grid, (i,j), runLength)
            if temp > max : max = temp
            temp = diagr_seq(grid, (i,j), runLength)
            if temp > max : max = temp

    return max


def main():
    grid = read_grid()
    print(grid)
    print(move_pointers(grid, 4))

if __name__ == '__main__':
    main()
