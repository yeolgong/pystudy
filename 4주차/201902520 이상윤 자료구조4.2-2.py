import math     #나중에 반올림 계산을 위함

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
        if self.size== len(self.items):
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
        olditems=self.items
        self.items=[None]*cap
        walk=self.front
        for i in range(self.size):
            self.items[i]=olditems[walk]
            walk=(walk+1)% len(olditems)
        self.front=-1
        self.rear=self.size-1
  
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

come_nowtime=Queue() #도착하는데 걸리는 시간보다는 첫사람이 오고 난 후 흐르는 시간으로 계산을 편리하게 하려고 만든 큐
cal_cometime=0
for i in range(cometime_queue.size):
    cal_cometime += cometime_queue.dequeue()
    come_nowtime.enqueue(cal_cometime)
 
    
  
d1_cometime_queue=Queue() #1번심사대 인원정보를 관리하는 큐 각각 온 시간과 심사시간
d1_dotime_queue=Queue()
d2_cometime_queue=Queue() #2번심사대 인원정보를 관리하는 큐 각각 온 시간과 심사시간
d2_dotime_queue=Queue()

end_d1=0    #대기시간이 적은 심사대로 가기위해 앞사람이 심사를 끝내는 시간을 저장하는 변수
end_d2=0

e1=come_nowtime.dequeue()   #첫사람은 1번심사대로 가는 알고리즘
d1_cometime_queue.enqueue(e1)
f1=dotime_queue.dequeue()
d1_dotime_queue.enqueue(f1)
f2=0    
end_d1=f1
while (come_nowtime.isEmpty()==False):  #반복문으로 대기인원이 모두 대기시간이 적은 심사대로 가는 알고리즘

    if end_d1 <= end_d2:    #1번심사대의 마지막 사람이 2번심사대 마지막 사람보다 빨리 끝나거나 같이 끝날경우 다음사람을 1번 심사대로 보냄
        e1=come_nowtime.dequeue()       #1번심사대 관련 큐에 정보 enqueue
        d1_cometime_queue.enqueue(e1)
        if (end_d1-e1<0): #대기없이 입장할 경우
            f1=dotime_queue.dequeue()
            d1_dotime_queue.enqueue(f1)
            end_d1=e1+f1
        else:   #대기하고 입장할 경우
            f1=dotime_queue.dequeue()
            d1_dotime_queue.enqueue(f1)
            end_d1+= f1
      
    else:   #2번심사대가 먼저 빠지는 경우
        e2=come_nowtime.dequeue()
        d2_cometime_queue.enqueue(e2)
        if (end_d2-e2<0):   #대기없이 입장할 경우
            f2=dotime_queue.dequeue()
            d2_dotime_queue.enqueue(f2)
            end_d2=e2+f2
        else:   #대기하고 입장할 경우
            f2=dotime_queue.dequeue()
            d2_dotime_queue.enqueue(f2)
            end_d2+= f2

sum_waittime=0

endtime1=d1_cometime_queue.dequeue()
endtime2=d2_cometime_queue.dequeue()
for i in range(d1_cometime_queue.size):    #1번심사대에서의 개인마다 대기시간 계산
    endtime1+=d1_dotime_queue.dequeue()
    d1_waittime=endtime1 - d1_cometime_queue.dequeue() 
    if d1_waittime<0:   #도착했을 때 심사대가 비어있는 경우의 계산
        endtime1-=d1_waittime
        d1_waittime=0 
    #print(d1_waittime)
    sum_waittime+= d1_waittime   
    
for i in range(d2_cometime_queue.size):    #2번심사대에서의 개인마다 대기시간 계산
    endtime2+=d2_dotime_queue.dequeue()
    d2_waittime=endtime2 - d2_cometime_queue.dequeue() 
    if d2_waittime<0:  #도착했을 때 심사대가 비어있는 경우의 계산
        endtime2-=d2_waittime     
        d2_waittime=0
    #print(d2_waittime)
    sum_waittime+= d2_waittime   
       
result=sum_waittime/people


def my_round(a):        #파이썬의 반올림은 우리가 보통 알고있는 반올림과 다르기 때문에 직접 구현
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


