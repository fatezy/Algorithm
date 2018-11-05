# 判断一个树是不是平衡二叉树
class Solution:
    def IsBalanced_Solution(self, pRoot):
        """
        1. 判断当前节点是否平衡
        2. 递归调用求节点深度的方法，判断左右子树的高度差是否小于等于1
        :param pRoot:
        :return:
        """
        if not pRoot:
            return True
        left = self.TreeDepth(pRoot.left)
        right = self.TreeDepth(pRoot.right)
        return True if abs(left-right)<= 1 else False


    def TreeDepth(self, pRoot):
        if not pRoot:
            return 0
        left = self.TreeDepth(pRoot.left)
        right = self.TreeDepth(pRoot.right)
        return left+1 if left >= right else right+1




