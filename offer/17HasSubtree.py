# 输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
from offer.tree_helper import TreeNode

class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        result = False

        if pRoot1 is not None and pRoot2 is not None:
            if pRoot1.val == pRoot2.val:
                result = self.DoesTreeHasTree2(pRoot1,pRoot2)

            if not result:
                result = self.HasSubtree(pRoot1.left,pRoot2)

            if not result:
                result = self.HasSubtree(pRoot1.right,pRoot2)

            return result

    def DoesTreeHasTree2(self,pRoot1,pRoot2):
        if not pRoot2:
            return True

        if not pRoot1:
            return False

        if pRoot1.val != pRoot2.val:
            return False

        return self.DoesTreeHasTree2(pRoot1.left,pRoot2.left) and self.DoesTreeHasTree2(pRoot1.right,pRoot2.right)




