class Stack:                           # 스택 클래스 구현
    def __init__(self):
        self.items = []                # 리스트 초기화

    def isEmpty(self):
        return len(self.items) == 0    # 리스트 길이가 0이면 True

    def clear(self):
        self.items = []

    def push(self, e):
        self.items.append(e)           # 스택 push 구현 

    def pop(self):                     # 스택 pop 구현
        if not self.isEmpty():
            return self.items.pop()

    def size(self):
        return len(self.items)


def A(string_list):
    s = Stack()
    idx_list = []
    op = '({['
    cp = ')}]'
    idx = 0
    for x in range(len(string_list)):
        idx = 0
        line = 1+x
        for ch in string_list[x]:
            idx +=1                           # 반복할때마다 인덱스 +1
            if ch in op:                      # 여는 괄호일때 스택에 push
                s.push(ch)
                idx_list.append(idx)          # 처음으로 짝을 찾지 못한 괄호의 인덱스를 저장하기 위한 리스트 생성
            elif ch in cp:                    # 닫는 괄호일때
                if s.isEmpty():               # 스택이 비었다면
                    if ch == ')':
                        print("error 1: ) at position", idx, "in line", line)   # 괄호에 맞게 인덱스와 에러 출력
                        return False
                    elif ch == '}':
                        print("error 2: } at position", idx, "in line", line) 
                        return False
                    elif ch == ']':
                        print("error 3: ] at position", idx, "in line", line) 
                        return False
                     
                else:                                # 스택에 원소가 있다면
                    oc = s.pop()                     # oc는 스택에서 꺼낸 괄호
                                       # 짝이 있다면 인덱스 리스트 pop
                
                    if (ch == ')' and oc != '('):    # 상황에 맞게 에러 출력
                        print("error 1: ) at position", idx, "in line", line) 
                        return False
                    elif (ch == ']' and oc != '['):
                        print("error 3: ] at position", idx, "in line", line) 
                        return False
                    elif (ch == '}' and oc != '{'):
                        print("error 2: } at position", idx, "in line", line) 
                        return False
                
    if not s.isEmpty():                          # 스택에 남은 괄호가 있으면
        if s.items[len(s.items)-1] == '(':                    # 처음으로 발견되는 괄호가 필요하므로 인덱스 0
            print("error 4: ( at position", idx_list[len(idx_list)-1], "in line", line)         # 각 상황에 맞게 에러 출력
            return False
        
        elif s.items[len(s.items)-1] == '{':
            print("error 5: { at position", idx_list[len(idx_list)-1], "in line", line) 
            return False
        
        elif s.items[len(s.items)-1] == '[':
            print("error 6: [ at position", idx_list[len(idx_list)-1], "in line", line) 
            return False
    else :
        print(1)
        return True


import sys

str_list = []
while True:
    str = sys.stdin.readline().rstrip()
    if str == '':
        break
    else:
        str_list.append(str)
A(str_list)