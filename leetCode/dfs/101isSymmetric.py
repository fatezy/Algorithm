# 给定一个二叉树，检查它是否是镜像对称的。
#
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
#
#     1
#    / \
#   2   2
#    \   \
#    3    3

class Solution:
    def isSymmetric(self, root):
        """判断二叉树是否为镜像二叉树，调用上题的是否为相同树的方法，中间的递归调用稍加修改即可

        深度优先遍历解法

        :type root: TreeNode
        :rtype: bool
        """
        return self.helper(root.left,root.right)


    def helper(self,p,q):
        if not p and not q:
            return True
        if p and q:
            if p.val == q.val:
                l = self.helper(p.left,q.right)
                r = self.helper(p.right,q.left)
                return l and r
        return False





if __name__ == '__main__':
    print(123)