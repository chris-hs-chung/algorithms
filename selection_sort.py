stuff = [4,533,5,-12,34,2,-66,777,0,1,48,456,-444]

def find_smallest(arr):
    smallest = arr[0]
    smallestIndex = 0
    arrayLength = len(arr)
    for i in range(1, arrayLength):
        if arr[i] < smallest:
            smallest = arr[i]
            smallestIndex = i
    return smallestIndex

def selection_sort(arr):
    newArr = []
    arrLength = len(arr)
    for i in range(arrLength):
        smallestIndex = find_smallest(arr)
        newArr.append(arr.pop(smallestIndex))
    return newArr
        

print(selection_sort(stuff))
