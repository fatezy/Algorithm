from leetCode.easyCollection.linkLists.linklist_helper import ListNode
from leetCode.easyCollection.linkLists.linklist_helper import LinkList

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


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        h1 = head
        flag = 0
        for i in range(n+1):
            if h1 is None:
                flag = 1
                break
            h1 = h1.next

        h2 = head

        while h1 is not None:
            h1 = h1.next
            h2 = h2.next

        if flag == 1:
            head = head.next
        else:
            h2.next = h2.next.next
        return head

if __name__ == '__main__':
    a = LinkList([1,2,3,4,5])
    Solution().removeNthFromEnd(a.get_head(),2)
    a.print_list()

