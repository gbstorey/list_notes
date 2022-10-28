import numpy as np
myArray = np.arange(1,20)

def findNumber(array, number):
    for i in range(len(array)):
        if array[i] == number:
            print(i)

findNumber(myArray, 13)
findNumber(myArray, 100)