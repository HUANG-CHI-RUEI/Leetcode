# Given a non-negative number represented as a singly linked list of digits, plus one to the number.

# The digits are stored such that the most significant digit is at the head of the list.

# Input:
# 1->2->3

# Output:
# 1->2->4
#1. iterately: https://github.com/KrisYu/LeetCode-CLRS-Python/blob/master/369.Plus%20One%20Linked%20List.md
# TC:O(n)
# SC:O(1)
class Solution:
    def plusOne(self, head):
        lst = []
        cur = head

        while cur:
            lst.append(cur)
            cur = cur.next

        carry = 1
        for i in range(len(lst)-1, -1, -1):
            lst[i].val += carry 
            if lst[i].val < 10:
                carry = 0
                break
            else:
                lst[i].val -= 10

        if carry == 1:
            node = ListNode(1)
            node.next = head
            return node
        else:
            return head
            
# 2. https://www.youtube.com/watch?v=bURKdgHpiUM&ab_channel=TechZoo

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        not_nine = dummy

        # find the rightmost not-nine digit
        while head:
            if head.val != 9:
                not_nine = head
            head = head.next

        not_nine.val += 1
        not_nine = not_nine.next

        # mean the rightmost is 9
        while not_nine:
            not_nine.val = 0 # mean plus 1, 9+1 = 10
            not_nine = not_nine.next

        # 999 + 1 = 1000, 多一位，所以進入if條件
        if dummy.val:
            return dummy
        else: 
            return dummy.next

        


