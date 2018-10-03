# 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
# 要求不能创建任何新的结点，只能调整树中结点指针的指向。
from offer.tree_helper import *


class Solution:
    def Convert(self, pRootOfTree):
        if not pRootOfTree:
            return None
        res = self.helper(pRootOfTree)
        for i in range(len(res)):
            if i != 0:
                res[i].left =res[i-1]
            if i != len(res)-1:
                res[i].right = res[i+1]

        return res[0]

    def helper(self,pRootOfTree):
        if not pRootOfTree:
            return []

        res =[]

        left= self.helper(pRootOfTree.left)
        res = left + [pRootOfTree]
        right = self.helper(pRootOfTree.right)
        res = res + right

        return res



if __name__ == '__main__':
    tree = biTree([10,6,14,4,8,12,16])
    root = tree.creat()
    res = Solution().Convert(root)
    print(1)


