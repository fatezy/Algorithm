class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def insert(root,val):
    if not root:
        root = TreeNode(val)
    else:
        if val < root.val:
            root.left = insert(root.left,val)
        elif val > root.val:
            root.right = insert(root.right,val)
    return root



def query(root,val):
    if not root:
        return False
    if root:
        if root.val == val:
            return True
        elif root.val < val:
            return query(root.right,val)
        elif root.val > val:
            return query(root.left,val)


def midOrder(root,res):
    if not root:
        return
    midOrder(root.left,res)
    res.append(root.val)
    midOrder(root.right,res)


if __name__ == '__main__':
    root = TreeNode(3)
    root = insert(root,2)
    root = insert(root,4)
    root = insert(root,1)
    res = []
    midOrder(root,res)
    print(res)
