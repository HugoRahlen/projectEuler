# Sums all primes below two million
import itertools
import math
import csv

list = [2, 3, 5, 7]
cieling = 2000000

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

def primeFile(list):
    with open('primes.csv', 'w', newline='') as csvfile:
        primewriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        primewriter.writerow(list)

primeFile(list)
#print(sumPrime(cieling, list))
