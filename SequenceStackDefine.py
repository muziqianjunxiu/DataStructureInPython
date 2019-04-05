#栈
class SequenceStack:
    '''
    顺序栈的节点属性self.top值指示栈顶位置，值为-1时表示栈空。栈内元素采用数组s存储，下标值与self.top值对应。
    入栈操作时，self.top的值增一，并将元素存入s数组中self.top对应下标的位置处；实现了self.top始终指向栈顶元素。
    出栈操作时，将s数组中self.top对应下标的元素删除，self.top的值减一，self.top依然指示栈顶元素。
    '''
    def __init__(self,Max):
        '''
        顺序栈的初始化，其实就是初始化一个数组 s ，用来存放入栈元素，和一个标记 top ，用来指示栈顶位置。
        而链栈的初始化，是要初始化一个节点，此节点包含一个数据域 self.data 用来存放入栈元素，和一个指针域self.next ，用来指示栈顶位置。
        '''
        self.MaxStackSize=Max
        self.s = [None for x in range(0,self.MaxStackSize)]
        self.top = -1
#判断栈是否为空
    def IsEmptyStack(self):
        if self.top == -1:
            iTop = True
        else:
            iTop = False
        return iTop
#进栈函数
    def PushStack(self,x):
        if self.top < self.MaxStackSize-1:
            self.top = self.top+1
            self.s[self.top] = x
        else:
            print('栈满')
            return
#出栈函数
    def PopStack(self):
        if self.IsEmptyStack():
            print('栈为空')
            return
        else:
            iTop = self.top
            self.top = self.top-1
            return(self.s[iTop])
#获取栈顶元素
    def GetTopStack(self):
        if self.IsEmptyStack():
            print('栈为空')
            return 
        else:
            return self.s[self.top]
#遍历栈内元素
    def StackTraverse(self):
        if self.IsEmptyStack():
            print('栈为空')
            return
        else:
            for i in range(0,self.top+1):
                print(self.s[i],end='\n')
#通过用户输入建栈
    def CreateStackByInput(self):
        data=input('输入元素，结束按"#"键：')
        while data !='#':
            self.PushStack(data)
            data=input('输入元素，结束按“#”键：')
#销毁栈
    def DestoryStack(self):
        if self.IsEmptyStack():
            print('栈为空')
            return
        else:
            self.top = -1
            del self.s[:]
#获取栈长度
    def GetStackLength(self):
        i=0
        if self.IsEmptyStack():
            print('栈为空')
            return 0
        else:
            itop=self.top
            while itop !=-1:
                itop=itop-1
                i=i+1
            return i
#判断元素是否在栈中
    def ItemInStack(self,x):
        if self.IsEmptyStack():
            print('栈为空')
            return 
        else:
            for i in range(0,self.GetStackLength()):
                if self.s[i] == x:
                    return True
                else:
                    return False 

#访问注释文档，使用__doc__方法，不用带（）
print(SequenceStack.__doc__)