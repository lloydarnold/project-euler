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

def primeFactors(n):
    relPrimes = sieve(int(math.sqrt(n)+1))
    factors = []
    i = 0
    while True:
        if n % relPrimes[i] == 0:
            factors.append(relPrimes[i])
            if n == relPrimes[i]:
                return factors

            n /= relPrimes[i]
            i = 0
        else:
            i += 1

def main():
    print(max(primeFactors(600851475143)))

if __name__ == "__main__":
    main()
