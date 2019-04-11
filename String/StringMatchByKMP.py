from StringList import StringList
'''
对BF算法进行改进，即在匹配失败后，重新开始匹配时不改变主串S中的i，只改变模式串T中的j，从而减少匹配的次数

'''
class Indexkmp(StringList):
    #获取模式串next数组的函数
    def GetListNext(self):
        ListNext=[None for x in range(0,100)]
        ListNext[0]=-1
        k=-1
        j=0
        while j<len(self.chars):
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
        i=pos
        j=0
        lengthT=T.GetStringLength()
        lengthS=self.GetStringLength()
        string=T.chars
        while i<lengthS and j<lengthT:
            if j==-1 or self.chars[i]==string[j]:
                i=i+1
                j=j+1
            else:
                j=ListNext[j]
        if j==lengthT:
            print('匹配成功，模式串在主串中第一次出现的位置为：',i-lengthT)
        else:
            print('匹配失败')
    #测试
    def TestIndexKMP(self):
        S=Indexkmp()
        S.CreateString()
        print('主串为：',end=' ')
        S.GetString()
        print()
        T=Indexkmp()
        T.CreateString()
        print('模式串为：',end=' ')
        T.GetString()
        print()
        pos=int(input('请输入从主串中哪一位置开始串的模式匹配：'))
        print('\n借助ListNext值的匹配结果：')
        S.IndexKMP(pos,T,T.GetListNext())
        print('\n借助ListNextValue值的匹配结果')
        S.IndexKMP(pos,T,T.GetListNextValue())

test=Indexkmp()
test.TestIndexKMP()