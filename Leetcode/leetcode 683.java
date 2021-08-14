// 题目大意：有n个花盆，第i天，第flowers[i]个花盆的花会开。问是否存在一天，两朵花之间有k个空花盆。
// https://zxi.mytechroad.com/blog/simulation/leetcode-683-k-empty-slots/
// Problem:

// There is a garden with N slots. In each slot, there is a flower. The N flowers will bloom one by one in N days. In each day, there will be exactly one flower blooming and it will be in the status of blooming since then.

// Given an array flowers consists of number from 1 to N. Each number in the array represents the place where the flower will open in that day.

// For example, flowers[i] = x means that the unique flower that blooms at day i will be at position x, where i and x will be in the range from 1 to N.

// Also given an integer k, you need to output in which day there exists two flowers in the status of blooming, and also the number of flowers between them is k and these flowers are not blooming.

// If there isn’t such day, output -1.

// Example 1:

// Input: 
// bulbs: [1,3,2]
// K: 1
// Output: 2
// Explanation:
// On the first day: bulbs[0] = 1, first bulb is turned on: [1,0,0]
// On the second day: bulbs[1] = 3, third bulb is turned on: [1,0,1]
// On the third day: bulbs[2] = 2, second bulb is turned on: [1,1,1]
// We return 2 because on the second day, there were two on bulbs with one off bulb between them.
// Example 2:

// Input: 
// bulbs: [1,2,3]
// K: 1
// Output: -1

class Solution {
    public int kEmptySlots(int[] flowers, int k) {
        int n = flowers.length;
        if (n == 0 || k >= n) return -1;
        int[] f = new int[n + 1];
        
        for (int i = 0; i < n; ++i)
            if (IsValid(flowers[i], k, n, f))
                return i + 1;
        
        return -1;
    }
    
    private boolean IsValid(int x, int k, int n, int[] f) {
        f[x] = 1;
        if (x + k + 1 <= n && f[x + k + 1] == 1) {
            boolean valid = true; 
            for (int i = 1; i <= k; ++i)
                if (f[x + i] == 1) {
                    valid = false;
                    break;
                }
            if (valid) return true;
        }
        if (x - k - 1 > 0 && f[x - k - 1] == 1) {
            for (int i = 1; i <= k; ++i)
                if (f[x - i] == 1) return false;
            return true;
        }
        return false;
    }
}

// https://www.youtube.com/watch?v=CnGzY0qfewE
// 思想：本质上是一个找一个有效的window，两边的值比中间k的值都小。如果有多个有效的天，返回最小的。
class Solution2 {
    public int kEmptySlots(int[] flowers, int k) {
        int n = flowers.length;
        int[] position = new int[n + 1];
        for(int i = 0; i < n; i++) {
            position[flowers[i]] = i;
        }

        int res=  Integer.MAX_VALUE;
        int lo = 1, hi = 2 + k;
        for (int i = 1; hi <= n; i++) {
            if(position[i] > position[lo] && position[i] > position[hi])
                continue;
            
            if(i == hi) {
                res = Math.min(res, Math.max(position[lo], position[hi]) + 1);
            }
            lo = i;
            hi = i + k + 1;
        }

        return res == Integer.MAX_VALUE ? -1 : res;
    }
}