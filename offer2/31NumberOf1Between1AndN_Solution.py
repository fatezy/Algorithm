# 从1 到 n 中1出现的次数

class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        res = ''
        for i in range(n+1):
            res += str(i)

        return res.count('1')