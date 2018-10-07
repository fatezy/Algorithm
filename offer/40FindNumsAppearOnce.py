# 一个整型数组里除了两个数字之外，其他的数字都出现了偶数次。
# 请写程序找出这两个只出现一次的数字。

from collections import Counter

class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        if not array:
            return None
        res = []
        nummap ={}
        for i,val in enumerate(array):
            if nummap.__contains__(val):
                nummap.pop(val)
            else:
                nummap[val] = 1
        for i in nummap.keys():
            res.append(i)
        return res





    def FindNumsAppearOnce2(self, array):
        return list(map(lambda c: c[0], Counter(array).most_common()[-2:]))