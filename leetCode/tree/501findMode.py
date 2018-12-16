# 给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。
#
# 假定 BST 有如下定义：
#
# 结点左子树中所含结点的值小于等于当前结点的值
# 结点右子树中所含结点的值大于等于当前结点的值
# 左子树和右子树都是二叉搜索树
# 例如：
# 给定 BST [1,null,2,2],
#
#    1
#     \
#      2
#     /
#    2
# 返回[2].
from offer.tree_helper import *
class Solution:
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.max_count = -1
        self.res = []
        self.pre = -1
        self.count = 0
        self.helper(root)
        return self.res

    def helper(self, root):
        if not root:
            return
        if root:
            self.helper(root.left)

            if root.val == self.pre:
                self.count += 1
            else:
                self.count = 1
                self.pre = root.val

            if self.count == self.max_count and root.val != self.res[-1]:
                    self.res.append(root.val)

            if self.count > self.max_count:
                self.max_count = self.count
                self.res = []
                self.res.append(root.val)
        self.helper(root.right)

if __name__ == '__main__':
    tree = biTree([1,'#',2,2])
    root = tree.creat()
    print(Solution().findMode(root))