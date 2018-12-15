# 计算给定二叉树的所有左叶子之和。
#
# 示例：
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# 在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24


class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        t = 0
        if root.left and not root.left.left and not root.left.right:
            t = root.left.val

        l = self.sumOfLeftLeaves(root.left)
        r = self.sumOfLeftLeaves(root.right)
        return t+l+r






