# 连续子数组最大和


class Solution:
    def FindGreatestSumOfSubArray(self, array):
        if  array is None:
            return None
        if len(array)<2:
            return sum(array)
        res = [array[0] for i in array] # 用以记录第i个数为结尾，最大的值

        for i in range(len(array)):
            if i ==0 or res[i-1]<=0:
                res[i] = array[i]

            if i !=0 and res[i-1]>0:
                res[i] = res[i-1]+array[i]

        return max(res)


    def FindGreatestSumOfSubArray2(self, array):
        """
        思路同上，递归写法，没有超时
        :param array:
        :return:
        """
        if array is None:
            return None
        if len(array) < 2:
            return sum(array)
        res = []
        for i in range(len(array)):
            res.append(self.heler2(array,i))

        return max(res)

    def heler2(self,array,i):
        if i == 0 or self.heler2(array,i-1) <=0:
            return array[i]

        if i != 0 and self.heler2(array,i-1)>0:
            return array[i]+self.heler2(array,i-1)





if __name__ == '__main__':
    Solution().FindGreatestSumOfSubArray2([-2,-8,-1,-5,-9])