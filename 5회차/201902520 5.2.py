import sys
class DNode:        #이중연결리스트로 구현
    def __init__(self,e):
        self.data=e
        self.back=None
        self.next=None

class web:      
    def __init__(self):
        first=DNode('www.hufs.ac.kr') #초기 사이트 설정
        self.historylist=['www.hufs.ac.kr'] #go한 사이트 기록
        self.historyout=[]  #사이트 기록 출력위한 리스트
        self.head=first
        self.tail=first
        self.now=first
        print(first.data)   #초기사이트 출력
        
        
        
    def go(self,addr):
        new=DNode(addr)
        if self.now== self.tail:    #마지막 방문상태에서 새로 이동 
            self.tail.next=new
            new.back=self.tail
            self.tail=new           #마지막 값 tail을 새로 방문한 주소로 설정
            self.now=new            #현재 사이트를 새로 방문한 주소로 설정
            self.historylist.append(self.now.data)
            print(self.now.data)
        else:                       #뒤로가기 한 상태에서 새로 이동
            new.back=self.now
            self.now.next=new
            self.now=new    #현재 사이트를 새로 방문한 주소로 설정
            self.tail=new   #마지막 값 tail을 새로 방문한 주소로 설정
            self.historylist.append(self.now.data)
            print(self.now.data)
        
        
    def forward(self):              #앞으로 가기
        if self.now==self.tail:     #더이상 앞으로 갈 수 없음
            return
        else:
            self.now=self.now.next
            print(self.now.data)
        
    def backward(self):             #뒤로 가기
        if self.now==self.head:     #더이상 뒤로 갈 수 없음
            return
        else:
            self.now=self.now.back
            print(self.now.data)
        
    def history(self):              #go한 사이트 기록 역순으로 출력
        self.historyout=[]          #history 여러번 구현을 위한 출력리스트 비우기
        index=len(self.historylist)-1   #역순이므로 반대로 중복검사
        while index >= 0:
            if self.historylist[index] not in self.historyout:
                self.historyout.append(self.historylist[index])
            index-=1
        
        for i in range(len(self.historyout)):   #history출력
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
    
