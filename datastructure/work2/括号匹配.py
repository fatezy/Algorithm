
class Solution:
    def check(self,brackets):
        if not brackets:
            return False

        brackets_map = {'[':']','(':')'}
        brackets = list(brackets)
        brackets_stack =[]

        while brackets:
            curr = brackets.pop(0)   # 弹出当前队列的第一个括号
            if brackets_stack and brackets_map.get(brackets_stack[-1]) == curr:  # 获取当前括号是否与栈顶括号匹配
                brackets_stack.pop()
            else:
                brackets_stack.append(curr)

        return True if not brackets_stack else False


if __name__ == '__main__':
    print(Solution().check('([]())'))

    print(Solution().check('((('))