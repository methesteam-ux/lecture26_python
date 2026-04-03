number_list = [23, 45, 27, 11, 25, 65, 78]

def getIndex(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
        
def getMax(arr):
    maxnum = arr[0]
    for i in arr:
        if maxnum < i:
            maxnum = i
    
    return maxnum

def getMin(arr):
    minnum = arr[0]
    for i in arr:
        if minnum > i:
            minnum = i
    
    return minnum

def countGT(arr, target):
    count = 0
    for i in arr:
        if i > target:
            count += 1

    return count

def sumList(arr):
    count = 0
    for i in arr:
        count += i

    return count

def swapList(arr):
    global number_list
    temp = []
    
    for i in range(-1, -1-len(arr), -1):
        temp.append(arr[i])

    number_list = temp

print(getIndex(number_list, 25))
print(getMax(number_list))
print(getMin(number_list))
print(countGT(number_list, 42))
print(sumList(number_list))
swapList(number_list)
print(number_list)