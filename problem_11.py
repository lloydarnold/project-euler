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

def main():
    print(read_grid())

if __name__ == '__main__':
    main()
