# 给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
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
# 例如，给定如下二叉搜索树: root = [6, 2, 8, 0, 4, 7, 9, null, null, 3, 5]
#
# 示例
# 1:
#
# 输入: root = [6, 2, 8, 0, 4, 7, 9, null, null, 3, 5], p = 2, q = 8
# 输出: 6
# 解释: 节点
# 2
# 和节点
# 8
# 的最近公共祖先是
# 6。
# 示例
# 2:
#
# 输入: root = [6, 2, 8, 0, 4, 7, 9, null, null, 3, 5], p = 2, q = 4
# 输出: 2
# 解释: 节点
# 2
# 和节点
# 4
# 的最近公共祖先是
# 2, 因为根据定义最近公共祖先节点可以为节点本身。
from offer.tree_helper import *

class Solution:

    def lowestCommonAncestor(self, root, p, q):
        while root:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return root

    def lowestCommonAncestor1(self, root, p, q): # 这种写法一直通不过，不知道是什么原因
        """ 所有节点是唯一的
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        p_father = []
        self.helper(root,p_father,p,[])
        q_father = []
        self.helper(root,q_father,q,[])
        size = min(len(p_father),len(q_father))
        for i in range(size):
            if p_father[i] != q_father[i]:
                return p_father[i-1]
        # return p_father[size-1]




    def helper(self,root,res,q,temp):
        """
        找出根节点到子节点的路径
        :param root:
        :param res:
        :param q:
        :return:
        """
        if not root:
            return
        if root.val == q:
            temp.append(root)
            res +=temp[::]
            return
        if root:
            temp.append(root)
            self.helper(root.left,res,q,temp)
            self.helper(root.right,res,q,temp)
            temp.pop()






if __name__ == '__main__':
    tree = biTree([6,2,8,0,4,7,9,'#','#',3,5])
    root = tree.creat()

    res = Solution().lowestCommonAncestor(root,2,8)
    print(res.val)




