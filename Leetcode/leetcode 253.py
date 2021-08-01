# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],…] (si < ei), 
# find the minimum number of conference rooms required.

# Input: [[0, 30],[5, 10],[15, 20]]
# Output: 2

# Input: [[7,10],[2,4]]
# Output: 1
# https://www.youtube.com/watch?v=FdzJmTCVyJU
"""
TC:O(nlogn)
SC:O(n)
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
class Solution:
    def minMeetingRooms(self, intervals):
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals]
        
        res, count = 0, 0
        s, e = 0, 0
        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            res = max(res, count)

        return res


'''
2. Heap: https://www.youtube.com/watch?v=NDToQ-nbguE&list=PL7O5Ubado0Q3azAJdEtqREuHj13d-fCR0&index=5&ab_channel=%E4%BB%8A%E5%A4%A9%E6%AF%94%E6%98%A8%E5%A4%A9%E5%8E%B2%E5%AE%B3
TC:O(nlogn)
SC:O(n)
'''
from heapq import *
class Solution:
    def minMeetingRooms(self, intervals):
        # edge check:
        if not intervals:
            return 0

        intervals.sort()
        rooms = []
        heapq.heappush(rooms, intervals[0][1])
        i = 1

        while i < len(intervals):
            if rooms[0] <= intervals[i][0]:
                heapq.heappop(room)
            heapq.heappush(rooms, intervals[i][1])
            i += 1
            
        return len(rooms)