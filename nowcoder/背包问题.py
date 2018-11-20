# 有n个重量与价值分别为wi,vi的物品，从这些物品中挑选总重量不超过w的物品，求所有挑选方案中价值总和最大值

class Solution:


    def rec(self,w,v,j):
        """

        :param w:  list 物品重量
        :param v: list 物品价值
        :param j: int 代表背包剩余容量
        :return: int 背包能背的最大价值
        """
        return self.recHelper(w,v,0,j)


    def recHelper(self,w,v,i,j):
        """
        从第i个物品挑选总重小于j的部分
        :param w:
        :param v:
        :param i:
        :param j:
        :return:
        """
        res = 0
        if i == len(w):
            # 代表已经没有物品了
            res = 0
        elif j<w[i]:
            # 太重加不进背包
            res = self.recHelper(w,v,i+1,j)
        else:
            # 判断不加和加了哪种比较合适
            res = max(self.recHelper(w,v,i+1,j),self.recHelper(w,v,i+1,j-w[i])+v[i])

        return res

    def rec2(self,w,v,j):
        # 初始化一个二维数组，记录背包当前位置的最大价值，用于剪枝
        dp = [[-1 for k in range(j + 1)] for i in range(len(w)+ 1)]

        res =  self.recHelper2(w,v,0,j,dp)
        return res


    def recHelper2(self,w,v,i,j,dp):
        """
        从第i个物品挑选总重小于j的部分
        :param w:
        :param v:
        :param i:
        :param j:
        :return:
        """
        # 等于0 代表i已经走到了头即没有物品了，从此位置只能为0
        if dp[i][j] >= 0:
            return dp[i][j]

        res = 0
        if i == len(w):
            # 代表已经没有物品了
            res = 0
        elif j<w[i]:
            # 太重加不进背包
            res = self.recHelper2(w,v,i+1,j,dp)
        else:
            # 判断不加和加了哪种比较合适
            res = max(self.recHelper2(w,v,i+1,j,dp),self.recHelper2(w,v,i+1,j-w[i],dp)+v[i])

        dp[i][j] = res
        return res


    # 动态规划

    def rec3(self,w,v,j):
        """
        此种顺序求出问题的解的方式，称之为动态规划
        :param w:
        :param v:
        :param j:
        :return:
        """
        # 初始化一个二维数组，记录背包当前位置的最大价值，用于剪枝
        dp = [[-1 for k in range(j + 1)] for i in range(len(w)+ 1)]
        dp[len(w)][:] = [0 for i in range(j+1)]

        for i in range(len(w)-1,-1,-1):
            for k in range(j+1):
                if k < w[i]:
                    dp[i][k] = dp[i+1][k]
                else:
                    dp[i][k] = max(dp[i+1][k],dp[i+1][k-w[i]]+v[i])

        return dp[0][j]







if __name__ == '__main__':
    w = [2,1,3,2]
    v = [3,2,4,2]
    j = 5
    print(Solution().rec3(w, v, j))
