# 一副扑克牌，大小王是癞子，用0表示，判断能否组成癞子
class Solution:
    def IsContinuous(self, numbers):
        """
        失误 代码写的有点丑
        :param numbers:
        :return:
        """
        if not numbers:
            return []
        numbers.sort()
        zero_num = 0
        for i, val in enumerate(numbers):
            if i == 4:
                continue
            if val == 0:
                zero_num += 1
                continue
            if val == numbers[i+1]:
                return False
            if val+1 == numbers[i+1]:
                continue
            if val+1 != numbers[i+1] and numbers[i+1] - val > zero_num+1:
                return False
            if val+1 != numbers[i+1] and numbers[i+1] - val <= zero_num+1:
                zero_num = zero_num - (numbers[i+1] - val-1)


        return True


if __name__ == '__main__':
    print(Solution().IsContinuous([0,3,2,6,4]))


