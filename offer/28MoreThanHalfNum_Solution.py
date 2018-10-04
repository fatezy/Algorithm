# 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组
# {1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。
# 如果不存在则输出0。

class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        """
        空间换时间
        :param numbers:
        :return:
        """
        if not numbers:
            return 0

        map = {}
        for i in range(len(numbers)):
            if map.__contains__(numbers[i]):
                map[numbers[i]] = map[numbers[i]]+1
            else:
                map[numbers[i]] = 1

            if (map[numbers[i]] > len(numbers) / 2):
                return numbers[i]

        return 0

    def MoreThanHalfNum_Solution2(self,numbers):
        """
        如果一个数的个数超过列表的一半，那么中位数一定是这个数
        :param numbers:
        :return:
        """
        if not numbers:
            return 0
        numbers.sort()
        center = numbers[len(numbers)/2]
        if numbers.count(center) >= len(numbers)/2:
            return center
        else:
            return 0





