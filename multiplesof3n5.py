# lists all multiples of 3 or 5 below the specified number and adds them
from tkinter import Tk

print('Enter range')

sum = 0
range = int(input())

def multiples(range, sum):
    i = 0
    while i < range:
        if (i % 3 == 0) or (i % 5 == 0):
            sum = sum + i
            print(i)
        i = i + 1

    print('Sum = ' + str(sum) + '. Copying sum to clipboard.')
    return sum

Tk(str(multiples(range, sum)))
