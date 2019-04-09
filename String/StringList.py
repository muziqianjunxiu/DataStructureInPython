class StringList:
    '''
    字符串的顺序存储实现
    '''
    
    #初始化顺序串
    def __init__(self):
        self.MaxStringSize=256
        self.chars=''

    #判断串是否为空
    def IsEmptyString(self):
        if len(self.chars)==0:
            return True
        else:
            return False

    #创建串
    def CreateString(self):
        stringSH=input('请输入字符串，按回车键结束：')
        if len(stringSH)>self.MaxStringSize:
            print('输入的字符串序列超过分配的存储空间，超过部分无法存入')
            self.chars=stringSH[:self.MaxStringSize]
        else:
            self.chars=stringSH

    #获取串的长度
    def GetStringLength(self):
        print('串长度为',len(self.chars))
        return len(self.chars)

    #获取串的所有字符
    def GetString(self):
        for i in self.chars:
            print(i,end='\t')
                
    #由串strSrc复制得当前串
    def StringCopy(self,strSrc):
        self.chars=strSrc.chars
        return self.chars

    #将当前串与串strSrc进行比较
    def StringCompare(self,strSrc):
        for i in range(0,len(self.chars)+1):
            if self.chars[i]!=strSrc.chars[i]:
                print('两串不同')
                return
        print('两串相同')
        return
                
    #将串strSrc连接到当前串的末尾
    def StringConcat(self,strSrc):
        lengthSrc=strSrc.length
        stringSrc=strSrc.chars
        if lengthSrc + self.length <=self.MaxStringSize:
            self.chars = self.chars + stringSrc
            self.length=lengthSrc+self.length
        else:
            print('两个字符串连接后的长度超过分配的内存，超过的部分无法显示')
            size = self.MaxStringSize-self.length
            self.chars = self.chars + stringSrc[0:size]
            self.length=self.MaxStringSize        

    #从当前串的指定位置ipos获取长度为length的子串
    def SubString(self,ipos,length):
        if ipos>self.length-1 or ipos<0 or length<1 or (length+ipos>self.length):
            print('无法获取子串')
        else:
            substr=self.chars[ipos:ipos+length]
            print('获取的子串为：',substr)

    #从当前串的指定位置ipos删除长度为length的子串
    def StringDelete(self,ipos,length):
        if ipos>self.length-1 or ipos<0 or length<1 or (length+ipos>self.length):
            print('无法删除子串')
        else:
            substrfront=self.chars[0:ipos]
            substrrear=self.chars[ipos+length : self.length]
            self.chars=substrfront+substrrear
            self.length=self.length-length
            print('删除后的子串为：',self.chars,'删除后的串长度为：',self.length)

    #从当前串的指定位置ipos插入串strSrc
    def StringInsert(self,ipos,strSrc):
        if ipos>self.length-1 or ipos<0 or strSrc.length+ipos>self.MaxStringSize:
            print('无法插入子串')
        else:
            substrfront=self.chars[0:ipos]
            substrrear=self.chars[ipos:self.length]
            self.chars=substrfront+strSrc.chars+substrrear
            self.length=self.length+strSrc.length
            print('插入后的串为：',self.chars,'添加后串的长度为：',self.length)

# test=StringList()
# test.CreateString()
# test.GetString()
# print('\n')
# test.GetStringLength()
# print('\n')
# test1=StringList()
# test1.CreateString()
# test1.GetString()
# print('\n')
# test.StringCompare(test1)
# print('\n')
# test2=StringList()
# test2.StringCopy(test)
# test2.GetString()
# test2.StringDelete(0,3)