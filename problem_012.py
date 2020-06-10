def triNums(limit):
    seq = []
    for n in range(0,limit):
        seq.append(n * n/2)
    return seq


def main():
    print(triNums(10))


if __name__ == '__main__':
    main()
