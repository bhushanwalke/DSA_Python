# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.rightview(root, res, 0)

        return res

    def rightview(self, root, res, currdepth):
        if not root:
            return
        if currdepth == len(res):
            res.append(root.val)

        self.rightview(root.right, res, currdepth+1)
        self.rightview(root.left, res, currdepth+1)
