/**
Solution1: https://www.youtube.com/watch?v=Eqhu29_NTSs
TC:O(M*N)
SC:O()
best version:
"abc" -> "1,1"
"acf" -> "2,3"


suppose w1 has same inword shifting pattern with w2
Map<String, List<String>>
3. Coding
4. Testing
findPattern("abc") -> "1,1"
patternWordsMap ={
 "1,1" : ["abc", "bcd", "xyz"]
 "2,2,1" : ["acef"]
 "25," : ["az", "ba"]
 "," : ["a", "z"]
}
 */


class Solution {
    
    private String findPattern(String word) {
        if(word.length() == 0)
            return "";
        if(word.length() == 1)
            return ",";
        
        StringBuilder pattern = new StringBuilder();
        for(int i = 0; i < word.length() - 1; i++) {
            int diff = word.charAt(i + 1) - word.charAt(i);
            if(diff < 0)
                diff += 26;
            pattern.append(diff + ",");
        }
        return pattern.toString();
    }
    
    public List<List<String>> groupStrings(String[] strings) {
        List<List<String>> ret = new LinkedList<>();
        if(string.length == 0)
            return ret;
        
        Map<String, List<String>> patternWordsMap = new HashMap<>();
        for(String word : strings) {
            Stirng pattern = findPattern(word);
            if (!patternWordsMap.containsKey(pattern)) {
                patternWordsMap.put(pattern, new LinkedList<>());

            }
            patternWordsMap.get(pattern).add(word);
        }
        
        for(String pattern: patternWordsMap.keySet()) {
            ret.add(patternWordsMap.get(pattern));
        }
        return ret;
    }
}