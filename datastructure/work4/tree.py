class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class biTree:
    def __init__(self,list):
        self.list = list
        self.res = []

    def creatTree(self,root):
        """
        前序数组,并非完全层序,如果某节点为null，则下一层节点不用输入

        :param root:
        :param i:
        :return:
        """
        if self.list:
            val = self.list.pop(0)
            if val =='#':
                return None
            else:
                root = TreeNode(val)
                root.left = self.creatTree(root.left)
                root.right = self.creatTree(root.right)
                return root
        return root

    def preOrder(self,root):
        res = []
        if  root:
            res.append(root.val)
            res.extend(self.preOrder(root.left))
            res.extend(self.preOrder(root.right))
        return res


    def midOrder(self,root):
        if root:
            self.preOrder(root.left)
            self.res.append(root.val)
            self.preOrder(root.right)
        return self.res

    def postOrder(self,root):
        res = []
        if root:
            res.extend(self.preOrder(root.left))
            res.append(root.val)
            res.extend(self.preOrder(root.right))
        return res


    def creat(self):
        return self.creatTree(None)

if __name__ == '__main__':
    tree = biTree(list('ABC##DE#G##F###'))
    root = tree.creat()
    print(tree.preOrder(root))
    print(tree.midOrder(root))
    print(tree.postOrder(root))




