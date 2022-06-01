
class Student:  #학생정보
    def __init__(self,number,name,major,grade,score=''):
        self.stu_number=number  #학번
        self.stu_name=name      #이름
        self.stu_major=major    #학과
        self.stu_grade=grade    #학년
        self.stu_score=score    #점수

class TNode:    #이진트리 학생정보 저장하는 노드 
    def __init__(self,key,value,left=None,right=None):
        self.key=key
        self.value=value
        self.left=left
        self.right=right

class Course:
    def __init__(self):
        self.root=None
        self.printlist=[]


    def insert(self,key,value): #수강신청을 위한 이진트리 삽입연산
        self.root=self.insertsubtree(self.root,key,value)
    def insertsubtree(self,node,key,value):
        if node==None:
            return TNode(key,value)
        elif key<node.key:      #왼쪽 부트리에 노드 삽입
            node.left=self.insertsubtree(node.left,key,value)
        elif key>node.key:      #오른쪽 부트리에 노드 삽입
            node.right=self.insertsubtree(node.right,key,value)
        else:
            pass
        return node

    def search(self,key):#key 값으로 이진트리 탐색연산(입력받은 키값의 node반환)
        node=self.root
        while node is not None:
            if key==node.key:
                return node
            elif key<node.key:
                node=node.left
            else:
                node=node.right
        return None
    
    #삭제연산
    def minnode(self,node): #최소키 노드 반환(삭제연산에 이용)
        if node.left==None:
            return node
        else:
            return self.minnode(node.left)
    def delete(self,key):#3
        self.root=self.deletesubtree(self.root,key)
    def deletesubtree(self,node,key):
        if node==None:
            return None
        if key<node.key:    #삭제할 키의 노드가 node의 왼쪽 부트리인 경우
            node.left=self.deletesubtree(node.left,key)
            return node
        elif key>node.key:  #삭제할 키의 노드가 node의 오른쪽 부트리인 경우
            node.right=self.deletesubtree(node.right,key)
            return node
        else:               #node가 삭제할 키의 노드의 경우
            if node.right==None:#node의 오른쪽 자식노드가 없는 경우
                return node.left
            if node.left==None:#node의 왼쪽 자식노드가 없는 경우
                return node.right
            rightminnode=self.minnode(node.right) # node의 오른쪽 부트리에서 최소키의 노드를 찾음
            node.key=rightminnode.key #node의 오른쪽 부트리에서 최소키의 노드를 복사 node에 복사
            node.value=rightminnode.value
            node.right=self.deletesubtree(node.right,rightminnode.key)# node의 오른쪽 부트리에서 최소키의 노드를 삭제
            return node

    def inorder(self):  #중위순회. key값을 가장 작은 순서(오름차순)부터 출력하기 위해 사용
        self.printlist=[]
        self.subtreeinorder(self.root)
    def subtreeinorder(self,p):
        if p is not None:
            self.subtreeinorder(p.left)
            self.printlist.append(p)
            self.subtreeinorder(p.right)
            


    def new(self,number,name,major,grade): #수강신청, key값에 학번, value값은 Student클래스를 저장
        stu=Student(number,name,major,grade)
        if self.search(number) is None:
            self.insert(number,stu)
        else:
            print('error1')

    def scorein(self,number,score): #입력받은 학번의 학생 점수 설정. 학생이 이미 있으면 error1
        node=self.search(number)
        if node is not None:
            node.value.stu_score=score
        else:
            print('error2')

    def cancel(self,number):    #입력받은 학번의 학생 수강 취소. 학생이 없으면 error2
        if self.search(number) is not None:
            self.delete(number)
        else:
            print('error2')
    
    def rshow(self,number): #입력받은 학번의 학생 조회. 학생이 없으면 error2
        if self.search(number) is not None:
            node=self.search(number)
            print(node.value.stu_number,node.value.stu_name,node.value.stu_major,node.value.stu_grade,node.value.stu_score)
        else:
            print('error2')


    def majorshow(self,major):  #입력받은 학과의 학생수와 정보를 오름차순으로 출력
        self.inorder()
        result=[]   #그냥 value를 출력하면 원하는 값이 나오지 않아서 쉽겨 출력하기 위해 출력용 리스트 생성했습니다
        for i in range(len(self.printlist)):    #중위순회하면서 입력받은 학과와 같은지 탐색
            if self.printlist[i].value.stu_major==major:
                node=self.printlist[i]
                result.append(node)
        print(len(result))
        for i in range(len(result)):
            node=result[i]
            print(node.value.stu_number,node.value.stu_name,node.value.stu_major,node.value.stu_grade,node.value.stu_score)
    
    def printout(self): #수강생의 수와 정보를 오름차순으로 출력
        self.inorder()
        print(len(self.printlist))
        for i in range(len(self.printlist)):
            node=self.printlist[i]
            print(node.value.stu_number,node.value.stu_name,node.value.stu_major,node.value.stu_grade,node.value.stu_score)
    

stuadmin=Course()
while True:
    command=input()
    if command[0]=='N':
        do,number,name,major,grade=command.split()
        stuadmin.new(number,name,major,grade)
    elif command[0]=='G':
        do,number,score=command.split()
        stuadmin.scorein(number,score)
    elif command[0]=='C':
        do,number=command.split()
        stuadmin.cancel(number)
    elif command[0]=='R':
        do,number=command.split()
        stuadmin.rshow(number)
    elif command[0]=='D':
        do,major=command.split()
        stuadmin.majorshow(major)
    elif command[0]=='P':
        stuadmin.printout()
    elif command[0]=='Q':
        break

