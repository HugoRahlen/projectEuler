# solves for the difference of the sum of the squares and the square of the sum

sqRange = 100

def sumofsquare(n):
    sum = 0
    for i in range(n):
        b = i + 1
        sum = sum + (b * b)
    return sum

def squareofsum(n):
    sum = 0
    for i in range(n):
        b = i + 1
        sum = sum + b
    return (sum * sum)

print(squareofsum(sqRange) - sumofsquare(sqRange))
