#linked_list=[[1,2],[1,4],[4,3],[5,5],[1,7],[4,6],[3,8],[6,-1],[2,1]]
'''
x=len(linked_list)
def traverse(i):
    print(linked_list[i][0])
    if linked_list[i][1]!=-1:
        traverse(linked_list[i][1])
traverse(0)
'''
'''
def traverse(i):
    if linked_list[i][1]!=-1:
        traverse(linked_list[i][1])
    else:
        linked_list[i][1]=len(linked_list)

def add(data):
    node=[data,-1]
    traverse(0)
    linked_list.append(node)
    print(linked_list)

add(8)
'''

class node():
    def __init__(self,data):
        self.data=data
        self.next=None
    
class linked_list():
    def __init__(self,head,tail,length):
        self.head=head
        self.tail=tail
        self.length=length
    
    def add(self,llnode):
        if self.length==0:
            self.head=llnode
            self.tail=llnode
            self.length+=1

        else:
            self.tail.next=llnode
            self.tail=llnode
            self.length+=1
    
    #  llindex = 1 代表插入到第0个和第1个节点之间
    def insert(self,llindex,llnode):
        if llindex==1:
            llnode.next=self.head
            self.head=llnode
            self.length+=1
        
        #指针初始化在0和1的空当,before_pointer对应指针前的节点,after_pointer对应指针后的节点
        pointer=1
        before_pointer=None
        after_pointer=self.head
        
        #开始遍历，直到找到llindex对应的两个节点间的空当
        while pointer<llindex:
            before_pointer=after_pointer
            after_pointer=after_pointer.next
            pointer+=1
        
        #指针找到llindex
        if pointer==llindex and llindex!=1:
            llnode.next=after_pointer
            before_pointer.next=llnode
            self.length+=1

    def return_linked_list(self):
        temp=[]
        xnode=self.head
        while xnode!=None:
            temp.append(xnode.data)
            xnode=xnode.next
        
        return temp
    
    def search(self,data):
        acc=0
        llnode=self.head
        while llnode.data!=data:
            llnode=llnode.next
            acc+=1
        return acc

a=linked_list(None,None,0)
a.add(node(1))
a.add(node(5))
a.add(node(3))
a.add(node(4))

#a.insert(3,node(2))

print(a.search(5))


#print(a.return_linked_list())

