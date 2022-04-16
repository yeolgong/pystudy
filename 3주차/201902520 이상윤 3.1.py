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
    
    
    for ch in string:
        if ch in openPa:        #여는 괄호는 스택에 push
           par.push(ch)
        elif ch in closePa:    
            if par.isEmpty():    #닫는 괄호가 있는데 여는괄호가 앞에 없으면 0리턴
                return 0
            else:       #여는괄호가 있지만 닫는괄호가 여는괄호와 매칭이 되지 않는다면 0리턴
                opench=par.pop()
                if ( ch==')' and opench !='(' ) or ( ch=='}' and opench !='{' ) \
                    or ( ch==']' and opench !='[' ):
                    return 0
                
    if par.isEmpty():      #남아있는 여는괄호가 있는지 검사 스택이 비어있지 않으면 짝이 맞지 
                           #않으므로 0리턴
        return 1
    else:
        return 0

print(parentheses_bal(str))       
    
