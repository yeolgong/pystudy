import sys
class web:
    def __init__(self):
        self.addrlist=['www.hufs.ac.kr']
        self.historylist=['www.hufs.ac.kr']
        self.historyout=[]
        self.index=0
        self.search=0
        print(self.addrlist[0])
        
    def go(self,addr):
        self.index +=1
        if self.index==len(self.addrlist):  #최근방문 상태에서 새로 이동
            self.addrlist.append(addr)
            self.historylist.append(addr)
        else:                               #한번 방문한 상태에서 새로 이동
            self.addrlist[self.index]=addr
            self.historylist.append(addr)
        print(self.addrlist[self.index])
        self.search=self.index+1
        for i in range(len(self.addrlist)-self.search):
            del self.addrlist[self.search]
        return
        
        
    def forward(self):
        self.index +=1
        if self.index>=len(self.addrlist):
            self.index -=1
            return
        else:
            #self.historylist.append(self.addrlist[self.index])
            print(self.addrlist[self.index])
        
    def backward(self):
        self.index -=1
        if self.index<0:
            self.index +=1
            return
        else:
            #self.historylist.append(self.addrlist[self.index])
            print(self.addrlist[self.index])
            
    def history(self):
        self.historyout=[]
        index=len(self.historylist)-1
        while index >= 0:
            if self.historylist[index] not in self.historyout:
                self.historyout.append(self.historylist[index])
            index-=1
        
        for i in range(len(self.historyout)):
            print(self.historyout[i])
            
            
    def quit(self,addr=''):
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
        