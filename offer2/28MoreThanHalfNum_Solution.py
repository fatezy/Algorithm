# 题目描述
# 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
# 例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组
# 中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。

class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        if not numbers:
            return 0
        num_map = {}

        for i in range(len(numbers)):
            if not num_map.__contains__(numbers[i]):
                num_map[numbers[i]] = 1
            else:
                num_map[numbers[i]] += 1

        length = len(numbers)/2
        for i in num_map.keys():
            if num_map[i] > length:
                return i

        return 0




if __name__ == '__main__':
    print(Solution().MoreThanHalfNum_Solution([1,2,3,2,4,2,5,2,3]))
