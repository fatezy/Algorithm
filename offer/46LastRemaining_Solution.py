# 题目:0,1,....,n-1这n个数字排成一个圆圈，从数字0开始每次从这个圆圈中
# 删除第m个数字。求出这个圆圈中剩余的数字

class Solution:
    # def LastRemaining_Solution(self, n, m):
    #     nums = list(range(n))
    #     temp = m-1
    #     i = n-1
    #     while i:
    #         i-=1
    #         nums[temp] = -1
    #         # temp = (temp+m)%n
    #         j,k = 0,0
    #         while j<m:
    #             if nums[(temp+k)%n] != -1:
    #                 nums[(temp + k) % n] = -1
    #                 j+=1
    #             k +=1
    #
    #     for i in range(n):
    #         if nums[i] != -1:
    #             return nums[i]


# if __name__ == '__main__':
#     Solution().LastRemaining_Solution(5,3)




