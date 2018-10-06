# 输入一棵二叉树，判断该二叉树是否是平衡二叉树。

from offer.tree_helper import *
class Solution:
    def IsBalanced_Solution(self, pRoot):
        if not pRoot:
            return True,0
        l,ld = self.IsBalanced_Solution(pRoot.left)
        r,rd = self.IsBalanced_Solution(pRoot.right)

        if l and r:
            return (True,max(ld,rd)+1) if abs(ld -rd) <= 1 else  (False,-1)

        return False,-1

if __name__ == '__main__':
    tree = biTree([1,2,3,4,5,'#','#','#','#',6])
    root = tree.creat()
    a = Solution().IsBalanced_Solution(root)
    print(a[0])
