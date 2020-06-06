def load_nums():
    nums = []
    fNums = open("res/prob_13_nums")
    for tempNum in fNums:
        nums.append(int(tempNum))

    return nums

def big_sum(numList):
    firstTen = 0
    for num in numList:
        firstTen += num / 10**38

    return str(firstTen)[:10]


def main():
    print(big_sum(load_nums()))


if __name__ == '__main__':
    main()
