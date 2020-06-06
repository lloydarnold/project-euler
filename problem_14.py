''' collatz :: (Integral a) => a -> [a]
collatz 1 = [1]
collatz n
        | even n = n:collatz (n `div` 2)
        | odd n  = n:collatz (3*n + 1)

maximum' :: (Ord a) => [a] -> a
maximum' [] = error "Error, list empty"
maximum' [x] = x
maximum' (x:xs) = max x (maximum' xs)

eulerSolution :: Int
eulerSolution = maximum' (map length (map collatz [1..1000000]))
'''

def gen_map():
    return [-1 for i in range(0,1000000) ]


def nCollatz(n):
    if n%2 == 0:
        return int(n/2)
    else:
        return 3*n +1


def collatz(root, map, counter):
    nextNum = nCollatz(root)
    temp = map[nextNum]
    if temp != -1:
        return temp + counter
    else:
        return collatz(nextNum, map, counter+1)


def driver():
    map = gen_map()
    max = 0
    for i in range(0,len(map)):
        temp = collatz(i, map, 0)
        map[i] = temp
        if temp > max : max = temp
    return max


def main():
    print(driver())


if __name__ == '__main__':
    main()
