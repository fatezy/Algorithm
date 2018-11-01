# 把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7
# 。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。

class Solution:
    def GetUglyNumber_Solution(self, index):
        """
        求第index个丑数，设置p2，p3,p5分别代表第i个乘2,3,5大于当前最大丑数的数
        :param index:
        :return:
        """
        if not index:
            return 0
        uglys = [1]
        i,p2,p3,p5 = 0,0,0,0

        while i<index:
            next_ugly = min(uglys[p2]*2,uglys[p3]*3,uglys[p5]*5)
            uglys.append(next_ugly)
            i += 1
            if uglys[p2]*2 <= next_ugly:
                p2 +=1
            if uglys[p3]*3 <= next_ugly:
                p3 +=1
            if uglys[p5]*5 <= next_ugly:
                p5 += 1


        return uglys[index-1]
