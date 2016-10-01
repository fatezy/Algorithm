# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 输入一个链表，从尾到头打印链表每个节点的值。
# 输入描述:
# 输入为链表的表头
#
#
# 输出描述:
# 输出为需要打印的“新链表”的表头

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        result = []
        if listNode is None:
            return result
        while  listNode.next is not None:
            result.extend([listNode.val])
            listNode = listNode.next
        result.extend([listNode.val])
        return result[::-1]

if __name__ == '__main__':
    node = ListNode(1)
    node.next = ListNode(2)
    node.next.next = ListNode(3)
    print(Solution().printListFromTailToHead(node))




