import sys
class web:
    def __init__(self):
        self.addrlist=['www.hufs.ac.kr']    #초기사이트 설정
        self.historylist=['www.hufs.ac.kr'] #방문기록을 저장하는 리스트
        self.historyout=[]                  #나중에 중복제거하고 출력할 방문기록 리스트
        self.index=0
        self.search=0
        print(self.addrlist[0])             #초기사이트 출력
        
    def go(self,addr):
        self.index +=1
        if self.index==len(self.addrlist):  #최근방문 상태에서 새로 이동
            self.addrlist.append(addr)
            self.historylist.append(addr)   #go 했을때만 기록리스트에 저장
        else:                               #뒤로가기한 상태에서 새로 이동
            self.addrlist[self.index]=addr
            self.historylist.append(addr)   #go 했을때만 기록리스트에 저장
        print(self.addrlist[self.index])
        self.search=self.index+1
        for i in range(len(self.addrlist)-self.search): #뒤로가기한 상태에서 이동 후 뒤에있는 사이트 리스트에서 제거
            del self.addrlist[self.search]
        return
        
        
    def forward(self):  #앞으로 가기 구현
        self.index +=1
        if self.index>=len(self.addrlist):  #다음 주소가 없을 경우 현재사이트는 바뀌지 않고 출력결과x
            self.index -=1
            return
        else:
            print(self.addrlist[self.index])
        
    def backward(self): #뒤로 가기 구현
        self.index -=1
        if self.index<0:     #이전 주소가 없을 경우 현재사이트는 바뀌지 않고 출력결과x
            self.index +=1
            return
        else:
            print(self.addrlist[self.index])
            
    def history(self):  #history구현
        self.historyout=[]  #history를 여러번 구현할 경우를 대비한 빈 리스트로 초기화
        index=len(self.historylist)-1
        while index >= 0:   #중복제거, 방문한 역순이기 때문에 리스트안 원소를 반대방향으로 검사
            if self.historylist[index] not in self.historyout:
                self.historyout.append(self.historylist[index])
            index-=1
        
        for i in range(len(self.historyout)):
            print(self.historyout[i])
            
            
    def quit(self):
        exit()

explore=web()        
while True:
    come=sys.stdin.readline().strip() #한꺼번에 입력시 일부 함수호출이 무시돼서 stdin으로 구현
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
        
