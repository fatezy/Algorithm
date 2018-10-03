class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None




class biTree:
    def __init__(self,list):
        self.list = list


    def creatTree(self,root,i):
        if i<len(self.list):
            if self.list[i] =='#':
                return None
            else:
                root = TreeNode(self.list[i])
                root.left = self.creatTree(root.left,2*i+1)
                root.right = self.creatTree(root.left,2*i+2)
                return root
        return root


    def creat(self):
        return self.creatTree(None,0)

if __name__ == '__main__':
    tree = biTree([1,2,3,'#',4,5])
    root = tree.creat()
    print(1)





