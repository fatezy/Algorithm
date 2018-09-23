# -*- coding:utf-8 -*-
import numpy as np
class Solution:
    # array 二维列表
    def Find(self, array, target):
        l1 = len(array)
        l2 = len(array[0])
        i = 0
        j = l2 - 1
        while i < l1 and j >= 0:
            if target == array[i][j]: return True
            if target > array[i][j]:
                i = i + 1
            else:
                j = j - 1
        return False

#  x**2的复杂度
    def Find2(self, target, array):
        for i, nums in enumerate(array):
            for j, num in enumerate(nums):
                if target == num:
                    return True
        return False

    def Find3(self,target,array):
        if not array:
            return 0

        i = 0
        j = len(array[0])-1
        while i<len(array) and j>=0:
            if target == array[i][j]:
                return True
            if target > array[i][j]:
                i = i+1
            else:
                j = j-1

        return False



if __name__ == '__main__':
    array = np.arange(0,16).reshape(4,4)
    print(Solution().Find2(34,list(array)))
    print(list(range(10)))


