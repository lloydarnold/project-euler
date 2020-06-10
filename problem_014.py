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

# max recursion depth is exceeded hmm
# let's do it non recursive then ig

def gen_map():
    return [0 for i in range(0,10000000) ]  # map is one OoM larger than max (just in case)


def nCollatz(n):
    if n%2 == 0:
        return int(n/2)
    else:
        return 3*n +1


def collatz(root, map):
    counter = 0
    nextNum = nCollatz(root)
    thisSequence = [nextNum]
    temp = 0
    while temp  == 0 and thisSequence[-1] != 1:
        counter += 1
        thisSequence.append(nCollatz(thisSequence[-1]))
        try : temp = map[thisSequence[-1]]
        except : temp = 0

    fVal = counter + map[thisSequence[-1]]
    map[root] = fVal
    return fVal

def driver():
    map = gen_map()
    max = (0,0)
    for i in range(1, 1000000):
        temp = collatz(i, map)
        map[i] = temp
        if temp > max[0] : max = (temp, i)
    return max[1]


def main():
    print(driver())


if __name__ == '__main__':
    main()
