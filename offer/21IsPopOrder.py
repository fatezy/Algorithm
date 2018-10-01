# 是不是栈的弹出顺序

# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        stack = []
        if not pushV:
            return

        i,j = 0,0

        while i<=len(pushV) and j<len(pushV):
            if not stack:
                if i == len(pushV):
                    break
                stack.append(pushV[i])
                i = i+1

            if stack[-1] != popV[j]:
                if i == len(pushV):
                    break
                stack.append(pushV[i])
                i += 1
            else:
                stack.pop()
                j+=1






        if not stack:
            return True
        else:
            return False


if __name__ == '__main__':
    Solution().IsPopOrder([1,2,3,4,5],[4,3,5,1,2])



