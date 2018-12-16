# 给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater Tree)，使得每个节点的值是原来的节点值加上所有
# 大于它的节点值之和。
#
# 例如：
#
# 输入: 二叉搜索树:
#               5
#             /   \
#            2     13
#
# 输出: 转换为累加树:
#              18
#             /   \
#           20     13
from offer.tree_helper import *
class Solution:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.preCount = 0
        self.helper(root)
        return root


    def helper(self,root):
        if not root:
            return
        if root:
            self.helper(root.right)
            root.val += self.preCount
            self.preCount = root.val
            self.helper(root.left)


if __name__ == '__main__':
    tree = biTree([5,2,13])
    root = tree.creat()
    Solution().convertBST(root)
