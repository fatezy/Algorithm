# 题目描述
# 统计一个数字在排序数组中出现的次数。
from collections import Counter
class Solution:
    def GetNumberOfK(self, data, k):
        return data.count(k)

    def GetNumberOfK2(self,data,k):
        left,right =

if __name__ == '__main__':
    print(Solution().GetNumberOfK([1, 2, 1, 2, 3], 2))