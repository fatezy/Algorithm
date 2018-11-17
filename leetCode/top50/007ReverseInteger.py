# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
#
# Input: 123
# Output: 321


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if not x:
            return 0
        flag = False
        if x<0:
            x = -x
            flag = True

        x_arr = list(str(x))
        x_arr = x_arr[::-1]
        while x_arr[0] == 0:
            x_arr.pop(x_arr[0])

        if ''.join(x_arr)>2**31:
            return 0


        return int(''.join(x_arr)) if not flag else -1*int(''.join(x_arr))




if __name__ == '__main__':
    print(Solution().reverse(-123))


