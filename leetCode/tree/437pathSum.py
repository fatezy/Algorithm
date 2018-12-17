# 二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。
#
# 示例：
#
# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
#
#       10
#      /  \
#     5   -3
#    / \    \
#   3   2   11
#  / \   \
# 3  -2   1
#
# 返回 3。和等于 8 的路径有:
#
# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3.  -3 -> 11
from offer.tree_helper import *
class Solution(object):

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        self.res = 0
        self.nodeList = []
        self.getAllNode(root)
        for i in range(len(self.nodeList)):
            self.helper(self.nodeList[i],sum)
        return self.res

    def getAllNode(self,root):
        if not root:
            return
        if root:
            self.nodeList.append(root)
            self.getAllNode(root.left)
            self.getAllNode(root.right)


    def helper(self,root,retain):
        if not root:
            return
        if retain == root.val:
            self.res += 1
            return

        self.helper(root.left,retain-root.val)
        self.helper(root.right,retain-root.val)
if __name__ == '__main__':
    tree = biTree([10,5,-3,3,2,'#',11,3,-2,'#',1])
    root = tree.creat()
    print(Solution().pathSum(root, 8))