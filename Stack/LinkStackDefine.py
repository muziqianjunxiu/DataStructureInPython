#定义链栈节点
class StackNode:
    '''
    链栈的节点：包含一个数据域 self.data，   一个指针域 self.next 。
    '''
    def __init__(self):
        self.data=None  
        self.next=None
#定义链栈类
class LinkStack:
    ''' 
    带头节点链栈的初始化：即初始化一个栈顶节点，其数据域为None，指针域next始终指向栈顶元素，是不移动的。
    元素入栈即：该指针next域改为指向该元素，而该元素next域接手指向self.top指向的入栈元素，即之前入栈的元素
    元素出栈即：该指针next域改为指向第二个元素
    而 顺序栈的初始化，其实就是初始化一个数组 s ，用来存放入栈元素，和一个标记 top ，用来指示栈顶位置。
    '''
    def __init__(self):
        self.top=StackNode()
#判断栈是否为空
    def IsEmptyStack(self):
        if self.top.next==None:
            return True
        else:
            return False
#出栈
    def PopStack(self):
        if self.IsEmptyStack():
            print('栈为空')
            return
        else:
            #tStackNode=StackNode()  #StackNode后面的括号不能忘，不然tStackNode就成了StackNode的别名了
            tStackNode=self.top.next
            self.top.next=tStackNode.next
            return tStackNode.data
#入栈
    def PushStack(self,x):
        tStackNode=StackNode()
        tStackNode.data=x
        tStackNode.next=self.top.next
        self.top.next=tStackNode
        print('当前进栈元素为：',x)
#获取栈顶元素
    def GetTopStack(self):
        if self.IsEmptyStack():
            print('栈为空')
            return
        else:
            return self.top.next.data          
#创建栈
    def CreateStackByInput(self):
        data=input('输入入栈元素，“#”键结束：')
        while data!='#':
            self.PushStack(data)
            data=input('输入入栈元素：')
        return
#栈的正序遍历
    def StackTraverse(self):
        if self.IsEmptyStack():
            print('栈为空')
            return
        else:
            #itop=StackNode()   #StackNode后面的括号不能忘，不然itop就成了StackNode的别名了
            itop=self.top
            print('栈内元素依次为：',end='\n')
            while itop.next!=None:
                itop=itop.next
                print(itop.data,end='\t')
            print('\n')
            return   
#栈的反序遍历
    def ReverseStackTraverse(self):        
        if self.IsEmptyStack():
            print('栈为空')
            return
        else:
            itop=self.top
            tlist=[]
            while itop.next!=None:
                itop=itop.next
                tlist.append(itop.data)
            #print(tlist[::-1])
            print('反序输出栈为：')
            for i in reversed(tlist):
                print(i,end='\t')
            print(tlist,tlist[::-1])
            return #list(tlist.reverse())
            #return tlist[::-1]

# la=LinkStack()
# la.CreateStackByInput()
# la.StackTraverse()
# la.ReverseStackTraverse()
