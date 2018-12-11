# 给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例:
# 给定如下二叉树，以及目标和 sum = 22，
#
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \      \
#         7    2      1
# 返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。


class Solution:

    def hasPathSum(self,root,sum):
        if not root:
            return False
        if not root.left  and not root.right and root.val == sum:
            return True
        return self.hasPathSum(root.left,sum-root.val) or self.hasPathSum(root.right,sum-root.val)

    def hasPathSum2(self, root, sum):
        """求的是从根节点到叶子节点，这种方法过不了
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        return self.helper(root,sum)

    def helper(self,root,sum):
        if not root:
            if sum == 0:
                return True
            return False
        if root:
            l = self.helper(root.left, sum - root.val)
            r = self.helper(root.right, sum - root.val)
            return l or r