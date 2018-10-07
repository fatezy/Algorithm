# 找出所有和为S的连续正数序列

class Solution:
    def FindContinuousSequence(self, tsum):
        if not tsum:
            return None
        small,big = 1,2
        res = []
        while small < (tsum+1)/2:
            cur_sum = sum(range(small,big+1))
            if cur_sum == tsum:
                res.append(list(range(small,big+1)))

            if cur_sum < tsum:
                big += 1
            else:
                small += 1
        return res