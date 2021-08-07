// https://www.youtube.com/watch?v=28ASDBKFTxw
// Given a non-empty string str and an integer k, rearrange the string such that the same characters are at least distance k from each other.
// All input strings are given in lowercase letters. If it is not possible to rearrange the string, return an empty string "".

// Example 1:
// str = " ", k = 3
// Result: "abcabc"
// The same letters are at least distance 3 from each other.

// Example 2:
// str = "aaabc", k = 3
// Answer: ""
// It is not possible to rearrange the string.

// Example 3:
// str = "aaadbbcc", k = 2
// Answer: "abacabcd"
// Another possible answer is: "abcabcda"
// The same letters are at least distance 2 from each other.

// TC: O(klogm), m is number of chars
// SC: O(26) = O(1), use space of heap and lsit, but they don't greater than 26

Class Solution{
    public String rearrangeString(String s, int k) {
        if(k == 0 || s.length()  <= 1) return s;
        int[] map = new int[26];
        for(char c: s.toCharArray()) {
            map[c - 'a']++;
        }

        StringBuilder sb = new StringBuilder();
        PriorityQueue<int[]> heap = new PriorityQueue<>
        ((a, b) -> a[1] == b[1] ? a[0] - b[0] : b[1] - a[1]);

        for(int i = 0; i < 26; i++) {
            if(map[i] > 0) {
                heap.offer(new int[]{i, map[i]});
            }
        }

        while(!heap.isEmpty()) {
            List<Integer> list = new ArrayList<>();
            for(int i = 0; i < k; i++) {
                int[] cur = heap.poll();
                sb.append((char) (cur[0] + 'a'));
                list.add(cur[0]);

                if(heap.size() == 0) {
                    if(i != k - 1 && sb.length() != s.length())
                        return "";
                    break;
                }
            }

            for(int i: list) {
                if(--map[i] > 0) {
                    heap.offer(new int[]{i, map[i]});
                }
            }
        }

        return sb.toString();
    }
}