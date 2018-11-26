# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
#
# 示例：
#
# 给定一个链表: 1->2->3->4->5, 和 n = 2.
#
# 当删除了倒数第二个节点后，链表变为 1->2->3->5.
# 说明：
#
# 给定的 n 保证是有效的。

from offer.list_helper import *
class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        pre,curr = ListNode(-1),head
        pre.next = head
        res = pre
        while n:
            n = n-1
            curr = curr.next

        while curr:
            curr = curr.next
            pre = pre.next
        pre.next = pre.next.next


        return res.next



if __name__ == '__main__':
    a = LinkList([1])
    print(Solution().removeNthFromEnd(a.get_head(), 1))
