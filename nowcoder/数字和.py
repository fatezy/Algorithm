# 统计数字和的问题
class NumCount:
    def num_count(self,num):
        return sum(range(1,num+1))

    def num_count1(self,num):
        if num == 1:
            return num
        else:
            return num + self.num_count(num-1)

    def num_count2(self,num):
        st = []   # 代表栈
        res = num
        st.append(num-1)
        while st:
            val = st.pop()
            res += val
            if val != 1:
                st.append(val-1)
        return res



if __name__ == '__main__':
    print(NumCount().num_count(5))
    print(NumCount().num_count1(5))
    print(NumCount().num_count2(5))


