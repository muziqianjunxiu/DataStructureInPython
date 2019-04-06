from CircularSequenceQueueDefine import CircularSequenceQueue as csq
class Fibonacci:
    '''
    利用2个队列元素的循环队列，实现斐波那契数计算小兔数，
    '''
    def FibonacciMake(self,n):
        qu=csq(2)
        if n==1:
            print('第1个月小兔数量为：1')
            return
        elif n==2:
            print('第2个月小兔数量为：1')
            return
        else:
            qu.EnQueue(1)
            qu.EnQueue(1)
            imonth=2
        while imonth<n:
            NumHead=qu.DeQueue()                        #将队首元素出队，并保存，即N-1个元素
            NumRear=qu.GetHead()                        #获取现队首元素，即之前的第N个元素
            TotalNum=NumHead+NumRear                    #计算第N+1个斐波那契数
            qu.EnQueue(TotalNum)                        #将前两个数之和入队
            imonth=imonth+1
        while qu.GetQueueLength()!=1:                   #当队列长度不为1时，进行出队操作，只留下最后一个元素，即所需的第n个斐波那契数
            qu.DeQueue()
        print('第',n,'个月小兔数量总数为：',qu.DeQueue())

    def TestFabonacci(self):
        n=int(input('输入需要哪个月的小兔数：'))
        while n<0:
          n=int(input('请重新输入：'))
        self.FibonacciMake(n)                           #将用户输入n传入计算函数Fibonacci中

li=Fibonacci()
li.TestFabonacci()

