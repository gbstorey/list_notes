myList = [1,20,30,44,5,56,57,8,19,10,31,12,13,14,35,16,27,58,21]

def is_unique(myList):
    items = {}
    for num in myList:
        if num in items.keys():
            return False
        else:
            items[num] = 1
    return True

print(is_unique(myList))

