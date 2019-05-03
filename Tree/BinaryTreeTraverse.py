from collections import deque

class BinNode:
    def __init__(self,val):
        self.left=None
        self.right=None 
        self.val=val
    
    def preOrder(self,root):        #先序遍历递归
        if root==None:
            return
        else:
            print(root.val)
            self.preOrder(root.left)
            self.preOrder(root.right)
    
    def preOrderNoRecur(self,root): #先序遍历非递归
        if root == None:
            return 
        stack=[]                    
        node=root
        while node or stack :
            while node:             #从根节点开始一直找它的左子树
                print(node.val)     #访问节点
                stack.append(node)  #将节点入栈
                node=node.left      #找其左子树，访问，并入栈
            node=stack.pop()        #while结束表示当前节点node为空，即前一个节点没有左子树了
            node=node.right         #开始查看它的右子树

    def inOrder(self,root):             #中序遍历递归
        if root == None:
            return
        self.inOrder(root.left)
        print(root.val)
        self.inOrder(root.right)

    def inOrderNoRecur(self,root):      #中序遍历非递归
        if root==None:
            return
        stack=[]
        node=root
        while node or stack:
            while node:             #从根节点开始，一直找左子树
                stack.append(node)  #将遇到的节点先入栈
                node=node.left      
            node=stack.pop()        #while结束表示当前节点node为空，即前一个节点没有左子树了
            print(node.val)         #此时弹出节点，并访问，
            node=node.right         #开始查看它的右子树

    def postOrder(self,root):               #后序遍历递归
        if root==None:
            return
        self.postOrder(root.left)
        self.postOrder(root.right)
        print(root.val)

    def postOrderNoRecur(sefl,root):        #后序遍历非递归
        if root == None:
            return
        stack1=[]                           #stack1用来遍历节点，stack1需要不停地入栈出栈节点
        stack2=[]                           #stack2用来存储结果
        node=root
        stack1.append(node)
        while stack1:                       #这个while循环用于找到后序遍历的逆序，存在stack2中
            node= stack1.pop()              #pop一下，此时node就会变成右子树节点，就会先处理右子树
            if node.left:                   #这时存储到stack2中的node顺序就会是后序遍历结果的逆序了
                stack1.append(node.left)    #巧就巧在，逆序两字
            if node.right:
                stack1.append(node.right)
            stack2.append(node)
        while stack2:
            print(stack2.pop().val)         #最后只需要一次出栈stack2中元素即可

    def BFS(self,root):         #层次遍历，也称广度优先遍历
        if root ==None:
            return
        quene=deque()           #deque 即双端队列。是一种具有队列和栈的性质的数据结构。双端队列中的元素可以从两端弹出
        node=root 
        quene.append(node)
        while quene:
            node=quene.popleft()    #弹出左边元素
            print(node.val)
            if node.left:
                quene.append(node.left)
            if node.right:
                quene.append(node.right)