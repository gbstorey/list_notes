# Creation
integers = [1,2,3,4]
print(integers)
stringList = ['Milk', 'Cheese', 'Butter']
print(stringList)
mixedList = [1, 1.5, 'spam']
print(mixedList)
nestedList = [1,2,3,4, [1.5, 1.6, 1.7], ['test']]
print(nestedList)
empty  = []

# Accessing/Traversal
shoppingList = ['Milk', 'Cheese', 'Butter']
print(shoppingList[0])
print('Bread' in shoppingList)
print(shoppingList[-2])
for i in shoppingList:
    print(i)
for i in range(len(shoppingList)):
    shoppingList[i] += "+"
print(shoppingList)

#Update/Insert
#Updating list item: O(1)
myList = [1,2,3,4,5,6,7]
print(myList)
myList[2] = 33
print(myList)
#insert()
#insert in beginning: O(n) Space: O(1)
myList.insert(0, 0)
print(myList)
#append()
#O(1) Space: O(1)
myList.append(55)
print(myList)
#extend()
#O(n) Space: O(n)
secondList = [55,56,57]
myList.extend(secondList)
print(myList)

#Slice/Delete
myList = ['a', 'b', 'c', 'd', 'e', 'f']
print(myList[0:2])
print(myList[:2])
print(myList[1:])
myList [0:2] = ['x', 'y']
print(myList[:])
#pop() O(n) Space: O(1)
myList.pop(1)
print(myList)
#last item O(1)
popped = myList.pop()
print(popped)
#del O(n) Space: O(1)
del myList[1]
print(myList)
del myList [0:2]
print(myList)
#remove() O(n) Space: O(1)
myList.remove('e')
print(myList)

#Searching for values
myList = [10,20,30,40,50,60,70,80,90]

if 20 in myList:
    print(True)

def searchInList(list, value): #O(n) Space: O(1)
    for i in list:
        if i == value:
            return list.index(value)
    return 'The value does not exist in the list.'

print(searchInList(myList, 20))

#List operations and list functions
list1 = [1,2,3]
list2 = [4,5,6]
print(list1+list2)
print(list1*4)
print(len(list1))
print(max(list1))
print(min(list1))
print(sum(list1))
average = (sum(list1)/len(list1))
print(average)

numbers = []

while (True):
    inp = input('Enter a number, or "done" if you are ready for average: ')
    if inp == "done": break
    else: numbers.append(float(inp))
print("The average is: " + str(sum(numbers) / len(numbers)))

#Lists and strings
a = 'spam spam spam'
b = list(a)
print(b)
c = a.split()
print(c)
adash = "spam-spam-spam"
d = adash.split("-")
print(d)
print("-".join(d))

#List Pitfalls
myList = [2,4,3,1,5,7]
myList = myList.sort()
print(myList)
myList = [2,4,3,1,5,7]
myList = myList + [10]
print(myList)
myList.append([10])
print(myList)

myList = [2,4,3,1,5,7]
orig = myList
print(orig)
myList.sort()
print(myList)
myList = [2,4,3,1,5,7]
print(sorted(myList))
print(myList)

fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
fruit_list2 = fruit_list1
fruit_list3 = fruit_list1[:]
 
fruit_list2[0] = 'Guava'
fruit_list3[1] = 'Kiwi'
 
sum = 0
for ls in (fruit_list1, fruit_list2, fruit_list3):
    print(ls)
    if ls[0] == 'Guava':
        sum += 1
    if ls[1] == 'Kiwi':
        sum += 20
 
print(sum)