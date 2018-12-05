# 给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例:
# 给定如下二叉树，以及目标和 sum = 22，
#
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
# 返回:
#
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]

from offer.tree_helper import *
class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        self.helper(root,res,[],sum)
        return res

    def helper(self, root, res, temp_list, remain):
        if not root:
            return
        if not root.left and not root.right and remain == root.val:
            temp_list.append(root.val)
            res.append(temp_list[:])
            temp_list.pop()
            return

        if root:
            temp_list.append(root.val)
            print(root.val)
            self.helper(root.left, res, temp_list, remain - root.val)
            self.helper(root.right, res, temp_list, remain - root.val)
            temp_list.pop()




if __name__ == '__main__':
    tree = biTree([5,4,8,11,'#',13,4,7,2,'#','#',5,1])
    root = tree.creat()
    print(Solution().pathSum(root, 22))



