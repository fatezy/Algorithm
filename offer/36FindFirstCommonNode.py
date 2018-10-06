# 输入两个链表，找出它们的第一个公共结点。
from offer.list_helper import *
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        """
        两个链表呈Y型，从第一个相同的节点之后所有节点全部相同，故可用栈找出最后一个相同的节点
        :param pHead1:
        :param pHead2:
        :return:
        """
        if not pHead1 or not pHead2:
            return None

        stack1 = []
        stack2 = []

        while pHead1:
            stack1.append(pHead1)
            pHead1 = pHead1.next

        while pHead2:
            stack2.append(pHead2)
            pHead2 = pHead2.next

        first = None
        while stack1 and stack2:
            top1 = stack1.pop()
            top2 = stack2.pop()
            if top1 is top2:
                first = top1
            else:
                break
        return first

    def FindFirstCommonNode2(self, pHead1, pHead2):

        len1,len2,p1,p2 = 0,0,pHead1,pHead2
        while p1:
            p1 = p1.next
            len1+=1

        while p2:
            p2 =p2.next
            len2+=1








