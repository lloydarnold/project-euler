## We'll be we'll be counting Sundays

def moveDayPointer(pointer, numOfDays):
    return

def main():
    oneHotDays = [0,0,0,0,0,0,1]  ## onehot encode days - 1 is Sunday
    months = [31,28,31,30,31,30,31,31,30,31,30,31]
    numOfSuns = 0
    
    ## root day -- Tuesday, January 1st, 1901
    dayPointer = 1
    monthPointer = 12

    for year in range(1901, 2002):
        for month in range(0,12):
            numOfSuns += oneHotDays[dayPointer]


if __name__ == '__main__':
    main()
