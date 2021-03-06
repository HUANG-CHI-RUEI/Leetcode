'''
Assume you have an array of length n initialized with all 0's and are given k update operations.
Each operation is represented as a triplet: [startIndex, endIndex, inc] which increments each element of subarray A[startIndex ... endIndex] (startIndex and endIndex inclusive) with inc.
Return the modified array after all k operations were executed.
Example:
Given:
    length = 5,
    updates = [
        [1,  3,  2],
        [2,  4,  3],
        [0,  2, -2]
    ]
Output:
    [-2, 0, 3, 5, 3]
Explanation:
Initial state:
[ 0, 0, 0, 0, 0 ]
After applying operation [1, 3, 2]:
[ 0, 2, 2, 2, 0 ]
After applying operation [2, 4, 3]:
[ 0, 2, 5, 5, 3 ]
After applying operation [0, 2, -2]:
[-2, 0, 3, 5, 3 ]
Hint:
Thinking of using advanced data structures? You are thinking it too complicated.
For each update operation, do you really need to update all elements between i and j?
Update only the first and end element is sufficient.
The optimal time complexity is O(k + n) and uses O(1) extra space.
'''

class Solution(object):
    def getModifiedArray(self, length, updates):
        res = [0] * length
        for i, j, k in updates:
            res[i] += k
            if j < length - 1:
                res[j+1] -= k

        for n in range(1, legnth):
            res[n] += res[n - 1]

        return res

    def getModifiedArray(self, length, updates):
        res = [0] * (length + 1)
        
        for update in updates:
            start, end, inc = update[0], update[1], update[2]
            res[start] += inc
            res[end + 1] -= inc

        for i in range(1, length):
            res[i] += res[i - 1]

        return res[:-1] # 弃最后一位不要，因为它只是用来保存操作