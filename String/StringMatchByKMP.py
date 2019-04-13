from StringList import StringList
'''
对BF算法进行改进，即在匹配失败后，重新开始匹配时不改变主串S中的i，只改变模式串T中的j，从而减少匹配的次数
改变模式串T中的j，依据的则是模式串的next数组值
'''
class Indexkmp(StringList):
    #获取模式串next数组的函数
    def GetListNext(self):
        '''
        求字符串next数组的方法，其实就是将字符串作为模式串与自己进行匹配，特殊的地方是：模式串要从主串第二个元素起开始匹配
        '''
        ListNext=[None for x in range(0,100)]           #初始化next数组 
        ListNext[0]=-1                                  #将next[0]置为-1
        k=-1                                            #k为循环变量                    
        j=0                                             #模式串 循环变量j 与 主串 循环变量k 的下一个位置开始对比
        while j<len(self.chars):                        #匹配一直进行到模式串结束
            if k==-1 or self.chars[j]==self.chars[k]:   
                k=k+1
                j=j+1
                ListNext[j]=k
            else:
                k=ListNext[k]
        return ListNext
    #获取模式串next数组的函数改进
    def GetListNextValue(self):
        ListNextValue=[None for x in range(0,100)]
        ListNextValue[0]=-1
        k=-1
        j=0
        while j<len(self.chars)-1:
            if k==-1 or self.chars[j]==self.chars[k]:
                k=k+1
                j=j+1
                if self.chars[j]!=self.chars[k]:
                    ListNextValue[j]=k
                else:
                    ListNextValue[j]=ListNextValue[k]
            else:
                k=ListNextValue[k]
        return ListNextValue
    #KMP算法
    def IndexKMP(self,pos,T,ListNext):
        i=pos                                   #将开始匹配位置赋值给i
        j=0                                     #模式串匹配位置下标
        lengthT=T.GetStringLength()             #获取模式串长度
        lengthS=self.GetStringLength()          #获取主串长度
        while i<lengthS and j<lengthT:          
            if j==-1 or self.chars[i]==T.chars[j]:  #字符匹配时，主串和模式串下标皆后移
                i=i+1
                j=j+1
            else:               #当不匹配出现时，主串i位置不动，依据模式串的next数组值将模式串进行移动
                j=ListNext[j]
        if j==lengthT:          #说明模式串匹配完全，匹配成功
            print('匹配成功，模式串在主串中第一次出现的位置为：',i-lengthT)
        else:
            print('匹配失败')
    #测试
    def TestIndexKMP(self):
        S=Indexkmp()
        S.CreateString()                #输入主串
        print('主串为：',end=' ')
        S.GetString()
        print()
        T=Indexkmp()
        T.CreateString()                #输入模式串
        print('模式串为：',end=' ')
        T.GetString()
        print()
        pos=int(input('请输入从主串中哪一位置开始串的模式匹配：'))  #输入从主串何处开始匹配
        print('\n借助ListNext值的匹配结果：')
        S.IndexKMP(pos,T,T.GetListNext())
        print('\n借助ListNextValue值的匹配结果')
        S.IndexKMP(pos,T,T.GetListNextValue())

test=Indexkmp()
test.TestIndexKMP()