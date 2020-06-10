import math

def sieve(primesTo):
    upperLim = int(math.sqrt(primesTo)+1)
    prime = [True for i in range(0, primesTo+1)]
    p = 2
    while p < upperLim:
        if prime[p] == True:
            for i in range(p*2, primesTo+1, p):
                prime[i] = False
        p+=1

    prime[0] = False ; prime[1] = False
    nums = [ i for i in range(1, primesTo+1) if prime[i] ]

    return nums

def sum(list):
    fSum = 0
    for num in list:
        fSum += num
    return fSum

def main():
    print(sum(sieve(2000000)))

if __name__ == '__main__':
    main()
