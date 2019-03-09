请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true
进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

#O(n)时间 O(1)空间
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pRev = None
        pCur = head
        while pCur!=None:
            pTemp = pCur
            pCur = pCur.next
            pTemp.next = pRev
            pRev = pTemp
        return pRev

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head==None:
            return True
        elif head.next==None:
            return True
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if not fast:
            mid = slow
        else:
            mid = slow.next
        new_head = self.reverseList(mid)
        while head and new_head:
            if head.val != new_head.val:
                return False
            else:
                head = head.next
                new_head = new_head.next
        return True


