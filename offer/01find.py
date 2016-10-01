# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, array, target):
        l1 = len(array)
        l2 = len(array[0])
        i =0
        j = l2 -1
        while i <l1 and j >=0:
            if(target == array[i][j]): return True
            if(target > array[i][j]): i=i+1
            else: j=j-1
        return False
