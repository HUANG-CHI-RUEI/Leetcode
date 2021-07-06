/**
 Given n points on a 2D plane, find if there is such a line parallel to y-axis that reflect the given points.

Example 1:
Given points = [[1,1],[-1,1]], return true.

Example 2:
Given points = [[1,1],[-1,-1]], return false.

Follow up:
Could you do better than O(n2)?

Hint:

Find the smallest and largest x-value for all points.
If there is a line then it should be at y = (minX + maxX) / 2.
For each point, make sure that it has a reflected point in the opposite side.

这道题主要是判断N个点是否沿某条线对称，
可以从提示看出来所有的点应该要满足 2Y = minX + maxX;
所以先把所有的点扫一遍存下来，找到minX和minX. 然后再扫一遍，判定是否点都是延直线对称的。 
时间复杂度O(n),空间复杂度O(n).
 */

public class Solution {
    public boolean isReflected(int[][] points) {
        int max = Integer.MIN_VALUE, min = Integer.MAX_VALUE;
        Set<String> set = new HashSet();
        for(int[] p: points) {
            set.add(p[0] + "," + p[1]);
            max = Math.max(p[0], max);
            min = Math.min(p[0], min);
        }

        int sum = min + max;
        for(int[] p: points) {
            if(!set.contains((sum - p[0]) + "," + p[1]) {
                return false;
            }
        }
        return true;
    }
}