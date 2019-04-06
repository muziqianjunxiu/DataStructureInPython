class SequenceQueue:
    '''
    循环队列采用数组存储，另外需要两个int值记录队首和队尾位置，相当于指针的功能。
    队头指针front始终指向队首元素所在位置的前一个位置， 队尾指针rear直接指向队尾元素
    元素个数：rear-front
    队空条件：front==rear
    队满条件：rear==MaxQueueSize-1
    '''
#初始化顺序队列
    def __init__(self,Max):
        self.MaxQueueSize=Max+1
        self.s=[None for x in range(0,self.MaxQueueSize)]
        self.front=0
        self.rear=0

#判断队列是否为空
    def IsEmptyQueue(self):
        if self.front==self.rear:
            return True
        else:
            return False
#判断队列是否已满
    def IsFullQueue(self):
        if self.rear==self.MaxQueueSize-1:
            return True
        else:
            return False
#入队
    def EnQueue(self,element):
        if self.rear<self.MaxQueueSize:
            self.rear=self.rear+1
            self.s[self.rear]=element
            print('当前进队的元素为：',element)
        else:
            print('队列满，无法进队')
            return
#出队
    def DeQueue(self):
        if self.IsEmptyQueue():
            print('队空')
            return
        else:
            self.front=self.front+1
            return self.s[self.front]
#队列元素遍历
    def QueueTraverse(self):
        if self.IsEmptyQueue():
            print('队空')
            return
        else:
            ifront=self.front
            print('队列正序为：\n')
            while ifront!=self.rear:
                ifront=ifront+1
                print(self.s[ifront])
            return
#队内元素反向遍历
    def ReverseQueueTraverse(self):
        if self.IsEmptyQueue():
            print('队空')
            return
        else:
            irear=self.rear
            print('队列逆序为：\n')
            while irear!=self.front:
                print(self.s[irear])
                irear=irear-1
            return
#获取队头元素
    def GetHead(self):
        if self.IsEmptyQueue():
            print('队空')
            return
        else:
            return self.s[self.front+1]
#获取队尾元素
    def GetRear(self):
        if self.IsEmptyQueue():
            print('队空')
            return
        else:
            return self.s[self.rear]        
#获取队列长度
    def GetQueueLength(self):
        return int(self.rear-self.front)
#用户输入建队
    def CreateQueueByInput(self):
        data=input('输入入队元素，‘#’键结束：')
        while data!='#':
            self.EnQueue(data)
            data=input('输入入队元素：')

# ls=SequenceQueue(4)
# ls.CreateQueueByInput()
# ls.QueueTraverse()
# ls.ReverseQueueTraverse()