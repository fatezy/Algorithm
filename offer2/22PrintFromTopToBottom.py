# 题目描述
# 从上往下打印出二叉树的每个节点，同层节点从左至右打印。

class Solution:

    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        res = []
        queue = []   # 队列

        if not root:
            return res

        queue.append(root)
        while queue:
            node = queue.pop(0)
            res.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return res