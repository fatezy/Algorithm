# 输入一个链表，输出该链表中倒数第k个结点。

from offer.list_helper import ListNode

class Solution:
    def FindKthToTail(self, head, k):
        # write code here

        front,late = head,head
        if not head:
            return

        for i in range(k):
            if front:
                front = front.next
            else:
                return

        while front:
            front = front.next
            late = late.next
        return late

# if __name__ == '__main__':
