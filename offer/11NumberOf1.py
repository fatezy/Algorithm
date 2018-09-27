# 题目描述
# 输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。

class Solution:
    def NumberOf1(self, n): # error
        count = 0

        while  n:
            if n & 1:
                count += 1
            n = n >> 1
        return count

    def NumberOf12(self,n): # error
        count = 0
        flag = 1
        flagN = 0

        while flag:

            if flag & n:
                count += 1
            flag = flag << 1

            flagN +=1
            if flagN > 100:
                break
        return count


    def NumberOf3(self, n):
        # write code here
        count = 0
        if n < 0:
            n = n & 0xffffffff   # python无限精度，需加以处理
        while n:
            count += 1
            n = (n - 1) & n
        return count






if __name__ == '__main__':
    print(Solution().NumberOf12(9))



