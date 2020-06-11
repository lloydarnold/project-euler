def powers(n,i):
    if n == 0 : return 0
    if i == 0 : return 1
    if i%2 == 0 :
        return powers(n, i // 2) * powers(n, i // 2)
    else :
        return n * powers(n, i-1)

def digitSum(n):
    sNum = str(n)
    sum = 0
    for char in sNum:
        sum += int(char)
    return sum

def main():
    print(digitSum(powers(2, 1000)))


if __name__ == '__main__':
    main()
