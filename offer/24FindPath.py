# 输入一颗二叉树的跟节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
# 路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。(注意:
# 在返回值的list中，数组长度大的数组靠前

class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
       result = []
       if not root:
           return result

       if not root.left and not root.right and root.val ==expectNumber:
           return [[root.val]]
       else:
           left = self.FindPath(root.left, expectNumber - root.val)
           right = self.FindPath(root.right, expectNumber - root.val)
           for item in left + right:
               result.append([root.val] + item)
           return result








