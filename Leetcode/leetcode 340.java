// This is a problem asked by Google.
// Given a string, find the longest substring that contains only two unique characters. 
// For example, given "abcbbbbcccbdddadacb",
// the longest substring that contains 2 unique character is "bcbbbbcccb".

// 1. HashMap:
// TC: O(n).
// SC: O(n)



public class Solution {
    public int lengthOfLongestSubstringKDistinct(String s, int k) {
        HashMap<Character, Integer> count = new HashMap<>();
        int max = 0, start = 0;
        if(k == 0)
            return 0;
            
        for(int i = 0; i < s.legnth(); i++) {
            char c = s.charAt(i);
            count.put(c, map.getOrDefault(c, 0) + 1);

            while(count.size() > k) {
                char tmp = s.charAt(start);
                if(count.get(tmp) == 1) {
                    count.remove(tmp);
                } else {
                    count.put(tmp, count.get(tmp) - 1);
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
        int[] couunt = new int[128];
        int maxLen = 0;
        for(int lo = 0, hi = 0, numDistinct = 0; hi < s.length(); hi++) {
            char letter = s.charAt(hi);
            if(count[letter] == 0) numDistinct++;
            count[letter]++;

            while(numDistinct > k) {
                letter = s.charAt(lo++);
                count[letter]--;
                if(count[letter] == 0) numDistinct--;
            }

            maxLen = hi - lo + 1;
        }
        return maxLen;
    }
}
