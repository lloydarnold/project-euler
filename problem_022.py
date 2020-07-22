import ast

def getNames():
    fNames = open("res/p022_names.txt", "r")
    raw = "[" + fNames.read() + "]"
    return ast.literal_eval(raw)

def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        while low <= high and array[high] >= pivot:
            high = high - 1

        while low <= high and array[low] <= pivot:
            low = low + 1

        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break

    array[start], array[high] = array[high], array[start]

    return high

def quickSort(array, start, end):
    if start >= end:
        return

    p = partition(array, start, end)
    quickSort(array, start, p-1)
    quickSort(array, p+1, end)

def cleanNames():
    names=getNames()
    quickSort(names, 0, len(names)-1)
    return names

def scoreName(name):
    score = 0
    for letter in name:
        score += ord(letter)-64
    return score

def main():
    names = cleanNames()
    sum = 0
    for i, name in enumerate(names):
        sum += scoreName(name) * (i+1)
    print(sum)

if __name__ == '__main__':
    main()
