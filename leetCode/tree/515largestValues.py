# 您需要在二叉树的每一行中找到最大的值。
#
# 示例：
#
# 输入:
#
#           1
#          / \
#         3   2
#        / \   \
#       5   3   9
#
# 输出: [1, 3, 9]

class Solution:
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        queue = [root]
        res.append(root.val)
        while queue:
            temp_queue = queue[::]
            queue = []
            max_value = -1*2**32
            for i in range(len(temp_queue)):
                if  temp_queue[i].left:
                    if temp_queue[i].left.val > max_value:
                        max_value = temp_queue[i].left.val
                    queue.append(temp_queue[i].left)
                if  temp_queue[i].right:
                    if temp_queue[i].right.val > max_value:
                        max_value = temp_queue[i].right.val
                    queue.append(temp_queue[i].right)
            res.append(max_value)
            max_value = -1*2**32

        return res[:-1]