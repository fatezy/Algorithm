# 二叉树层序遍历
from offer.tree_helper import TreeNode
import queue

class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        q_node = queue.Queue()
        res = []
        if root:
            q_node.put(root)

        while not q_node.empty():
            temp = q_node.get()

            res.append(temp.val)

            if  temp.left:
                q_node.put(temp.left)
            if  temp.right:
                q_node.put(temp.right)


        return res


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left =TreeNode(4)
    root.left.right =TreeNode(5)
    Solution().PrintFromTopToBottom(root)






