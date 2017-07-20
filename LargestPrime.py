# gives largest prime facor of a number

Number = 600851475143

def milli141(n): # quickest
    i = 2
    while i * i < n:
        while n % i == 0:
            n = n / i
        i += 1
    return n

def biggestFactor(number): # never completed
    prime = True
    for i in reversed(range(2, number, 2)):
        if number % i == 0:
            if isprime_divisor(i) == True:
                return i


def factorize(number): # never completed
    prime = True
    check = 0
    factors = []
    nfactors = []
    for i in range(2, number):
        if number % i == 0:
            if isprime_divisor(i) == True:
                factors.append(i)
            else:
                factors.extend(iter(factorize(i)))

    return sorted(list(set(factors)), reverse=True)

def isprime_divisor(n): # never completed
    n*=1.0
    if n%2==0 and n!=2 or n%3==0 and n!=3:
        return False
    for i in range(1, int(((n ** 0.5) + 1)/6.0 + 1)):
        if n%(6*i-1)==0:
            return False
        if n%(6*i+1)==0:
            return False
    return True

print(milli141(Number))
'''
for a in range(2, 100):
    if isprime(a):
        print(a)
'''
