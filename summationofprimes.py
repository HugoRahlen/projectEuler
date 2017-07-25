# Sums all primes below two million
import itertools
import math
import csv

list = [2, 3, 5, 7]
cieling = 1000

def sumPrime(cieling, list):
    for i in  range((max(list) + 1), cieling):
        if i in list:
            continue
        else:
            if isdivisible(i, list) == True:
                list.append(i)
    else:
        print(len(list))
        return math.fsum(list)

def isdivisible(i, list): # Tries if i is divisible by any earlier prime in list
    test = []
    for j in range(len(list)):
        if (i % list[j] == 0):
            return False
    return True

def prime_sum(n):
    if n < 2: return 0
    if n == 2: return 2
    if n % 2 == 0: n += 1
    primes = [True] * n
    primes[0], primes[1] = [None] * 2
    sum = 0
    for ind,val in enumerate(primes):
        if val is True and ind > n ** 0.5 + 1:
            sum += ind
        elif val is True:
            primes[ind*2::ind] = [False] * (((n - 1 // ind ) - 1))
            sum += ind
    return sum

#primeFile(list)
print(prime_sum(cieling))
