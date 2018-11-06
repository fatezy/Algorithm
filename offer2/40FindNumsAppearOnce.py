# 题目描述
# 一个整型数组里除了两个数字之外，其他的数字都出现了偶数次。请写程序找出这两个只出现一次的数字。

class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
            if not array:
                return []

            arr_map = {}

            for i in range(len(array)):
                if arr_map.__contains__(array[i]):
                    arr_map[array[i]] = 2
                else:
                    arr_map[array[i]] = 1

            res = []
            for i in arr_map.keys():
                if arr_map[i] == 1:
                    res.append(i)

            return res


