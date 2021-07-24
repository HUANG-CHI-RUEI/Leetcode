import java.util.HashMap;

// 1. HashMap:
// TC: O(n).
// SC: O(n)

public class Solution {
    public int lengthOfLongestSubstringKDistinct(String s, int k) {
        HashMap<Character, Integer> map = new HashMap<>();
        int max = 0, start = 0;

        for(int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            map.put(c, map.getOrDefault(c, 0) + 1);
            while(map.size() > k) {
                char tmp = s.charAt(start);
                if(map.get(tmp) == 1) {
                    map.remove(tmp);
                } else {
                    map.put(tmp, map.get(tmp) - 1);
                }
                start++;
            }
            max = Math.max(max, i - start + 1);
        }
        return max;
    }
}

// 2. sliding window(array)
// TC:O(n)
// SC:O(128) = 1

public class Solution {
    public int lengthOfLongestSubstringKDistinct(String s, int k) {
        int[] count = new int[128];
        int maxLen = 0;
        for(int lo = 0, hi = 0, numDistinct = 0; hi < s.length(); i++) {
            char letter = s.charAt(hi);
            if(count[letter] == 0) numDistinct++;
            count[letter]++;
            while(numDistinct > k) {
                letter = s.charAt(start);
                count[letter]--;
                if(count[letter] == 0) numDistinct--;
            }
            maxLen = hi - lo + 1;
        }
        return maxLen;
    }
}