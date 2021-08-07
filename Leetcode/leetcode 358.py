'''
https://www.youtube.com/watch?v=DT--N9p_O4Y
Given a non-empty string str and an integer k, rearrange the string such that the same characters are at least distance k from each other.
All input strings are given in lowercase letters. If it is not possible to rearrange the string, return an empty string "".
Example 1:
str = " ", k = 3
Result: "abcabc"
The same letters are at least distance 3 from each other.
Example 2:
str = "aaabc", k = 3
Answer: ""
It is not possible to rearrange the string.
Example 3:
str = "aaadbbcc", k = 2
Answer: "abacabcd"
Another possible answer is: "abcabcda"
The same letters are at least distance 2 from each other.
'''

class Solution(object):
    def rearrangeString(self, s: str, k: int) -> str:
        if k == 0: return s

        counter = collection.Counter(s)

        # convert minheap to maxheap: {'a': 3, 'b' : 2, 'c' : 1} => {-3 : 'a' , -2: 'b', -1: 'c'}
        pq = [(-counter[c], c) for c in counter]
        heap.heapify(pq)
        
        ans = ""
        
        while pq:
            temp_list = []
            
            # aaabc -> pq=[a,b,c] -> pq['-2': a] 長度小於k 且 a大於1個
            if len(pq) < k and -pq[0][0] > 1:
                return ""

            for _ in range(min(k, len(pq))): # 可能 pq 不足k 個元素
                cur_item = heapq.heappop(pq)
                count = -cur_item[0]
                c = cur_item[1]

                ans += c
                count -= 1

                #put visited element to temp_list
                if count:
                    temp_list.append((count, c))

            # push reamin part into heap
            for count, c in temp_list:
                heapq.heappush(pq, (count, c))

        return ans