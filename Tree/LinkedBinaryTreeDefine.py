
class LinkedBinaryTreeNode:   #二叉树的节点定义
    def __init__(self):
        self.data=None
        self.left=None 
        self.right=None     

class LinkedBinaryTree:
    #创建二叉树
    def CreateTree(self,root,val):
        newnode=LinkedBinaryTreeNode()
        newnode.data=val
        newnode.left=None
        newnode.right=None
        if root==None:
            root=newnode
            return root
        else:
            current=root
            while current!=None:
                backup=current
                if val < current.data:
                    current=current.left
                else:
                    current=current.right
            #current = newnode  或者：
            if val < backup.data:       
                backup.left = newnode                                                     
            else:                       
                backup.right=newnode    
            return root
    
    #用户输入创建二叉树
    def CreateTreeByInput(self):
        ls=list(input('请输入二叉树序列：'))
        root=None
        for i in ls:
            root=self.CreateTree(root,i)
    
    #中序遍历       遍历结果即是元素从小到大排序结果
    def InOrder(self,root):
        if root!=None:
            self.InOrder(root.left)
            print('[%2d]' %root.data,end='')
            self.InOrder(root.right)

    #后序遍历
    def PostOrder(self,root):
        if root!=None:
            self.PostOrder(root.left)
            self.PostOrder(root.right)
            print('[%2d]' %root.data,end='')

    #前序遍历
    def PreOrder(self,root):
        if root!=None:
            print('[%2d]' %root.data,end='')
            self.PreOrder(root.left)
            self.PreOrder(root.right)

    #查找元素
    def Search(self,root,val):
        while True:
            if root==None:
                return None
            if root.data==val:
                return root 
            elif root.data > val:
                root=root.left
            else:
                root=root.right

    #插入节点
    def InsertNode(self,root,data):
        if self.Search != None:
            print('二叉树中已有此节点')
        else:
            root=self.CreateTree(root,data)
    
    #寻找最小节点值
    def FindMin(self, root):
        if root:
            while root.left:
                root = root.left
        return root

    #删除值为val的节点
    def DeleteNode(self,root,val):
        if root:
            if val < root.data:
                self.DeleteNode(root.left,val)
            elif val > root.data:
                self.DeleteNode(root.right,val)
            elif val==root.data:
                if root.left and root.right:
                    tmp = self.FindMin(root.right)
                    root.data = tmp.data
                    root.right = self.DeleteNode(root.right,root.data)
                elif root.left==None and root.right !=None:
                    root = root.right
                elif root.right==None and root.left !=None:
                    root = root.left
                else:
                    root=None
                    print('树已空')
                    return
            else:
                print('找不到该节点')
                return            
        else:
            print('树为空')
            return


'''
#-----------------------------------------------另一种实现               
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BinarySearchTree:
    #插入节点
    def Insert(self, root, x):
        if root == None:
            root = TreeNode(x)
        else:
            if x < root.val:
                root.left = self.Insert(root.left, x)
            if x > root.val:
                root.right = self.Insert(root.right, x)
        return root
    #删除值为x节点
    def Delete(self, root, x):
        if root:
            if x < root.val:
                root.left = self.Delete(root.left, x)
            elif x > root.val:
                root.right = self.Delete(root.right, x)
            elif root.left and root.right:
                tmp = self.FindMin(root.right)
                root.val = tmp.val
                root.right = self.Delete(root.right, root.val)
            else:
                tmp = root
                if root.left is None: 
                    root = root.right
                elif root.right is None: 
                    root = root.left
        return root
    #寻找最小节点值
    def FindMin(self, root):
        if root:
            while root.left:
                root = root.left
        return root
'''

    
