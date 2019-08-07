def is_palindrome_int(num):
    intRev = int( str(num)[::-1] )
    if num == intRev :
        return True
    else: return False

if __name__ == "__main__":

    palindromes = []
    for n in range (900, 999) : 
      for m in range (900, 999) :
        if is_palindrome_int(n*m) : palindromes.append(n*m)
    print(palindromes)