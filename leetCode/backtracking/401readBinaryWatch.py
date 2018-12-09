# 二进制手表顶部有 4 个 LED 代表小时（0-11），底部的 6 个 LED 代表分钟（0-59）。
#
# 每个 LED 代表一个 0 或 1，最低位在右侧。
#
# 例如，上面的二进制手表读取 “3:25”。
#
# 给定一个非负整数 n 代表当前 LED 亮着的数量，返回所有可能的时间。
#
# 案例:
#
# 输入: n = 1
# 返回: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]

class Solution:
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        hour_list = [1,2,4,8]
        minute_list = [1,2,4,8,16,32]
        res = []
        self.helper(num,res,hour_list,minute_list,num,[],[],0,0)
        return res

        # todo 执行不过
    def helper(self,num,res,hour_list,minute_list,remain,temp_h,temp_m,start_h,start_m):
        if len(temp_h)+len(temp_m) == num:
            h = sum(temp_h)
            m = sum(temp_m)
            res.append(str(h)+':'+str(m))
            return

        for i in range(start_h,len(hour_list)):
            if remain > 0 and sum(temp_h)+hour_list[i] <= 11:
                remain -= 1
                temp_h.append(hour_list[i])
                self.helper(num,res,hour_list,minute_list,remain-1,temp_h,temp_m,start_h+1,start_m)

                for j in range(start_m, len(minute_list)):
                    if remain > 0 and sum(temp_m) + minute_list[j] <= 59:
                        remain -= 1
                        temp_m.append(minute_list[j])
                        self.helper(num, res, hour_list, minute_list, remain - 1, temp_h, temp_m, start_h, start_m + 1)
                        remain -= 1
                        temp_m.pop()

                temp_h.pop()
                remain += 1

    def readBinaryWatch2(self, num):  # 暴力解法
        return ['%d:%02d' % (h, m)
                for h in range(12) for m in range(60)
                if (bin(h) + bin(m)).count('1') == num]

    def readBinaryWatch3(self, n): # 回溯解法

        def dfs(n, hours, mins, idx):
            if hours >= 12 or mins > 59: return
            if not n:
                res.append(str(hours) + ":" + "0" * (mins < 10) + str(mins))
                return
            for i in range(idx, 10):
                if i < 4:
                    dfs(n - 1, hours | (1 << i), mins, i + 1)
                else:
                    k = i - 4
                    dfs(n - 1, hours, mins | (1 << k), i + 1)

        res = []
        dfs(n, 0, 0, 0)
        return res

if __name__ == '__main__':
    print(Solution().readBinaryWatch3(4))



