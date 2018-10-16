# 题目描述
# 输入两个单调递增的链表，输出两个链表合成后的链表，
# 当然我们需要合成后的链表满足单调不减规则。
from offer.list_helper import ListNode
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):

        # 各种为None的情况
        if not pHead1 and not pHead2:
            return None
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1

        p1, p2 = pHead1, pHead2
        newHead = ListNode(-1)
        curr = newHead
        while p1 and p2:
            if p1.val < p2.val:
                curr.next = p1
                p1 = p1.next
            else:
                curr.next = p2
                p2 = p2.next
            curr = curr.next

        curr.next = p2 if not p1 else p1

        return newHead.next






