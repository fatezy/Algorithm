# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
# 如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。

class Solution:
    def VerifySquenceOfBST(self, sequence):
        """
        本题运用递归，列表前半部分小于最后一位，列表的最后一位大于最后一位
        :param sequence:
        :return:
        """
        if not sequence:
            return False

        root  = sequence[-1]

        j = 0
        for i in range(len(sequence)): # 找出第一个大于最后一位的值
            j = i
            if sequence[i] > root:
                break

        for k in range(j,len(sequence)): # 如果从j开始存在大于最后一位值的数返回False
            if sequence[k] < root:
                return False

        left = True
        if j>0:
            left =self.VerifySquenceOfBST(sequence[:j])
        right = True
        if j <len(sequence) -1:
            right = self.VerifySquenceOfBST(sequence[j:-1])
        return left and right


