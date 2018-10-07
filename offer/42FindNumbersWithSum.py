# 输入一个递增排序的数组和一个数字S，在数组中查找两个数，
# 使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
import sys
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        if not array or not tsum:
            return []
        small,big = 0,len(array)-1
        sum_ok = []
        while small < big:
            if array[small] + array[big] == tsum:
                sum_ok.append([array[small],array[big]])
                small+=1
                big-=1
            elif array[small] + array[big] < tsum:
                small +=1
            else:
                big -=1

        min_v = sys.maxsize
        res = -1
        for ind,l in enumerate(sum_ok):
            if l[0] * l[1] < min_v:
                min_v = l[0] * l[1]
                res = ind

        return sum_ok[res] if res != -1 else []

if __name__ == '__main__':
    Solution().FindNumbersWithSum([],0)




