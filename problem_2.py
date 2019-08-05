def sum_even_fibonacci_lt(lessThan):
    i = 1 ; j = 1 ; current = 0 ; sum = 0
    while current < lessThan:
        current = i + j
        i = j ; j = current
        if current % 2 == 0 : sum += current
    return sum

print (sum_even_fibonacci_lt(10))