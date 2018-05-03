# Given a sorted array, remove the duplicates in place such that
# each element appear only once and return the new length.
#
# Do not allocate extra space for another array, you must do this in place with constant memory.
#
# For example,
# Given input array nums = [1,1,2],
#
# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
# It doesn't matter what you leave beyond the new length.

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        temp = 0
        for index,item in enumerate(nums):
            if nums[temp] != nums[index]:
                temp = temp+1
                nums[temp] = nums[index]
        return temp+1

    def removeDuplicates2(self, A):
        if not A:
            return 0

        newTail = 0

        for i in range(1, len(A)):
            if A[i] != A[newTail]:
                newTail += 1
                A[newTail] = A[i]

        return newTail + 1

if __name__ == '__main__':
    A = Solution()
    print(A.removeDuplicates([1,1,3]))



