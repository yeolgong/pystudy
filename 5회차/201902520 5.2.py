import sys
class DNode:
    def __init__(self,e):
        self.data=e
        self.back=None
        self.next=None

class web:
    def __init__(self):
        first=DNode('www.hufs.ac.kr')
        self.historylist=['www.hufs.ac.kr']
        self.historyout=[]
        self.head=first
        self.tail=first
        self.now=first
        print(first.data)
        
        
        
    def go(self,addr):
        new=DNode(addr)
        '''if self.now == self.head:
            self.head.back=new
            new.back=self.head
            self.tail=new
            self.now=new
            print(self.now.data)'''
        if self.now== self.tail:
            self.tail.next=new
            new.back=self.tail
            self.tail=new
            self.now=new
            self.historylist.append(self.now.data)
            print(self.now.data)
        else:
            new.back=self.now
            self.now.next=new
            self.now=new
            self.tail=new
            self.historylist.append(self.now.data)
            print(self.now.data)
        
        
    def forward(self):
        if self.now==self.tail:
            return
        else:
            self.now=self.now.next
            print(self.now.data)
        
    def backward(self):
        if self.now==self.head:
            return
        else:
            self.now=self.now.back
            print(self.now.data)
        
    def history(self):
        self.historyout=[]
        index=len(self.historylist)-1
        while index >= 0:
            if self.historylist[index] not in self.historyout:
                self.historyout.append(self.historylist[index])
            index-=1
        
        for i in range(len(self.historyout)):
            print(self.historyout[i])
    
    def quit(self):
        exit()    

explore=web()        
while True:
    come=sys.stdin.readline().strip()
    if come[0:2]=='go':
        fun,address=come.split()
    else:
        fun=come
     
    if fun=='go':
        explore.go(address)
    elif fun=='forward':
        explore.forward()
    elif fun=='backward':
        explore.backward()
    elif fun=='history':
        explore.history()
    elif fun=='quit':
        explore.quit()
    
