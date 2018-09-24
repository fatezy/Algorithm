# -*- coding:utf-8 -*-
# 用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
class Solution:
    def __init__(self):
        self.stackA = []
        self.stackB = []

    def push(self, node):
        # write code here
        self.stackA.append(node)

    def pop(self):
        # return xx
        if self.stackB:
            return self.stackB.pop()
        elif not self.stackA:
            return None
        else:
            while self.stackA:
                self.stackB.append(self.stackA.pop())
            return self.stackB.pop()

    def push2(self, node):
        self.stackA.append(node)

    def pop2(self):
        if self.stackB:
            return self.stackB.pop()

        elif not self.stackA:
            return None
        else:
            while self.stackA:
                self.stackB.append(self.stackA.pop())

        return self.stackB.pop()


if __name__ == '__main__':
    test = Solution()

    test.push2(1)
    test.push2(2)
    test.push2(3)

    print(test.pop2())
    print(test.pop2())

    test.push2(4)

    print(test.pop2())

    test.push2(5)

    print(test.pop2())
    print(test.pop2())

