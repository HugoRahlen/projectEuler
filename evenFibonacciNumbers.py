# Sum of all even Fibonacci numbers up to 4 million
print('Enter range: ')
range = int(input())

def Fibonacci(range):

    fib_1 = 1
    fib_2 = 2
    sum = 0

    print(fib_1)

    while fib_2 < range:
        fib_temp = fib_1
        if fib_2 % 2 == 0:
            sum = sum + fib_2
        fib_1 = fib_2
        fib_2 = fib_2 + fib_temp
        print(fib_1)
    print('The sum of all even numbers in the Fibonacci series are: ' + str(sum))
    return sum

Fibonacci(range)
#print('Sum = ' + str(Fibonacci())
