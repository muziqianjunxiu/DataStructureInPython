class CircularSequenceQueue:
    '''
    元素个数：(rear-front+MaxQueueSize) % MaxQueueSize
    队空条件：front==rear
    队满条件：front==(rear+1) % MaxQueueSize
    '''
#初始化循环顺序队列
    def __init__(self,MaxSize):
        self.MaxQueueSize=MaxSize+1
        self.s=[None for x in range(0,self.MaxQueueSize)]
        self.front=0
        self.rear=0
#判断队列是否为空
    def IsEmptyQueue(self):
        if self.front==self.rear:
            return True
        else:
            return False
#入队
    def EnQueue(self,x):
        if self.front!=(self.rear+1) % self.MaxQueueSize:
            self.rear=(self.rear+1) % self.MaxQueueSize
            self.s[self.rear] = x
            #print('当前进队元素为：',x)
        else:
            print('队列已满，无法入队')
            return
#出队
    def DeQueue(self):
        if self.IsEmptyQueue():
            print('队列为空，无法出队')
            return 
        else:
            self.front=(self.front+1) % self.MaxQueueSize
            #print('当前出队元素为',self.s[self.front])
            return self.s[self.front]
#队列元素正序遍历
    def QueueTraverse(self):
        if self.IsEmptyQueue():
            print('队列为空')
            return
        else:
            ifront=self.front
            print('正序输出队列：')
            while ifront!=self.rear:
                ifront=(ifront+1) % self.MaxQueueSize
                print(self.s[ifront])
            return
#反序遍历队列元素
    def ReverseQueueTraverse(self):
        if self.IsEmptyQueue():
            print('队列为空')
            return
        else:
            irear=self.rear
            print('反序输出队列：')
            while irear!=self.front:
                print(self.s[irear])
                irear=(irear-1+self.MaxQueueSize) % self.MaxQueueSize
            return
#获取队首元素
    def GetHead(self):
        if self.IsEmptyQueue():
            print('队列为空')
            return
        else:
            return(self.s[(self.front+1)%self.MaxQueueSize]) 
#获取队尾元素
    def GetRear(self):
        if self.IsEmptyQueue():
            print('队列为空')
            return
        else:
            return(self.s[self.rear])
#获取队列长度
    def GetQueueLength(self):
        return (self.rear-self.front+self.MaxQueueSize) % self.MaxQueueSize
#以用户输入创建队列
    def CreateQueueByInput(self):
        data=input('输入入队元素，“#”键结束：')
        while data !='#':
            self.EnQueue(data)
            data=input('输入入队元素：')
        return

# ls=CircularSequenceQueue(5)   #使用1,2,3,4,5测试
# ls.CreateQueueByInput()       
# ls.QueueTraverse()
# ls.ReverseQueueTraverse()
# ls.DeQueue()
# ls.EnQueue(0)
# ls.QueueTraverse()
# ls.ReverseQueueTraverse()