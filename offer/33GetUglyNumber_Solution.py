# 把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，
# 因为它包含质因子7。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。

# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):  # 此方法超时
        i = 0
        num = 1
        while i<index:
            if self.uglyNumber(num):
                i += 1
            num +=1
        return num-1


    def uglyNumber(self,number):
        while True:
            if number == 1:
                return True
            if number%2!=0 and number %3 != 0 and number%5 !=0:
                return False
            if number%2 == 0:
                number = number/2
            if number%3 == 0:
                number = number/3
            if number%5 == 0:
                number = number/5



    def GetUglyNumber_Solution2(self,index):
        """
        设置三个值分别记录乘2，3，5大于当前值的数
        :param index:
        :return:
        """
        if not index:
            return 0

        uglys = [1]
        i,p2,p3,p5 = 0,0,0,0

        while i < index:
            next_ugly = min(uglys[p2]*2,uglys[p3]*3,uglys[p5]*5)
            uglys.append(next_ugly)
            i+=1
            while uglys[p2]*2<=next_ugly:
                p2+=1
            while uglys[p3]*3<=next_ugly:
                p3+=1
            while uglys[p5]*5<=next_ugly:
                p5+=1

        return uglys[index-1]






if __name__ == '__main__':
    print(Solution().GetUglyNumber_Solution2(1))
