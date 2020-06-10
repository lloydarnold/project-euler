## sum of multiples of 3 or 5 < 1000

def sum_multiples_lt(multOf, lessThan):
    i = 0 ; j = 0 ; sum = 0
    while j < lessThan:
        sum += j ; i += 1 ; j = i * multOf
    return sum

totalSum = sum_multiples_lt(3, 1000) + sum_multiples_lt(5, 1000)
for i in range (1, 67):
  totalSum -= 15 * i

print(totalSum)