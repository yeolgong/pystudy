import sys
class Node:     #Node 구현
    def __init__(self,element):
        self.data=element
        self.link=None
        
class LinkedStack:  #Linkedstack 구현
    def __init__(self):
        self.top=None
        
    def isEmpty(self):
        return self.top==None   
    
    def push(self,e):
        newNode=Node(e)
        newNode.link=self.top
        self.top=newNode
        
    def pop(self):
        if(self.isEmpty()):
            print("Stack is empty")
            return
        e=self.top.data
        self.top=self.top.link
        return e

def Postfix_cal(question):  #후위표기 수식 계산 알고리즘
    stack=LinkedStack()
    operator=('+','-','*','/','//','%') #연산자 구분
    for i in range(len(question)):
        str=question[i]
        if str in operator: #값이 연산자일 경우
            if i==0:   #첫번째로 연산자가 나올경우 error출력
                print ('error')
                return
            if stack.isEmpty(): #연산자가 있지만 피연산자가 없는 경우 error출력
                print("error")
                return
            else:   #그 외의 경우 val2 pop
                val2=stack.pop()
            
            if stack.isEmpty(): #또 다른(2번째) 피연산자가 없는 경우 error출력
                print("error")
                return
            else:   #아니면 val1 pop
                val1=stack.pop()
            if str=='+': stack.push(val1+val2)      #연산자와 알맞는 연산
            elif str=='-': stack.push(val1-val2)
            elif str=='*': stack.push(val1*val2)
            elif str=='/': stack.push(val1/val2)
            elif str=='//': stack.push(val1//val2)
            elif str=='%': stack.push(val1%val2)
        elif str==';':          
            result=stack.pop()  #';'을 만난경우 결과 pop
            if stack.isEmpty(): # 방금 pop한 경우가 stack의 마지막 값일 경우 진짜 답
                print("%.0f" %result)
                return 
            else: #다른 값이 더 있을 경우 error 출력
                print("error") 
                return
        else:   #연산자가 아닌 피연산자는 stack에 push
            stack.push(float(str))
        
solution=sys.stdin.readline().split()   #후위 표기 수식 입력받음
Postfix_cal(solution) 