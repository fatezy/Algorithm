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

class Solution:
    def flatten(self, root):
        """
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