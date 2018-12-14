# 根据一棵树的中序遍历与后序遍历构造二叉树。
#
# 注意:
# 你可以假设树中没有重复的元素。
#
# 例如，给出
#
# 中序遍历 inorder = [9,3,15,20,7]
# 后序遍历 postorder = [9,15,7,20,3]
# 返回如下的二叉树：
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
from offer.tree_helper import *
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        使用和前序遍历和中序遍历类似的方法
        前序遍历的顺序为 中 左 右
        后序遍历的顺序的逆序为中 右 左
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            ind = inorder.index(postorder.pop())
            root = TreeNode(inorder[ind])
            root.right = self.buildTree(inorder[ind+1:],postorder)
            root.left = self.buildTree(inorder[:ind],postorder)
            return root




