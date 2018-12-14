# 给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。
#
# 说明：
# 你可以假设 k 总是有效的，1 ≤ k ≤ 二叉搜索树元素个数。
#
# 示例 1:
#
# 输入: root = [3,1,4,null,2], k = 1
#    3
#   / \
#  1   4
#   \
#    2
# 输出: 1
# 示例 2:
#
# 输入: root = [5,3,6,2,4,null,null,1], k = 3
#        5
#       / \
#      3   6
#     / \
#    2   4
#   /
#  1
# 输出: 3

from offer.tree_helper import *
class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int 总是有效的
        :rtype: int
        """
        res = []

        def dfs(root):   # 中序遍历
            if not root:
                return
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)

        dfs(root)
        return res[k-1]

if __name__ == '__main__':
    tree = biTree([3,1,4,'#',2])
    root = tree.creat()
    print(Solution().kthSmallest(root, 1))





