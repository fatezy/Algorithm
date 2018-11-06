# 题目描述
# 输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。

import sys
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        if not array:
            return []
        small,big =0,len(array)-1

        sum_list = []
        res = []
        while small < big:
            if array[small]+array[big] == tsum:
                sum_list.append([array[small],array[big]])
                small += 1
            if array[small]+array[big] < tsum:
                small += 1
            if array[small]+array[big] > tsum:
                big -= 1

            min_val = sys.maxsize
        for i,temp in enumerate(sum_list):
            if temp[0]*temp[1] < min_val:
                min_val = temp[0]*temp[1]
                res = sum_list[i]

        return res


# if __name__ == '__main__':
