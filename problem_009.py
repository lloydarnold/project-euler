# pythTrips = [(a, b, c) | c <- [300..1000], b <- [1..c], a <- [1..b],
#               a^2 + b^2 == c^2, a + b + c == 1000]

def prodTrip (a,b,c):
    return a * b * c

def driver():
    for c in range (333, 1000):
        for b in range(1, c):
            for a in range (1, b):
                if a+b+c == 1000 and a**2 + b**2 == c**2:
                    print(prodTrip(a,b,c))
                    return

def main():
    driver()

if __name__ == '__main__':
    main()
