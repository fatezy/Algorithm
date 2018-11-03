# 题目描述
# 输入两个链表，找出它们的第一个公共结点。
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):

            stack1 = []
            stack2 = []

            if not pHead1 or not pHead2:
                return None

            while pHead1:
                stack1.append(pHead1)
                pHead1 = pHead1.next

            while pHead2:
                stack2.append(pHead2)
                pHead2 = pHead2.next

            commonNode = None
            while stack1 and stack2:
                top1 = stack1.pop()
                top2 = stack2.pop()
                if top1 is top2:
                    commonNode = top1
                else:
                    break

            return commonNode


