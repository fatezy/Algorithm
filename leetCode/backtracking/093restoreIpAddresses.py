# 给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
#
# 示例:
#
# 输入: "25525511135"
# 输出: ["255.255.11.135", "255.255.111.35"]


class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) > 12:
            return []
        res = []
        self.helper(s,res,'',0)
        if  res:
            res = [i[1:] for i in res]
        return res


    def helper(self,s,res,temp_s,start):
        if len(s)+4 == len(temp_s):
            if temp_s.count('.') == 4:
                res.append(temp_s)
            return
        if temp_s.count('.') > 4:   # 优化了一下
            return

        for i in range(start,len(s)):

            if i<len(s) or (i<len(s) and s[i] == '0'):                 # 最初的时候，这里写的是1+1<s，会导致0000用例通不过
                temp_s +=('.'+s[i])
                self.helper(s,res,temp_s,i+1)
                temp_s = temp_s[:-2]

            if i + 1 < len(s) and s[i] != '0':
                temp_s += ('.'+s[i:i+2])
                self.helper(s, res, temp_s,i + 2)
                temp_s = temp_s[:-3]

            if i + 2 < len(s) and int(s[i:i+3])<=255 and  s[i] != '0':
                temp_s += ('.'+s[i:i+3])
                self.helper(s, res, temp_s , i+3)
                temp_s = temp_s[:-4]


if __name__ == '__main__':
    print(Solution().restoreIpAddresses('010010'))



