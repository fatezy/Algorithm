# 给定一个
# N
# 叉树，返回其节点值的前序遍历。
#
# 例如，给定一个
# 3
# 叉树:
#
# 返回其前序遍历: [1, 3, 5, 6, 2, 4]。
#
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        self.res = []
        self.helper(root)
        return self.res

    def helper(self, root):
        if not root:
            return
        if root:
            self.res.append(root.val)
            children = root.children
            for i in range(len(children)):
                self.helper(children[i])


