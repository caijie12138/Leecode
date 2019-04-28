'''
给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回锯齿形层次遍历如下：

[
  [3],
  [20,9],
  [15,7]
]
'''
#其实思路很简单 就是把之前层次遍历的结果拿过来 之后再进行单行和双行的区分并反向就行
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        d = {}
        def helper(root,lv):
            if not root:
                return
            if lv not in d:
                d[lv] = [root.val]
            else:
                d[lv].append(root.val)
            helper(root.left,lv+1)
            helper(root.right,lv+1)
        helper(root,1)
        return [d[x] if i%2==0 else d[x][::-1] for i,x in enumerate(d)]
