# 定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数
# （时间复杂度应为O（1））。
import sys

class Solution:
    def __init__(self):
        self.arr = []
        self.min_stack = []
        self.min_stack.append(sys.maxsize)

    def push(self, node):
        if node <= self.min_stack[-1]:
            self.min_stack.append(node)

        self.arr.append(node)


    def pop(self):
        if self.arr[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        return self.arr.pop()

    def top(self):
        return self.arr[-1]
    def min(self):            # 用栈来存储最小值的过程
        return self.min_stack[-1]


if __name__ == '__main__':
    stack = Solution()
    stack.push(3)
    stack.min()
    stack.push(4)
    stack.min()
    stack.push(2)
    stack.min()