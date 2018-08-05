# 给定一个非负整数组成的非空数组，在该数的基础上加一，返回一个新的数组。
#
# 最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。
#
# 你可以假设除了整数 0 之外，这个整数不会以零开头。
#
# 示例 1:
#
# 输入: [1,2,3]
# 输出: [1,2,4]
# 解释: 输入数组表示数字 123
from functools import reduce

class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = reduce(lambda i, j: i*10+j, digits)+1
        # return [int(i) for i in str(num)]
        return list(map(int, str(num)))


if __name__ == '__main__':
    val = Solution().plusOne([1,2,3])
    print(1)