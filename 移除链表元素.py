删除链表中等于给定值 val 的所有节点。

示例:

输入: 1->2->6->3->4->5->6, val = 6
输出: 1->2->3->4->5

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head == None:
            return None
        while head.val == val:
            if head.next != None:
                head = head.next
            else:
                return None
        p = head
        q = head
        res = q
        if p.next != None:
            p = p.next
        while p:
            if p.val==val and p.next!=None:
                q.next = p.next
                p = p.next
            elif p.val!=val and p.next!=None:
                q = p
                p = p.next
            elif p.val==val and p.next==None:
                q.next = None
                p = None
            else:
                return res
        return res





