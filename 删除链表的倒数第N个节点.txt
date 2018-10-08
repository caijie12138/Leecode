# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        count = 0
        one = head
        while (one != None):
            one = one.next
            count += 1
        if count == 1:
            return None
        if count == 2 and n == 2:
            return head.next
        if count == 2 and n == 1:
            head.next = None
            return head
        index = count - n
        p = head
        q = p.next
        count1 = 0
        while (p != None and q != None):
            if index == 0:
                head = head.next
                return head
            if count1+1 == index:
                p.next = q.next
                q = q.next
                break
            p = p.next
            q = q.next
            count1 += 1
        return head
        
