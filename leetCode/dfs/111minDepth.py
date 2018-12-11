# 给定一个二叉树，找出其最小深度。
#
# 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例:
#
# 给定二叉树 [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回它的最小深度  2.
from offer.tree_helper import *
class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if root:
            left = self.minDepth(root.left)
            right = self.minDepth(root.right)
            if (left == 0 or right ==0) and (left !=0 or right !=0):
                return max(left,right)+1
            return left+1 if left<right else right+1



if __name__ == '__main__':
    tree = biTree([1, 2])
    root = tree.creat()
    print(Solution().minDepth(root))
