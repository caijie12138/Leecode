'''
给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。

假定 BST 有如下定义：

结点左子树中所含结点的值小于等于当前结点的值
结点右子树中所含结点的值大于等于当前结点的值
左子树和右子树都是二叉搜索树
例如：
给定 BST [1,null,2,2],

   1
    \
     2
    /
   2
返回[2].

提示：如果众数超过1个，不需考虑输出顺序
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.dic = {}
    def calcu(self,root):
        if root is None:
            return None
        if root.val not in self.dic:
            self.dic[root.val] = 1
        else:
            self.dic[root.val] += 1
        self.calcu(root.left)
        self.calcu(root.right)
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return None
        self.calcu(root)
        max_time = max(self.dic.values())
        return [i for i in self.dic if self.dic[i]==max_time]

