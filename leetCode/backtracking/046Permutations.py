# Given a collection of distinct integers, return all possible permutations.
#
# Example:
#
# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]

class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.helper(res,[],nums,0)
        return res


    def helper(self,res,temp_list,nums,start):

        if len(temp_list) == len(nums):
            res.append(temp_list[:])
            return
        for i in range(len(nums)):
            # 没有考虑nums中存在重复值
            if nums[i] not in temp_list:
                temp_list.append(nums[i])
                self.helper(res,temp_list,nums,i+1)
                temp_list.pop()

if __name__ == '__main__':
    print(Solution().permute([1, 2, 3]))