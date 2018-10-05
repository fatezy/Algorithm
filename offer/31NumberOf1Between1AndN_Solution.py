# 求出1到n区间内1出现的次数


class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        str_n = ''
        for i in range(n+1):
            str_n += str(i)

        return str_n.count('1')


if __name__ == '__main__':
    Solution().NumberOf1Between1AndN_Solution(1)



