def factorial(n):
    if n == 1 : return 1
    else : return n * (factorial (n-1))

def digitSum(n):
    sNum = str(n)
    sum = 0
    for char in sNum:
        sum += int(char)
    return sum

def main():
    print( digitSum ( factorial(100) ) )

if __name__ == '__main__':
    main()
