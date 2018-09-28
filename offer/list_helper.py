class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkList:
    def __init__(self,nums):
        self.head = None
        self.last = None
        for x , y in enumerate(nums):
            if x == 0:
                self.head = ListNode(y)
                self.last = self.head
            else:
                self.last.next = ListNode(y)
                self.last = self.last.next

    def get_head(self):
        return self.head

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.val,end=",")
            temp = temp.next


if __name__ == '__main__':
    a = LinkList([1,2,3])
    a.head = a.head.next
    a.print_list()


