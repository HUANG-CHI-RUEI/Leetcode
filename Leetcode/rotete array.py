# https://www.geeksforgeeks.org/array-rotation/

# METHOD 2 (Rotate one by one)
# TC:O(n*d)
# SC:O(1)

def leftRotate(arr, d, n):
    for i in range(d):
        leftRotateByOne(arr, n)

def leftRotateByOne(arr, n):
    temp = arr[0]
    for i in range(n-1):
        arr[i] = arr[i+1]
    arr[n-1] = temp

def printArray(arr, size):
    for i in range(size):
        print ("% d"% arr[i], end =" ")

arr = [1, 2, 3, 4, 5, 6 ,7]
n = len(arr)
d = 2
leftRotate(arr, d, n)
printArray(arr, n)

# https://www.geeksforgeeks.org/program-for-array-rotation-continued-reversal-algorithm/
# Method 4 (The Reversal Algorithm) :
# TC:O(n)
# SC:O(1)

def leftRotate(arr, d):
    if  d == 0:
        return

    n = len(arr)

    d = d % n
    reverseArray(arr, 0, d-1)
    reverseArray(arr, d, n-1)
    reverseArray(arr, 0, n-1)

def reverseArray(arr, start, end):
    while start < end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -= 1

def printArray(arr):
    for i in range(0, len(arr)):
        print(arr[i])

arr = [1, 2, 3, 4, 5, 6, 7]
n = len(arr)
d = 2
  
leftRotate(arr, d)  # Rotate array by 2
printArray(arr)