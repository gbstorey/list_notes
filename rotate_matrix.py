
myMatrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

def rotate_matrix(myMatrix):
    newMatrix = [
        [],
        [],
        []
    ]
    numRows = len(myMatrix)
    for n in range(numRows):
        for i in range(numRows):
            newMatrix[i].append(myMatrix[numRows-n][i])
    return newMatrix

print(rotate_matrix(myMatrix))