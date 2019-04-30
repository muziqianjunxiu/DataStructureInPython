'''
广义表一般记作：LS=(a[0],a[1],a[2]...a[n-1]),称为LS的书写形式串，其中LS是广义表的名称，a[i]是广义表的数据元素，既可以是基本的数据元素，此时我们称a[i]是广义表LS的原子。也可以是广义表，此时称a[i]为广义表的子表
LS中括号的最大嵌套层数被称为深度，而表中元素的个数称为长度，即n 
n>0时LS为非空表。我们称第一个元素a[0]为LS的表头，称剩余元素组成的表（a[1],a[2]....a[n-1]）为表尾。
n=0时LS为空表，此时LS的表头为空，表尾为空表。
表尾是广义表中除了第一个元素以为剩余元素组成的表，所以广义表的表尾一定是一个广义表。
广义表的数据元素既可以是原子也可以是广义表，所以采用链式存储。
这里我们将广义表的每一层看作一个线性表，对该层数据的存储采用类似于线性表的存储方式，这种方式称为扩展线性链表存储结构。即：将原子和广义表都看作是子表。
只定义一种节点：该节点包含标志域tag、联合域union、和指针域next    其中tag为1时表示该节点时表节点，此时union中存放当前表的子表的地址；tag为0时表示是原子节点，此时union中存放原子值。
next域存放下一节点的地址。
'''
import copy

class GLNode:                                               #创建表节点
    def __init__(self):                                     #该节点包含标志域tag、联合域union、和指针域next                                                
        self.tag=1                                          #其中tag为1时表示该节点时表节点，此时union中存放当前表的子表的地址；tag为0时表示是原子节点，此时union中存放原子值。
        self.union=None                                     #next域存放下一节点的地址
        self.next=None

class GList:
    #创建广义表，以“#”代表空表。
    def CreateGList(self,Table):
        if len(Table)>0:
            tTable=Table.pop(0)
            tGLNode=GLNode()
            if tTable=='(':                                 #若为真，说明接下来处理的是表
                tGLNode.tag=1                               #将标志域置1
                tGLNode.union=self.CreateGList(Table)       #递归创建广义表，并同时将其地址存入节点的联合域union中
            elif tTable==')' or tTable=='#':                #若为')',说明当前子表处理完毕。若为'#'，说明当前子表为空表
                tGLNode=None                                #则将节点设置为None
            else:                                           #若上述条件都不满足，说明tTable为原子，
                tGLNode.tag=0                               #此时将标志域置0
                tGLNode.union=tTable                        #并将tTable值存入节点union域中
        else:                                               #若传入序列为空
            tGLNode=None                                    #将节点置为None
        if  len(Table)>0:                                   #
            tTable=Table.pop(0)
        if  tGLNode!=None:                                  #此时说明表不为空
            if tTable==',':                                 #判断当前待处理字符是否为','，
                tGLNode.next=self.CreateGList(Table)        #递归创建当前表的后继元素，并将其地址存入tGLNode的指针域中  
            else:                                           
                tGLNode.next=None                           #若没有后继元素，则将tGLNode的指针域置为None
        return tGLNode                                      #返回tGLNode以便其他函数调用

    #遍历广义表
    def TraverseGList(self,GList):
        if GList != None:
            if GList.tag==0:                                #判断标志位，此时是原子，
                print(GList.union,end=' ')                  #直接将联合域中原子值输出
            else:                                           #否则为子表
                print('(',end='')                           #先打印'('
                if GList.union==None:                       #判断是否为空表
                    print('#',end=' ')                      #用‘#’代表空表
                else:                                       #不为空表时
                    self.TraverseGList(GList.union)         #递归遍历当前子表
                print(')',end=' ')                          #子表遍历完，打印')'
            if GList.next!=None:                            #判断当前子表是否还有后继元素需处理
                print(',',end=' ')                          #若有，则打印','
                self.TraverseGList(GList.next)              #递归遍历当前子表后继元素的子表
    
    #获取广义表表头的函数
    def GetGListHead(self,GList):
        if GList != None  and  GList.union != None:
            head=copy.deepcopy(GList.union)
            head.next=None
            return head
        else:
            print('无法获取表头！')
    
    #获取广义表表尾的函数
    def GetGListTail(self,GList):
        if GList != None and GList.union != None:
            tail= copy.deepcopy(GList.union.next)
            return tail
        else:
            print('无法获取表尾！')

