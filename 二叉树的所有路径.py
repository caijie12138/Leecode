'''
给定一个二叉树，返回所有从根节点到叶子节点的路径。

说明: 叶子节点是指没有子节点的节点。

示例:

输入:

   1
 /   \
2     3
 \
  5

输出: ["1->2->5", "1->3"]

解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        def getpath(root,path):
            if root == None:
                return None
            path += str(root.val)
            if root.left != None:
                getpath(root.left,path+'->')
            if root.right != None:
                getpath(root.right,path+'->')
            if root.left == None and root.right == None:
                res.append(path)
        getpath(root,'')
        return res
