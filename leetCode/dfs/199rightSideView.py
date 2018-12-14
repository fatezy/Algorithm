# 给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
#
# 示例:
#
# 输入: [1,2,3,null,5,null,4]
# 输出: [1, 3, 4]
# 解释:
#
#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---

from offer.tree_helper import *
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        queue = [root]
        res = []

        while(queue):
            level_queue = queue[::]
            queue = []
            res .append(level_queue[-1].val)
            for i in range(len(level_queue)):
                if level_queue[i].left:
                    queue .append(level_queue[i].left)
                if level_queue[i].right:
                    queue .append(level_queue[i].right)
        return res



if __name__ == '__main__':
    tree = biTree( [1,2,3,'#',5,'#',4])
    root = tree.creat()
    print(Solution().rightSideView(root))




