# 输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，
# 另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。
# （注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）

class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:


    def Clone(self, pHead):
        node_map = {}

        if not pHead:
            return None

        temp = pHead
        newHead = RandomListNode(-1)     # 任意初始化一个节点
        newTemp = newHead
        while temp:
            newTemp.next = RandomListNode(temp.label)
            node_map[temp] = newTemp.next
            temp,newTemp = temp.next,newTemp.next

        temp,newTemp = pHead,newHead.next
        while temp:
            newTemp.random = node_map.get(temp.random)
            temp = temp.next
            newTemp = newTemp.next

        return newHead.next

if __name__ == '__main__':
    head = RandomListNode(1)
    head.next = RandomListNode(2)
    head.next.next = RandomListNode(3)
    head.next.next.next = RandomListNode(4)
    head.next.next.next.next = RandomListNode(5)

    head.random = head.next.next
    head.next.random = head
    head.next.next.random = head.next
    head.next.next.next.random = head
    head.next.next.next.next.random = head


    Solution().Clone(head)




