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