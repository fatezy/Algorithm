# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。
#
# 假设一个二叉搜索树具有如下特征：
#
# 节点的左子树只包含小于当前节点的数。
# 节点的右子树只包含大于当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。
# 示例 1:
#
# 输入:
#     2
#    / \
#   1   3
# 输出: true
# 示例 2:
#
# 输入:
#     5
#    / \
#   1   4
#      / \
#     3   6
# 输出: false
# 解释: 输入为: [5,1,4,null,null,3,6]。
#      根节点的值为 5 ，但是其右子节点值为 4 。
from offer.tree_helper import *
import sys
class Solution:

    def isValidBST(self,root):
        return self.helper(root,-1*sys.maxsize,sys.maxsize)


    def helper(self,root,minval,maxVal):
        if not root:
            return True
        if root:
            if root.val<= minval or root.val >= maxVal:
                return False
            l = self.helper(root.left,minval,root.val)
            r = self.helper(root.right,root.val,maxVal)
            return l and r




    def isValidBST2(self, root):
        """
        没有考虑到 [10,5,15,null,null,6,20]这种情况
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if root:
            l = self.isValidBST(root.left)
            r = self.isValidBST(root.right)
            flag = l and r
            if root.left:
                if root.val<=root.left.val:
                    return False
            if root.right:
                if root.val >= root.right.val:
                    return False
            return flag


if __name__ == '__main__':

    tree = biTree([1, 1])
    root = tree.creat()
    print(Solution().isValidBST(root))







