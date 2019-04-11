class StringNode:
    def __init__(self):
        self.data=None
        self.next=None

class StringLink:
    '''
    字符串的链式存储实现:
    约定每个节点都只存放一个字符，并使用带头结点的链表实现串的链式存储，且在链串中增加一个尾指针，以便链串的一些基本操作，如连接等。
    同时使用一个变量记录当前串的长度
    '''
    #初始化顺序串
    def __init__(self):
        self.front=StringNode()
        self.rear=self.front
        self.length=0
    #判断串是否为空
    def IsEmptyString(self):
        if self.length==0:
            return True
        else:
            return False
    #用户输入创建串
    def CreateStringByInput(self):
        stringSH=input('请输入字符串，按回车键结束：')
        while self.length<len(stringSH):
            Tstring=StringNode()
            Tstring.data=stringSH[self.length]
            self.rear.next=Tstring
            self.rear=Tstring
            self.length=self.length+1
    #获取串的长度
    def GetStringLength(self):
        print('串长度为',self.length)
        return self.length
    #获取串的所有字符
    def GetString(self):
        if self.IsEmptyString():
            print('串为空')
            return
        else:
            ifront=StringNode()
            ifront=self.front
            while ifront.next!=None:
                ifront=ifront.next
                print(ifront.data,end='\t')
            return  
    #由串strSrc复制得当前串
    def StringCopy(self,strSrc):
        self.front=strSrc.front
        self.rear=strSrc.rear
        self.length=strSrc.length
    #串strSrc和当前串进行比较
    def StringCompare(self,strSrc):
        if self.length!=strSrc.length:
            print('串不同')
            return
        else:
            ifrontx=self.front
            ifronty=strSrc.front
            while ifrontx.next!=None and ifronty.next!=None:
                ifrontx=ifrontx.next
                ifronty=ifronty.next
                if ifrontx.data!=ifronty.data:
                    print('两串不同')
                    return
            print('两串相同')
            return
    #串的连接
    def StringConcat(self,strSrc):
        self.rear.next=strSrc.front.next
        self.rear=strSrc.rear
        self.length=self.length+strSrc.length
    #串的指定位置插入串
    def StringInsert(self,ipos,strSrc):
        i=0
        ifront=self.front
        while i!=ipos:
            i=i+1
            ifront=ifront.next
        irear=ifront.next
        ifront.next=strSrc.front.next
        strSrc.rear.next=irear
        self.length=self.length+strSrc.length

# test=StringLink()
# test.CreateStringByInput()
# test.GetStringLength()
# test.GetString()
# print('\n')

# test1=StringLink()
# test1.StringCopy(test)
# test1.GetString()
# print('\n')

# test2=StringLink()
# test2.StringInsert(0,test)
# test2.GetString()
# print('\n')

# test3=StringLink()
# test3.StringConcat(test)
# test3.GetString()