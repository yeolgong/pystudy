import math #나중에 반올림 계산을 위함
class Queue:    #원형 큐 구현
    Max_Qsize=200
    def __init__(self):
        self.items=[None]*Queue.Max_Qsize
        self.front=-1
        self.rear=-1
        self.size=0
        
    def isEmpty(self):  
        return self.size==0
    
    def enqueue(self,e):
        if self.size == len(self.items):
            print("Queue is full")
            self.resize(2*len(self.items))
        else:
            self.rear=(self.rear+1)%(len(self.items))
            self.items[self.rear]=e
            self.size=self.size+1
            
    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            self.front=(self.front+1)%(len(self.items))
            e=self.items[self.front]
            self.size=self.size-1
            return e
        
    def resize(self, cap):
        olditems = self.items
        self.items = [None]*cap
        walk = self.front
        for k in range(self.size):
            self.items[k] = olditems[walk]
            walk = (walk + 1)% len(olditems)
        self.front = -1
        self.rear = self.size - 1


people=int(input()) #사람의 수 입력받음 200이하
cometime_queue=Queue()  #이전사람 도착후 다음사람 도착하는데 걸리는 시간 저장하는 큐
dotime_queue=Queue()    #한사람마다 심사하는데 걸리는 시간을 저장하는 큐

for i in range(people): #도착하는데 걸리는 시간과 심사하는데 걸리는 시간을 입력받고 정수로 변환
    cometime_1man, dotime_1man= input().split()
    cometime_1man=int(cometime_1man)
    dotime_1man=int(dotime_1man)
    #도착하는데 걸리는 시간과 심사하는데 걸리는 시간을 분리해서 큐에 enqueue
    cometime_queue.enqueue(cometime_1man)
    dotime_queue.enqueue(dotime_1man)
    

cometime=Queue()    #도착하는데 걸리는 시간보다는 첫사람이 오고 난 후 흐르는 시간으로 계산을 편리하게 하려고 만든 큐
cal_cometime=0
cal_endtime=0
for i in range (cometime_queue.size):
    cal_cometime+= cometime_queue.dequeue()
    
    cometime.enqueue(cal_cometime)
    
cometime.dequeue()  #1번사람이 오는데 걸리는 시간은 대기시간에서 무의미하므로 미리 빼냄
wait_1man=0 #한사람당 대기시간
sum_waittime=0  #대기시간 합
endtime=0   #이전사람이 끝나는 시간
for i in range(cometime.size):  #반복문으로 모든사람이 심사대로 가는 알고리즘
    endtime+=dotime_queue.dequeue()
    wait_1man=endtime - cometime.dequeue()
    if wait_1man<0: #도착했을 때 심사대가 비어있는 경우의 계산
        endtime-=wait_1man
        wait_1man=0
    sum_waittime+=wait_1man
result=sum_waittime/people

def my_round(a):    #파이썬의 반올림은 우리가 보통 알고있는 반올림과 다르기 때문에 직접 구현
    a=math.trunc(a*1000)
    a=a/1000
    b=a
    b=math.trunc(b*100)
    b=b/100
    
    if a-b<0.005:
        return b
    else:
        return b+0.01

result=my_round(result)
print("%.2f" %result) 

    

