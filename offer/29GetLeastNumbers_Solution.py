# 题目描述
# 输入n个整数，找出其中最小的K个数。例如输入
# 4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。


class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if not tinput:
            return []
        tinput.sort()
        if k <= len(tinput):
            return tinput[0:k]
        else:
            return []