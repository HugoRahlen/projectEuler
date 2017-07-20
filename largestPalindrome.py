# Find the largest palindrome made from the product of two 3-digit numbers.

a = 1000

def checkPalin(x, y):
    number = x * y
    if str(number)[::-1] == str(number):
        return True
    else:
        return False

def cycleRange(a): # Slow, but it works!
    biggest = [0, 0, 0]
    for i in range(a):
        for j in range(a):
            if checkPalin(i, j) == True and i*j > biggest[2]:
                biggest = [i, j, i*j]
            print(biggest)
    return biggest

def cycleRangeRev(a): # finds a lower number, probably because it does not check that it's the biggest number.
    for i in reversed(range(a)):
        for j in reversed(range(a)):
            if checkPalin(i, j) == True:
                return i, j, i * j

print(cycleRange(a))
