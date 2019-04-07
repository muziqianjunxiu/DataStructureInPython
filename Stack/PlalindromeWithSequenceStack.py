#判断单词是否为回文数
from SequenceStackDefine import SequenceStack
#定义两个栈，分别将单词顺序入栈，反序入栈，再比较两个栈内容。
def Plalindrome(str):
    ss1=SequenceStack(20)#初始化两个栈
    ss2=SequenceStack(20)

#将字符串顺序入栈    
    i=0
    while i<(len(str)):
        ss1.PushStack(str[i])
        i=i+1
    print('栈ss1内元素依次为：',end='\n')
    ss1.StackTraverse()
#将字符串反序入栈
    i=i-1
    while i<(len(str)) and i>=0:
        ss2.PushStack(str[i])
        i=i-1
    print('栈ss2内元素依次为：',end='\n')
    ss2.StackTraverse()
#两个栈一起pop，比较元素是否一样
    while ss1.IsEmptyStack() !=True:
        if ss1.PopStack() != ss2.PopStack():
            print(str,'不是回文单词')
            return
    print(str,'是回文单词')
#判断输入是否合法
def TestPlalindrome():
    str=input('输入待测单词：')
    i=0
    while i<len(str):
        if (str[i]>='a' and str[i]<='z') or (str[i]>='A' and str[i]<='Z'):
            i=i+1
        else:
            break
    if i==len(str):
        Plalindrome(str)
    else:
        print('输入错误')
TestPlalindrome()
