# 判断列表二是不是一的弹出顺序

class Solution:
    def IsPopOrder(self, pushV, popV):
        if not pushV or not popV:
            return False

        stack = []
        while popV or pushV:

            if  pushV:          # 每次进栈一个
                stack.append(pushV.pop(0))

            while stack and popV:  # 尽可能多出栈
                if stack[-1] == popV[0]:
                    popV.pop(0)
                    stack.pop()
                else:
                    break

            if not stack and not popV: # 栈空且popV空，表示已经完成任务
                return True

            if  stack and not pushV:# 栈不空，但是pushV空代表任务失败
                return False


if __name__ == '__main__':
    print(Solution().IsPopOrder([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))




