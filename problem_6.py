def sumSquares(n):
    sum = 0
    for i in range (0, n + 1):
        sum += i*i

    return sum

def squareSum(n):
    sum = 0
    for i in range (0,n+1):
        sum += i
    return sum*sum

def main():
    print(squareSum(100) - sumSquares(100))

if __name__ == "__main__":
    main()
