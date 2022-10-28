import numpy as np
myArray = np.array([1, 20, 30, 44, 5, 56, 57, 8 , 9 , 10, 31, 12, 13 , 14, 35, 16 , 27, 58, 19, 21])

def max_product(myArray):
    product = 0
    for i in range(len(myArray)):
        for j in range(i+1, len(myArray)):
            if myArray[i]*myArray[j] > product:
                product = myArray[i]*myArray[j]
                pairs = (myArray[i],myArray[j])
    return (product, pairs)
print(max_product(myArray))