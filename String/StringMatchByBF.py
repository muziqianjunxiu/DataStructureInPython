from StringList import StringList 

'''
BF算法，字符串暴力匹配算法，挨位匹配。
从主串指定位置pos处开始进行模式匹配。
'''
class TestIndex(StringList):
    '''
    创建类TestIndex，从类StringList继承，并创建自己方法IndexBF，该方法接收两个参数：pos表示从主串指定位置开始模式匹配，T为模式串。
    '''
    def IndexBF(self,pos,T):
        lengthT=T.GetStringLength()     #获取模式串长度
        lengthS=self.GetStringLength()  #获取主串长度
        if lengthT>lengthS:             #如果模式串长度大于主串长度，则不匹配
            print('子串的长度大于主串的长度，无法进行字符串的匹配')
        else:
            i=pos                       #将开始位置参数用i记录，从主串的i位置开始匹配
            while(lengthS-i>=lengthT):  #主串中剩余字符位数大于等于模式串位数时，才进行匹配
                iT=i                    #记录本次匹配循环开始位置
                j=0                     #模式串匹配位置
                tag=False               #匹配成功标志位
                while j<lengthT:        #表示模式串未匹配完
                    if self.chars[i]==T.chars[j]:   #主串和模式串逐位进行匹配
                        i=i+1
                        j=j+1
                    else:
                        break       #不成功则调出匹配，
                if j==lengthT:      #此时模式串匹配完全，表示匹配成功
                    print('匹配成功。模式串在主串中首次出现的位置为：',iT)
                    tag=True        #标志位置真
                    break           #跳出循环
                else:               #否则将i加1，即从主串的下一位置再次进行上述匹配过程
                    i=iT+1
            if tag==False:          #检查标志位
                print('匹配失败')
            return
    #测试
    def TestIndexBF(self):
        S=TestIndex()
        S.CreateString()
        print('主串为：',end='\n')
        S.GetString()
        T=TestIndex()
        T.CreateString()
        print('模式串为：',end='\n')
        T.GetString()
        ipos=int(input('请输入从主串哪一位置开始模式匹配：'))
        print('匹配结果：',end='\n')
        S.IndexBF(ipos,T)
              
test=TestIndex()
test.TestIndexBF()