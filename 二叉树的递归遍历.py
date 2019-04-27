#中序：
class Solution(object):
    def dfs(self,root,a):
        if root:
            self.dfs(root.left,a)
            a.append(root.val)
            self.dfs(root.right,a)
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        a = []
        if root == None:
            return a
        self.dfs(root,a)
        return a

#前序：
class Solution(object):
    def front(self,root,a):
        if root:
            a.append(root.val)
            self.front(root.left,a)
            self.front(root.right,a)
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        a = []
        if root == None:
            return a
        self.front(root,a)
        return a

#后序：
class Solution(object):
    def after(self,root,a):
        if root:
            self.after(root.left,a)
            self.after(root.right,a)
            a.append(root.val)

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        a = []
        if root==None:
            return a
        self.after(root,a)
        return a
