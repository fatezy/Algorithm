# 罗马数字包含以下七种字符： I， V， X， L，C，D 和 M。
#
# 字符          数值
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# 例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        num_map = {'M':1000,'CM':900,'D':500,'CD':400,'C':100,'XC':90,'L':50,'XL':40,'X':10,'IX':9,'V':5,'IV':4,'I':1}
        # 上面key,val写反了，调换一下位置
        num_map = {value:key for key,value in num_map.items()}
        arr = [1000,900,500,400,100,90,50,40,10,9,5,4,1]

        res = ''
        while num>0:
            for val in arr:
                if num >= val:
                    num -= val
                    res += num_map.get(val)
                    break
        return res


if __name__ == '__main__':
    print(Solution().intToRoman(4))



