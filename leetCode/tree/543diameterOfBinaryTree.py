# 给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过根结点。
#
# 示例 :
# 给定二叉树
#
#           1
#          / \
#         2   3
#        / \
#       4   5
# 返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。
#
# 注意：两结点之间的路径长度是以它们之间边的数目表示。


class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dianter = 0
        self.helper(root)
        return self.dianter

    def helper(self,root):
        if not root:
            return 0

        if root:
            l = self.helper(root.left)
            r = self.helper(root.right)
            if self.dianter < l+r:
                self.dianter = l+r
        return max(l,r)+1