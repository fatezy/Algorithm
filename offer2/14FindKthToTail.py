# 题目描述
# 输入一个链表，输出该链表中倒数第k个结点。

class Solution:
    def FindKthToTail(self, head, k):
        front,later = head,head
        for i in range(k):
            if not front:
                return None
            front = front.next

        while front:
            front = front.next
            later  = later.next

        return later