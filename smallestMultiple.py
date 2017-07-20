# finds the smallest number that can be evenly divisible by all numbers through 1 to 20

divRange = 20

def cycle(divRange): # Whoop!
    n = 1
    test = []
    while set(test) != {True}:
        test = []
        for i in range(1, divRange + 1):
            if n % i == 0:
                test.append(True)
                #print(n, i, n%i, set(test))
            else:
                test.append(False)
                #print(n, i, n%i, set(test))
                break
        n += 1
    return n - 1

print(str(cycle(divRange)))
