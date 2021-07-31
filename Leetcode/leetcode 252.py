# Meeting Rooms
# Given an array of meeting time intervals consisting of start and end times [s1, e1], [s2, e2], ... , determine if a person could attend all meetings.

# For example,
# Given [ [0, 30], [5, 10], [15, 20] ],
# return false.
# https://www.youtube.com/watch?v=WFyzgWs9Vyc


# How to determine overlap?
# second first must less than first end.

# So we need to sort first

# TC:O(n) + O(nlogn)
# SC:O(n) :sort() mergesort in python


def Solution(intervals: List[List[int]])  -> bool:
    intervals.sort() # O(nlogn)
    i = 1

    while i < len(intervals): # O(n)
        if intervals[i][0] < intervals[i-1][1]:
            return False
        i += 1

    return True   