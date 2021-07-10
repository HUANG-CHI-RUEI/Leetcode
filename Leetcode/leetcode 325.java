/**
Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.
Note:
The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.
 Example 1:
Given nums = [1, -1, 5, -2, 3], k = 3,
return 4. (because the subarray [1, -1, 5, -2] sums to 3 and is the longest)
Naive Approach: Consider the sum of all the sub-arrays and return the length of the longest sub-array having sum 'k'. Time Complexity is of O(n^2).
Efficient Approach: Following are the steps:
1.Initialize sum = 0 and maxLen = 0.
2.Create a hash table having (sum, index) tuples.
3.For i = 0 to n-1, perform the following steps:
    1.Accumulate arr[i] to sum.
    2. If sum == k, update maxLen = i+1.
    3..Check whether sum is present in the hash table or not. If not present, then add it to the hash table as (sum, i) pair.
    4.Check if (sum-k) is present in the hash table or not. If present, then obtain index of (sum-k) from the hash table as index. Now check if maxLen < (i-index), then update maxLen = (i-index).
4.Return maxLen.
 */

import java.io.*;
import java.util.*;
 
class Solution {

     public int maxSubArrayLen(int[] nums, int k) {
            HashMap<Integer, Integer> map = new HashMap<>();
            map.put(0, -1);

            int sum = 0, maxLen = 0;
            for(int i = 0; i < nums.length; i++) {
                sum += nums[i];
                if(map.contiansKey(sum - k)) {
                    result = Math.max(result, i - map.get(sum - k));
                }
                map.putIfAbsent(sum, i);
            }

            return result;
    }
 
      // Driver code
      public static void main(String args[]){
            int[] arr = {10, 5, 2, 7, 1, 9};
            int n = arr.length;
            int k = 15;
            System.out.println("Length = " +
                    maxSubArrayLen(arr, n, k));
      }
}

// 1, -1, 5, -2, 3  ;k = 3
// (0, -1) (-2, 0) (-3, 1) (2, 2) 
// (0, 3)  = > result = i - map.get(0) = 3-(-1) = 4

// {10, 5, 2, 7, 1, 9} k = 15
// map: {(10, 0) (15, 1)} = > result = 2
// (17, 2) (24, 3 (25, 4)) => 25-15 = 10 True , then (i - map.get(10)) = 4 - 0 = 4 is result