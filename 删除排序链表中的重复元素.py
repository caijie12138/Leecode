'''
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

示例 1:

输入: 1->1->2
输出: 1->2
示例 2:

输入: 1->1->2->3->3
输出: 1->2->3
'''
#链表去重
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        q = head
        dic = {head.val: 1}
        while(p.next!=None):
            p = p.next
            if p.val in dic and p.next!=None:
                continue
            if p.val==q.val and p.next==None:
                q.next = None
                break
            else:
                q.next = p
                q = p
                dic[p.val] = 1
        return head

if __name__=='__main__':
    a = Solution()
    new = ListNode(1)
    p = ListNode(1)
    # q = ListNode(1)
    r = ListNode(2)
    s = ListNode(3)
    t = ListNode(3)
    new.next = p
    p.next = r
    # q.next = r
    r.next = s
    s.next = t
    res = a.deleteDuplicates(new)
    while res != None:
        print(res.val)
        res = res.next
