# Finds the n-th prime
import itertools

N = 10001
primes = [2, 3, 5, 7, 11]

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

def isdivisible(i, list): # Tries if i is divisible by any earlier prime
    test = []
    for j in range(len(list)):
        if (i % list[j] == 0):
            test.append(False)
            return False
        else:
            test.append(True)
    #print(set(test), i)
    #print(j)
    #if False not in test:
    return True

print(findsN(N, primes))
