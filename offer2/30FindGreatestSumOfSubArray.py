# 连续子数组最大和

class Solution:
    def FindGreatestSumOfSubArray(self, array):
        if not array:
            return None
        if len(array) <2:
            return sum(array)

        res = [array[0] for i in array]
        # 找出所有位置上对应的最大和
        for i in range(len(array)):
            if i==0 or res[i-1]<=0:  # 如果是第一个或前面的小于0
                res[i] = array[i]

            if i !=0 and res[i-1] >0: # 如果不是第一个且前面大于0
                res[i] = res[i-1] +array[i]

        return max(res)

    def FindGreatestSumOfSubArray2(self,array):
        if  array is None:
            return None

        if len(array)<2:
            return sum(array)

        res = []
        for i in range(len(array)):
            res.append(self.heler2(array,i))


    def heler2(self,array,i):
        if i == 0 or self.heler2(array,i-1) <=0:
            return array[i]

        if i != 0 and self.heler2(array,i-1)>0:
            return array[i]+self.heler2(array,i-1)




