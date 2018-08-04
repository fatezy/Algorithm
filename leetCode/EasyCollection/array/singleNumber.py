from functools import reduce


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(lambda i, j: int(i) ^ int(j), nums)      # 异或运算符


if __name__ == '__main__':
    print(Solution().singleNumber([2, 2, 1]))