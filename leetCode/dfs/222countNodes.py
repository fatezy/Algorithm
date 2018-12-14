# 给出一个完全二叉树，求出该树的节点个数。
#
# 说明：
#
# 完全二叉树的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层，则该层包含 1~ 2h 个节点。
#
# 示例:
#
# 输入:
#     1
#    / \
#   2   3
#  / \  /
# 4  5 6
#
# 输出: 6

class Solution(object):

    def countNodes(self, root):
        leftdepth = self.getdepth(root, True)
        rightdepth = self.getdepth(root, False)

        if leftdepth == rightdepth:
            return 2 ** leftdepth - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def getdepth(self, root, isLeft):
        if root is None:
            return 0
        if isLeft:
            return 1 + self.getdepth(root.left, isLeft)
        else:
            return 1 + self.getdepth(root.right, isLeft)


    def countNodes4(self, root):
        """ 该算法超时
        :type root: TreeNode
        :rtype: int
        """
        self.count = 0
        if not root:
            return 0

        def dfs(root):
            if not root:
                return
            if root:
                self.count = self.count + 1
                dfs(root.left)
                dfs(root.right)
                return self.count
        return dfs(root)

    def countNodes2(self,root):
        """
        上个算法写法的优化改写版本，依然超时
        :param root:
        :return:
        """
        if not root:
            return 0
        if root:
            l = self.countNodes2(root.left)
            r = self.countNodes2(root.right)
            return l+r+1

    def countNodes3(self, root):
        """ 优化了一下代码，依然超时
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        l = root
        r = root

        h = 0
        while not r:
            l = l.left
            r = r.right
            h = h + 1

        if not l:
            return (2 ** h) - 1

        return 1 + self.countNodes3(root.left) + self.countNodes3(root.right)
