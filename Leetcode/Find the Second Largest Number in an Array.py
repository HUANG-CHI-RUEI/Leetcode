# TC:O(nlogn)
# SC:O(1)

def print2largest(arr, arr_size):
    
    if arr_size < 2:
        print("Invalid Input")
        return

    arr.sort()

    for i in range(arr_size-2, -1, -1):
        
        if(arr[i] != arr[arr_size - 1]) :
            print("The second largest element is", arr[i])
            return
    print("There is no second largest element")



# TC:O(n)
# SC:O(1)
def print2largest2(arr, arr_size):
    if arr_size < 2:
        return
    
    first = second = float('-inf')
    for i in range(arr_size):
        if(arr[i] > first):
            second = first
            first = arr[i]
        elif arr[i] > second and arr[i] != first:  
            second = arr[i]

    return second == float('-inf') ? "" : second



# Driver code
arr = [12, 35, 1, 10, 34, 1]
n = len(arr)
print2largest(arr, n)
 