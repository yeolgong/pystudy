
class Stack:        #stack을 사용하기 위한 클래스  구현
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return len(self.items)==0
    def pop(self):
        try:
            return self.items.pop()
        except SyntaxError:
            print("stack is empty")
    def push(self, item):
        self.items.append(item)

str=input()

def parentheses_bal(string):
    par= Stack()
    openPa="([{"
    closePa=")]}" 
    index=Stack()

    for i in range(len(string)):
        if string[i] in openPa:     #여는괄호는 스택에 push
            par.push(string[i])
            index.push(i)           #오류위치를 나중에 출력하기 위해 index스택에 index값 push
        elif string[i] in closePa:
            if par.isEmpty():       #닫는괄호가 나왔는데 앞에 여는괄호가 없으면 괄호 모양에 따른 에러 발생
                if string[i]==')':
                    return i, "error1 "
                if string[i]=='}':
                    return i, "error2"
                if string[i]==']':
                    return i, "error3"
            else:       #닫는괄호가 있고 앞에 여는괄호가 있지만 모양이 다른경우 닫는괄호의 모양에 따른 에러발생
                opench=par.pop()
                index.pop()
                if ( string[i]==')' and opench !='(' ):
                    return i, "error1"
                if ( string[i]=='}' and opench !='{' ):
                    return i, "error2"
                if ( string[i]==']' and opench !='[' ):
                    return i, "error3"
    if par.isEmpty():               #남아있는 여는괄호가 있는지 검사 스택이 비었으면 짝이 맞음
        i=1
        return i, ""
    else:     #여는괄호가 남아있으면 그에 맞는 닫는괄호가 없으므로 여는괄호의 모양에 따라 에러발생.
#스택에서 제일 나중에 들어온 여는괄호가 먼저 닫혀야 하는데 닫는괄호가 없으니 첫 오류로 판단하고 해당 index값 pop
        i=index.pop()
        p=par.pop()
        if p=='(':
            return i,"error4"
        elif p=='{':
            return i, "error5" 
        elif p=='[':
            return i,"error6"
        
           
num, error=parentheses_bal(str) #출력값이 (a,b)이런식으로 나오므로 괄호빼기위한 출력방식
print(num,error)      
