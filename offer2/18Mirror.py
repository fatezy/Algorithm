# 题目描述
# 操作给定的二叉树，将其变换为源二叉树的镜像。
from offer.tree_helper import *

class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        if root:
            root.left,root.right = root.right,root.left
            self.Mirror(root.left)
            self.Mirror(root.right)
        return root

    def Mirror2(self,root):
        if not root:
            return None
        # python 大法好
        root.left,root.right = self.Mirror2(root.right),self.Mirror2(root.left)
        return root


if __name__ == '__main__':
    tree = biTree([8,6,10,5,7,9,11])
    root = tree.creat()
    Solution().Mirror2(root)
    print(1)

