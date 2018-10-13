# 题目描述
# 用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。


class Solution:
    def __init__(self):
        self.stackA = []   # push
        self.stackB = []   # pop


    def push(self, node):
        self.stackA.append(node)

    def pop(self):
        if  self.stackB:
            return self.stackB.pop()
        else:
            while self.stackA:
                self.stackB.append(self.stackA.pop())
            return self.stackB.pop()


