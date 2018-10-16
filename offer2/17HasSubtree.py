# 输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）

from offer.tree_helper import *
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        res = False
        if pRoot1 and pRoot2:
            if pRoot1.val == pRoot2.val:
                res = self.helper(pRoot1,pRoot2)
            if not res:
                res = self.helper(pRoot1.left,pRoot2)
            if not res:
                res = self.helper(pRoot1.right,pRoot2)
            return res


    def helper(self,pRoot1,pRoot2):
        if not pRoot2:
            return True
        if not pRoot1:
            return False

        if pRoot1.val != pRoot2.val:
            return False
        else:
            left = self.helper(pRoot1.left,pRoot2.left)
            right = self.helper(pRoot1.right,pRoot2.right)
            return left and right


