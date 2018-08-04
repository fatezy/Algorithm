class Solution:
      def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        map = {}
        for i in range(len(nums)):
            if map.__contains__(nums[i]):
                return True
            else:
                map[nums[i]] = 1
        return False

      def containsDuplicate2(self, nums):
          if len(set(nums)) == len(nums):
              return False
          else:
              return True