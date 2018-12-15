# 给定一个
# N
# 叉树，返回其节点值的层序遍历。 (即从左到右，逐层遍历)。
#
# 例如，给定一个
# 3
# 叉树:
#
# 返回其层序遍历:
#
# [
#     [1],
#     [3, 2, 4],
#     [5, 6]
# ]


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res  = []
        queue = [root]

        while queue:
            level_queue = queue[::]
            res.append([i.val for i in level_queue])
            queue = []
            for i in range(len(level_queue)):
                if not level_queue[i].children:
                    continue
                for j in range(len(level_queue[i].children)):
                    queue.append(level_queue[i].children[j])

        return res





