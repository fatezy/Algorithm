# 题目描述
# 求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）

class Solution:
    def Sum_Solution(self, n):
        """
        利用短路求解问题
        :param n:
        :return:
        """
        return sum(range(1,n+1))

    def Sum_Solution2(self, n):
        res = n
        return n and n + self.Sum_Solution(n-1)


if __name__ == '__main__':
    print(1 and 2)