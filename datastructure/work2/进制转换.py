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

if __name__ == '__main__':
    print(Solution().ten_to_eight(1348))
    print(Solution().ten_to_eight(234))