# Sums all primes below two million
import itertools
import math

list = [2, 3, 5, 7]
cieling = 100

def sumPrime(cieling, list):
    for i in  range((max(list) + 1), cieling):
        if i < cieling:
            if i in list:
                continue
            else:
                if isdivisible(i, list) == True:
                    list.append(i)
        else:
            print(i)
            return math.fsum(list)

def isdivisible(i, list): # Tries if i is divisible by any earlier prime
    test = []
    for j in range(len(list)):
        if (i % list[j] == 0):
            test.append(False)
            return False
        else:
            test.append(True)

def findsN(n, list):
    for i in itertools.count((max(list) + 1), 1):
        if i in list:
            continue
        else:
            if isdivisible(i, list) == True:
                list.append(i) # adds new prime to list of primes
        #print(list)
        #print(i)
        if len(list) == n:
            return i, len(list)


print(sumPrime(cieling, list))
