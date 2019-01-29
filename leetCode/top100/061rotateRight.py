# 给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。
#
# 示例 1:
#
# 输入: 1->2->3->4->5->NULL, k = 2
# 输出: 4->5->1->2->3->NULL
# 解释:
# 向右旋转 1 步: 5->1->2->3->4->NULL
# 向右旋转 2 步: 4->5->1->2->3->NULL
# 示例 2:
#
# 输入: 0->1->2->NULL, k = 4
# 输出: 2->0->1->NULL
# 解释:
# 向右旋转 1 步: 2->0->1->NULL
# 向右旋转 2 步: 1->2->0->NULL
# 向右旋转 3 步: 0->1->2->NULL
# 向右旋转 4 步: 2->0->1->NULL
from offer.list_helper import *

class Solution(object):
    def rotateRight(self, head, k):
        """ 懒得改了，通过了，但是代码很丑
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None

        newHead = ListNode(-1)
        temp = head
        len_of_list = 0
        end = ListNode(-1)
        while temp:
            if not temp.next: # 记录下end
                end = temp
            temp = temp.next
            len_of_list += 1 # 记录下链表长度

        if len_of_list == 1 or k==0:
            return head
        temp = head

        k = k%len_of_list
        if k!=0:
            k = len_of_list - k
        for i in range(k):
            temp = temp.next
        newHead = temp
        end.next = head

        temp = newHead
        for i in range(len_of_list-1):
            temp = temp.next
        temp.next = None

        return newHead

if __name__ == '__main__':
    a = LinkList([1,2])
    Solution().rotateRight(a.head, 2)







