import LinkStackDefine as LSDf
'''
C语言源程序的{}匹配问题，即出现一个{，必有一个}与之匹配。类似消消乐。
'''
#检查花括号是否匹配的函数
def BracketMatch(self,str):
    ls=LSDf.LinkStack()
    i=0
    while i<len(str):
        if str[i]=='{':
            ls.PushStack(str[i])
            i=i+1
        elif str[i]=='}':
            if ls.GetTopStack()=='{':
                ls.PopStack()
                i=i+1
            else:
                ls.PushStack(str[i])
                i=i+1
        else:
            i=i+1
    if ls.IsEmptyStack()==True:
        print('括号匹配成功')
    else:
        print('括号匹配不成功')
        print('未匹配的括号为：',end=' ')
        ls.ReverseStackTraverse()
#读取文件内容的函数
def ReadFile(self,strFileName):
    f=open(strFileName)
    str=f.read()
    f.close()
    print('要判断的文本如下：')
    print(str)
    return str