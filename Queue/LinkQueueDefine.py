class QueueNode:
    #初始化链式队列节点类型
    #一个数据域属性data，一个指针域属性next
    def __init__(self):
        self.data=None
        self.next=None

class LinkQueue:
    '''
    队尾rear 进队
    队头front 出队
    队头指针front 指向的是头结点，即队列第一个元素之前的节点
    队尾指针rear 直接指向队列最后一个元素
    '''
    #初始化队列
    def __init__(self):
        tQueueNode=QueueNode()
        self.front=tQueueNode
        self.rear=tQueueNode
    
    #判断队列是否为空
    def IsEmptyQueue(self):
        if self.front==self.rear:
            return True
        else:
            return False

    #入队
    def EnQueue(self,x):
        tQueueNode=QueueNode()
        tQueueNode.data=x
        self.rear.next=tQueueNode
        self.rear=tQueueNode
        print('当前进队元素为：',x)

    #出队
    def DeQueue(self):
        if self.IsEmptyQueue():
            print('队空')
        else:
            tQueueNode=self.front.next
            self.front.next=tQueueNode.next
            if self.rear==tQueueNode:       #此时原队列中只有一个元素
                self.rear=self.front        #该元素出队后，将队尾指针指向头结点，防止队尾指针丢失
            print('当前出队元素为：',tQueueNode.data)
            return tQueueNode.data
    
    #队列正序遍历
    def QueueTraverse(self):
        if self.IsEmptyQueue():
            print('队列空')
            return
        else:
            ifront=self.front
            print('队列正序输出：')
            while ifront.next!=None:
                ifront=ifront.next
                print(ifront.data)
    
    #队列反序遍历
    def ReverseQueueTraverse(self):
        if self.IsEmptyQueue():
            print('队列空')
            return
        else:
            print('队列反序输出：')
            ifront=self.front
            ls=list()
            while ifront.next!=None:
                ifront=ifront.next
                ls.append(ifront.data)
            #print(ls.reverse())
            for i in reversed(ls):
                print(i)
    
    #获取队头元素        
    def GetHead(self):
        if self.IsEmptyQueue():
            print('队列空')
            return
        else:
            print('队首元素为：',self.front.next.data)
            return self.front.next.data

    #获取队尾元素
    def GetRear(self):
        if self.IsEmptyQueue():
            print('队列空')
            return
        else:
            print('队尾元素为：',self.rear.data)
            return self.rear.data

    #用户输入建队
    def CreateQueueByInPut(self):
        data=input('请输入入队元素，“#”键结束：')
        while data!='#':
            self.EnQueue(data)
            data=input('请输入入队元素：')

# test=LinkQueue()
# test.CreateQueueByInPut()
# test.QueueTraverse()
# test.ReverseQueueTraverse()
# test.GetHead()
# test.GetRear()
# test.DeQueue()
# test.QueueTraverse()
# test.ReverseQueueTraverse()
# test.GetHead()
# test.GetRear()