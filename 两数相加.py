# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

# 示例：

# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        lis1 = []
        lis2 = []
        while l1:
            lis1.append(l1.val)
            l1 = l1.next
        while l2:
            lis2.append(l2.val)
            l2 = l2.next
        res = ''
        plus = 0
        if len(lis1) == 1 and len(lis2) == 1 and int(lis1[0]) + int(lis2[0]) >= 10:
            return [(int(lis1[0]) + int(lis2[0])) % 10, 1]
        if len(lis1) > len(lis2):
            for i in range(len(lis1) - len(lis2)):
                lis2.append(0)
        elif len(lis1) < len(lis2):
            for i in range(len(lis2) - len(lis1)):
                lis1.append(0)
        for i, j in zip(lis1, lis2):
            if int(i) + int(j) + plus >= 10:
                res += str((int(i) + int(j) + plus) % 10)
                plus=0
                plus += 1
            else:
                res += str(int(i) + int(j) + plus)
                plus = 0
        last = ListNode(int(res[0]))
        start = last
        for i in res[1::]:
            last.next = ListNode(i)
            last = last.next
        if plus == 1:
            last.next = ListNode(1)
        return start
