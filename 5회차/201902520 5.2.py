
class DNode:
    def __init__(self,e):
        self.data=e
        self.back=None
        self.next=None

class web:
    def __init__(self):
        first=DNode('www.hufs.ac.kr')
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
            print(self.now.data)
        else:
            new.back=self.now
            self.now.next=new
            self.now=new
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
    
    def quit(self):
        exit()    
    