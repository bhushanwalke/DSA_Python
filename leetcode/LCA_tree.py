# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        while root != None:
            if (p.val < root.val < q.val) or (p.val > root.val > q.val):
                return root
            if p.val < root.val:
                root = root.left
            else:
                root = root.right
