# 给定一个二叉树，计算整个树的坡度。
#
# 一个树的节点的坡度定义即为，该节点左子树的结点之和和右子树结点之和的差的绝对值。空结点的的坡度是0。
#
# 整个树的坡度就是其所有节点的坡度之和。
#
# 示例:
#
# 输入:
#          1
#        /   \
#       2     3
# 输出: 1
# 解释:
# 结点的坡度 2 : 0
# 结点的坡度 3 : 0
# 结点的坡度 1 : |2-3| = 1
# 树的坡度 : 0 + 0 + 1 = 1

from offer.tree_helper import *
class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.helper(root)
        return self.res
    def helper(self,root):
        """

        :param root:
        :return: int 当前节点的子树和当前节点的和
        """
        if not root:
            return 0
        l = self.helper(root.left)
        r = self.helper(root.right)
        self.res += abs(l-r)  # 计算当前节点的梯度

        return l+r+root.val

if __name__ == '__main__':
    tree = biTree([1,2,3,4,5,6,7])
    root = tree.creat()
    print(Solution().findTilt(root))