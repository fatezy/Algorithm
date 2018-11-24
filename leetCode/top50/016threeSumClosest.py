# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
#
# 例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
#
# 与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
class Solution(object):
    def threeSumClosest(self, nums, target): # 同样的复杂度，超时
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        N,res = len(nums),2<<32
        dis = 2<<32
        for i in range(N):
            t = target - nums[i] #两数之和目标值
            s,e = i+1,N-1
            while s<e:
                if nums[s]+nums[e] == t:
                    return target
                elif nums[s]+nums[e] < t:
                    val = nums[s] +nums[e]+nums[i]
                    if abs(target-val) < dis:
                        dis,res = abs(target-val),val
                        s = s + 1

                else:
                    val = nums[s] + nums[e] + nums[i]
                    if abs(target - val) < dis:
                        dis, res = abs(target - val), val
                    e = e - 1

        return res

    def threeSumClosest2(self, num, target):
        num.sort()
        result = num[0] + num[1] + num[2]
        for i in range(len(num) - 2):
            j, k = i + 1, len(num) - 1
            while j < k:
                sum = num[i] + num[j] + num[k]
                if sum == target:
                    return sum

                if abs(sum - target) < abs(result - target):
                    result = sum

                if sum < target:
                    j += 1
                elif sum > target:
                    k -= 1

        return result
if __name__ == '__main__':
    print(Solution().threeSumClosest([-1, 2, 1, -4], 1))




