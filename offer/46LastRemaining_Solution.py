# 题目:0,1,....,n-1这n个数字排成一个圆圈，从数字0开始每次从这个圆圈中
# 删除第m个数字。求出这个圆圈中剩余的数字

class Solution:
    def LastRemaining_Solution(self, n, m):
        """
        此方法超时
        :param n:
        :param m:
        :return:
        """
        if not n or not m:
            return -1
        nums = list(range(n))
        temp = (m-1)%n
        i = n-1
        while i:
            i-=1
            nums[temp] = -1
            j,k = 0,0
            while j<m:
                if nums[(temp+k)%n] != -1:
                    # nums[(temp + k) % n] = -1
                    j+=1
                k +=1
            temp = (temp + k - 1) % n

        for i in range(n):
            if nums[i] != -1:
                return nums[i]

    def LastRemaining_Solution2(self, n, m):
        if n < 1:
            return -1

        con = list(range(n))

        final = -1
        start = 0
        while con:
            k = (start + m - 1) % n
            final = con.pop(k)
            n -= 1
            start = k

        return final


if __name__ == '__main__':
    test = range(5)
    print(type(test))




