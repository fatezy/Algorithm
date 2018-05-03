# Given an array of integers, find if the array contains any duplicates.
# Your function should return true if any value appears at least twice in the array,
#  and it should return false if every element is distinct.
#判断是否有相同的项
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        map = {}
        for i in range(len(nums)):
            if nums[i] in map:
                return True
            else:
                map[nums[i]] = 1

        return False


    def  containsDuplicate2(self, A):
         map = {}
         for i,val in enumerate(A):
             if A[i] in map:
                 return True
             else:
                 map[A[i]] = 1

         return False