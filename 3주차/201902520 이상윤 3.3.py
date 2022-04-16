import sys
class Stack:        #stack을 사용하기 위한 클래스 구현
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
sen=sys.stdin.readlines()          #입력받을 여러줄의 문장 list생성
'''while(1):       #몇줄 받을지 모르기 때문에 입력값이 아무것도 없을때까지 입력받아 list에 append
    str=sys.stdin.readline()	#sys.stdin.readline()메소드를 사용하면 실행시간을 줄일 수 있다
    if str=='':
        break
    sen.append(str)
'''
def parentheses_bal(list):
    par=Stack()
    openPa='({['
    closePa=')}]'
    line=Stack()
    raw=Stack()
    
    for i in range(len(list)):      #i번째줄 문장의 j번째 단어가 여는괄호면 par스택에 push 
        for j in range(len(list[i])):
            if list[i][j] in openPa:
                par.push(list[i][j])
                line.push(i)        #오류위치를 출력하기 위해서 줄과 몇번째 글자인지 각각 line, raw스택에 push
                raw.push(j)
            elif list[i][j] in closePa: #닫는괄호가 나왔지만 앞에 여는 괄호가 없는경우 
                                        #닫는괄호의 모양에따라 error출력
                if par.isEmpty():
                    if list[i][j]==')':
                        return 'error 1: ) at position',j+1, 'in line', i+1
                    if list[i][j]=='}':
                        return 'error 2: } at position',j+1, 'in line', i+1
                    if list[i][j]==']':
                        return 'error 3: ] at position',j+1, 'in line', i+1
                else:       #닫는괄호와 최근 여는괄호의 짝이 맞지않을 떄 닫는괄호의 모양에 따른 error 출력
                    opench=par.pop()
                    l=line.pop()
                    r=raw.pop()
                    if ( list[i][j] == ')' and opench !='('):
                        return 'error 1: ) at position',j+1, 'in line', i+1 
                    if ( list[i][j] == '}' and opench !='{'):
                        return 'error 2: } at position',j+1, 'in line', i+1
                    if ( list[i][j] == ']' and opench !='['):
                        return 'error 3: ] at position',j+1, 'in line', i+1
    if par.isEmpty():     #짝이 맞을경우 1출력
        return 1,'','',''
    else:       #닫는괄호가 더이상 나오지 않는경우 남은 여는괄호중 가장 최근에 들어온 
                #여는괄호가 젤 먼저 닫히지 않는 에러 발생하므로 line, raw 여는괄호모양 pop해서 출력
        l=line.pop()
        r=raw.pop()
        p=par.pop()
        if p=='(':
            return 'error 4: ( at position', r+1, 'in line', l+1
        elif p=='{':
            return 'error 5: { at position', r+1, 'in line', l+1
        elif p=='[':
            return 'error 6: [ at position', r+1, 'in line', l+1

error, raw, inline, line=parentheses_bal(sen)
print(error,raw,inline,line)
