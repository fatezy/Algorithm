# 二叉搜索树中的两个节点被错误地交换。
#
# 请在不改变其结构的情况下，恢复这棵树。
#
# 示例 1:
#
# 输入: [1,3,null,null,2]
#
#    1
#   /
#  3
#   \
#    2
#
# 输出: [3,1,null,null,2]
#
#    3
#   /
#  1
#   \
#    2
# 示例 2:
#
# 输入: [3,1,4,null,null,2]
#
#   3
#  / \
# 1   4
#    /
#   2
#
# 输出: [2,1,4,null,null,3]
#
#   2
#  / \
# 1   4
#    /
#   3

from offer.tree_helper import *
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        allnode = []
        self.findAllNode(root,allnode)
        error1 = allnode[0]
        for i in range(len(allnode)-1):
            if allnode[i].val > allnode[i+1].val:
                error1 = allnode[i]
                break
        error2 = allnode[len(allnode)-1]
        for i in range(len(allnode)-1,0,-1):
            if allnode[i].val<allnode[i-1].val:
                error2 = allnode[i]
                break

        error1.val,error2.val =error2.val,error1.val


    def findAllNode(self,root,res):
        """
        找错误点
        :param root:
        :param res:
        :return:
        """
        if not root:
            return
        self.findAllNode(root.left,res)
        res.append(root)
        self.findAllNode(root.right,res)

if __name__ == '__main__':
    tree = biTree([1,3,'#','#',2])
    root = tree.creat()
    Solution().recoverTree(root)