# nums to words

ones= ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
       'nine','ten', 'eleven', 'twelve' ,'thirteen', 'fourteen', 'fifteen',
       'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens= ['','', "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty",
            "ninety"]

def num_driver(num):
    z = num % 10    # ones
    y = ((num % 100) - z) // 10 # tens
    x = ((num % 1000) - (y * 10) - z) // 100 # hundreds
    return x,y,z

def num2word(num):
    strNum = ""
    a,b,c = num_driver(num)
    if a != 0 : strNum += ones[a] + "hundred"
    if b == 0 and c == 0:
        return strNum
    if strNum != "" : strNum += "and"
    if b<=1:
        strNum+=ones[b*10 + c]
    else:
        strNum+=tens[b]+ones[c]

    return strNum

def get_sum():
    sum = 0
    for i in range(1,1000):
        sum += len(num2word(i))
    return sum + 11

def main():
    print(get_sum())


if __name__ == '__main__':
    main()
