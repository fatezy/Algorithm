# 给出二叉树的根，找出出现次数最多的子树元素和。一个结点的子树元素和定义为以该结点为根的二叉树上所有结点的元素之和（包括结点本身）。然后求出出现次数最多的子树元素和。如果有多个元素出现的次数相同，返回所有出现次数最多的元素（不限顺序）。
#
#
#
# 示例
# 1
# 输入:
#
# 5
# / \
#     2 - 3
# 返回[2, -3, 4]，所有的值均只出现一次，以任意顺序返回所有值。
#
# 示例
# 2
# 输入:
#
# 5
# / \
#     2 - 5
# 返回[2]，只有
# 2
# 出现两次，-5
# 只出现
# 1
# 次。
#
from offer.tree_helper import *
from collections import Counter
class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.preOrder(root,res)
        counts = {}
        for i in range(len(res)):
            val = self.valCount(res[i])
            if counts.__contains__(val):
                counts[val] += 1
            else:
                counts[val] = 1

        res = []
        maxcount = 0
        for key,val in counts.items():
            if val == maxcount:
                res.append(key)

            if val > maxcount:
                res = []
                res.append(key)
                maxcount = val

        return res


    def valCount(self,root):
        if not root:
            return 0
        if root:
            l = self.valCount(root.left)
            r = self.valCount(root.right)
            return l+r+root.val

    def preOrder(self,root,res):
        """
        用于记录下所有的节点
        :param root:
        :param res:
        :return:
        """
        if not root:
            return
        if root:
            res.append(root)
            self.preOrder(root.left,res)
            self.preOrder(root.right,res)


    def findFrequentTreeSum2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        vals = []
        def getSum(root):
            if not root:
                return 0
            s = getSum(root.left) + root.val + getSum(root.right)
            vals.append(s)
            # 别忘了返回s
            return s
        getSum(root)
        count = Counter(vals)
        frequent = max(count.values())
        return [x for x, v in count.items() if v == frequent]

if __name__ == '__main__':
    tree = biTree([5,2,-3])
    root = tree.creat()
    print(Solution().findFrequentTreeSum(root))