'''
遍历二叉树是对非线性结构结点的线性化过程，
由此得到的遍历序列中，每个结点有且仅有一个前驱和后继（除了序列中的第一个和最后一个结点）。
遍历线索二叉树的时间复杂度为O(n)，与递归或非递归遍历二叉链表一样，
但前者的空间复杂度为O(1)，而后者为O(n)，因为遍历线索二叉树不需要栈。
由于有了结点的前驱和后继信息，线索二叉树的遍历和指定次序下查找结点的前驱和后继算法都变得简单。
线索二叉树的遍历不需要设栈，避免了频繁的进栈、出栈，因此在时间和空间上都较遍历二叉树节省。
因此，若需要经常查找结点在所遍历线性序列中的前驱和后继，则采用线索链表作为存储结构。
构造线索二叉树实质上是将二叉链表中的空指针域改为前驱、后继指针域。
又因为前驱、后继的信息只有在遍历的时候才能得到，所以线索化的过程就是在遍历的时候修改空指针的过程。
'''
class Node:
    def __init__(self):
        self.val=0
        self.left=None
        self.right=None
        self.left_thread=0
        self.right_thread=0
root=Node()
root=None    
class ThreadBinaryTree:
    #将指定的值加入线索二叉树
    def add_node_to_tree(val):
        global root
        newnode=Node()
        newnode.val=val
        newnode.left_thread=0
        newnode.right_thread=0
        newnode.left=None
        newnode.right=None
        previous=Node()
        previous.val=val
        previous.left=None
        previous.right=None
        previous.left_thread=0
        previous.right_thread=0
        #设置线索二叉树的开头节点
        if root==None:
            root=newnode
            root.left=root
            root.right=None 
            root.left_thread=0
            root.right_thread=1
            return root
        #设置开头节点所指节点
        current=root.right
        if current==None:
            root.right=newnode
            newnode.left=root
            newnode.right=root
            return root
        parent=root #父节点是开头节点
        pos=0       #设置二叉树中的行进方向
        while current!=None:
            if current.val>val:
                if pos!=-1:
                    pos=-1
                    previous=parent
                parent=current
                if current.left_thread==1:
                    current=current.left
                else:
                    current=None
            else:
                if pos!=1:
                    pos=1
                    previous=parent
                parent=current
                if current.right_thread==1:
                    current=current.right
                else:
                    current=None
        if parent.val>val:
            parent.left_thread=1
            parent.left=newnode
            newnode.left=previous
            newnode.right=parent
        else:
            parent.right_thread=1
            parent.right=newnode
            newnode.left=parent
            newnode.right=previous
        return root
    #线索二叉树中序遍历
    def trace():
        global root
        tempnode=root
        while True:
            if tempnode.right_thread==0:
                tempnode=tempnode.right
            else:
                tempnode=tempnode.right
                while tempnode.left_thread!=0:
                    tempnode=tempnode.left  
            if tempnode!=root:
                break

#主程序
i=0
array_size=11
print('线索二叉树建立后，以中序遍历有排序的效果：')
print('第一个数字为线索二叉树的开头节点，不列入排序')
data1=[0,10,11,12,13,14,15,16,17,18,19,20,21]
for i in range(array_size):
   ThreadBinaryTree.add_node_to_tree(data1[i])
print('--------------------------------------------')
print('范例1')
print('数字从小到大排序为：')
ThreadBinaryTree.trace()