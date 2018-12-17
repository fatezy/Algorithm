# 给定一个二叉树，在树的最后一行找到最左边的值。
#
# 示例
# 1:
#
# 输入:
#
# 2
# / \
#     1
# 3
#
# 输出:
# 1
#
# 示例
# 2:
#
# 输入:
#
# 1
# / \
#     2
# 3
# / / \
#     4
# 5
# 6
# /
# 7
#
# 输出:
# 7

from offer.tree_helper import *
class Solution:
    def findBottomLeftValue(self, root): # 层序遍历，最后一层的最后一个就是结果
        """ 本题假设root不为空
        :type root: TreeNode
        :rtype: int
        """
        queue = [root]
        while queue:
            temp_queue = queue[::]
            queue = []
            for i in range(len(temp_queue)):
                if  temp_queue[i].left:
                    queue.append(temp_queue[i].left)
                if  temp_queue[i].right:
                    queue.append(temp_queue[i].right)
            if not queue:
                return temp_queue[0].val
        return root.val

    def findBottomLeftValue2(self, root):
        self.max_level = 0
        self.val = None
        self.helper(root, 1)
        return self.val

    def helper(self, root, level):
        if not root:
            return
        if level > self.max_level:
            self.max_level = level
            self.val = root.val
        self.helper(root.left, level + 1)
        self.helper(root.right, level + 1)
if __name__ == '__main__':
    tree = biTree([2,1,3])
    root = tree.creat()
    print(Solution().findBottomLeftValue2(root))



