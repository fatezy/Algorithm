# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
#
# 百度百科中最近公共祖先的定义为：“对于有根树
# T
# 的两个结点
# p、q，最近公共祖先表示为一个结点
# x，满足
# x
# 是
# p、q
# 的祖先且
# x
# 的深度尽可能大（一个节点也可以是它自己的祖先）。”
#
# 例如，给定如下二叉树: root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]
#
# 示例
# 1:
#
# 输入: root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], p = 5, q = 1
# 输出: 3
# 解释: 节点
# 5
# 和节点
# 1
# 的最近公共祖先是节点
# 3。
from offer.tree_helper import *
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root or p == root or q == root:
            return root
        l = self.lowestCommonAncestor(self.lowestCommonAncestor(root.left,p,q))
        r = self.lowestCommonAncestor(self.lowestCommonAncestor(root.right,p,q))
        if l and r:                 # 在不同子树上
            return root
        return l if l else r        # 在同一子树上 或 返回上一层





    def lowestCommonAncestor2(self, root, p, q):
        """ 超时
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        fathers = []
        self.findFather(root,p,q,fathers,[])
        size = min(len(fathers[0]), len(fathers[1]))
        for i in range(size):
            if fathers[0][i] !=fathers[1][i]:
                return fathers[0][i - 1]
        return fathers[0][size-1]

    def findFather(self,root,target1,target2,res,temp):
        if not root:
            return





        if root:
            if root == target1 or root == target2:
                temp.append(root)
                res.append(temp[::])
            self.findFather(root.left,target1,target2,res,temp + [root])
            self.findFather(root.right,target1,target2,res,temp + [root])


if __name__ == '__main__':
    tree = biTree([3,5,1,6,2,0,8,'#','#',7,4])
    root = tree.creat()
    res = []
    # print(Solution().lowestCommonAncestor2(root, root.left, root.left.right.right).val)
    print(Solution().lowestCommonAncestor2(root, root.left, root.right).val)


