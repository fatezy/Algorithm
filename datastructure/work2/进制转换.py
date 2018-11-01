# 十进制转换为八进制

class Solution:

    def ten_to_eight(self,num):
        if not num:
            return 0

        res = []
        while num:
            num,remainder = num // 8,  num % 8
            res.append(remainder)

        return ''.join(str(x) for x in res[::-1])

    def ten_to_eight2(self,num):
        res = ''
        # if not num:
        #     return res

        if num // 8 == 0:
            res += str(num)
            return res

        res +=  self.ten_to_eight2(num//8)
        res += str(num % 8)
        return res


if __name__ == '__main__':

    while True:
        val = input('请输入需要转换的十进制数,输入#键结束')
        if val == '#':
            break
        print(Solution().ten_to_eight(int(val)))
        print(Solution().ten_to_eight2(int(val)))



