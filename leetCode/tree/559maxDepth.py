# 给定一个
# N
# 叉树，找到其最大深度。
#
# 最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。
#
# 例如，给定一个
# 3
# 叉树:
#
# 我们应返回其最大深度，3。
#
# 说明:
#
# 树的深度不会超过
# 1000。
# 树的节点总不会超过
# 5000。

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        if not root.children:
            return 1
        children_length = []   #用于存储子节点的深度
        for i in range(len(root.children)):
            children_length.append(self.maxDepth(root.children[i]))
        return max(children_length)+1