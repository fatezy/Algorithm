# 给定两个二叉树，编写一个函数来检验它们是否相同。
#
# 如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
#
# 示例 1:
#
# 输入:       1         1
#           / \       / \
#          2   3     2   3
#
#         [1,2,3],   [1,2,3]
#
# 输出: true
# 示例 2:
#
# 输入:      1          1
#           /           \
#          2             2
#
#         [1,2],     [1,null,2]
#
# 输出: false
# 示例 3:
#
# 输入:       1         1
#           / \       / \
#          2   1     1   2
#
#         [1,2,1],   [1,1,2]
#
# 输出: false

from offer.tree_helper import *
class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        if not p or not q:
            return False
        p_queue = [p]
        q_queue = [q]
        while p_queue and q_queue:
            temp1 = p_queue.pop(0)
            temp2 = q_queue.pop(0)
            if temp1.val != temp2.val:
                return False
            if (temp1.left and not temp2.left) or (not temp1.left and  temp2.left) or (temp1.right and  not temp2.right) or (not temp1.right and temp2.right):
                return False
            if temp1.left:
                p_queue.append(temp1.left)
            if temp1.right:
                p_queue.append(temp1.right)
            if temp2.left:
                q_queue.append(temp2.left)
            if temp2.right:
                q_queue.append(temp2.right)
        return True


    def isSameTree2(self,p,q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p and q:
            m =  p.val == q.val
            l = self.isSameTree2(p.left,q.left)
            r = self.isSameTree2(p.right,q.right)
            return l and r and m



if __name__ == '__main__':
    tree1 = biTree([1,2,3])
    tree2 = biTree([1,2,3])
    root1 = tree1.creat()
    root2 = tree2.creat()
    print(Solution().isSameTree2(root1, root2))
