# 题目描述
# # 输入一颗二叉树的跟节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
# 路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。(注意: 在返回值
# 的list中，数组长度大的数组靠前)

from offer.tree_helper import *
class Solution:
    def __init__(self):
        self.res = []
        self.temp = []
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):

        if  not root and expectNumber == 0:
            if self.temp:
                self.res.append(self.temp.copy())

        if root:
            self.temp.append(root.val)
            self.FindPath(root.left,expectNumber-root.val)
            self.temp.pop()

        if root:
            self.temp.append(root.val)
            self.FindPath(root.right,expectNumber-root.val)
            self.temp.pop()

        return self.res[::2]




if __name__ == '__main__':
    tree = biTree([10,5,12,4,7])
    root = tree.creat()
    print(Solution().FindPath(root, 22))




