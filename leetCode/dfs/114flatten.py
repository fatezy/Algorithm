# 给定一个二叉树，原地将它展开为链表。
#
# 例如，给定二叉树
#
#     1
#    / \
#   2   5
#  / \   \
# 3   4   6
# 将其展开为：
#
# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6

from offer.tree_helper import *
class Solution:
    def flatten(self, root):
        """使用了一个辅助列表，空间复杂度比较高
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        node_list = []
        self.helper(root,node_list)
        if len(node_list) >=2:
            for i in range(len(node_list)-1):
                node_list[i].left = None
                node_list[i].right = node_list[i+1]

    def helper(self,root,node_list):
        if not root:
            return
        if root:
            node_list.append(root)
            self.helper(root.left,node_list)
            self.helper(root.right,node_list)


    def flatten2(self,root):  # 有些难以理解
        self.pre = None
        self.helper2(root)

    def helper2(self,root): # 这种遍历方式，右左中 可以理解为前序遍历的逆序遍历
        if not root:
            return
        self.helper2(root.right)
        self.helper2(root.left)
        root.right = self.pre
        root.left = None
        self.pre = root


if __name__ == '__main__':
    tree = biTree([1,2,5,3,4,'#',6])
    root = tree.creat()
    Solution().flatten2(root)

