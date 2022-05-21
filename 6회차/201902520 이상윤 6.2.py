

class Student:
    def __init__(self,number,name,major,grade,score=''):
        self.stu_number=number
        self.stu_name=name
        self.stu_major=major
        self.stu_grade=grade
        self.stu_score=score

class TNode:
    def __init__(self,key,value,left=None,right=None):
        self.key=key
        self.value=value
        self.left=left
        self.right=right

class Course:
    def __init__(self):
        self.root=None
        self.printlist=[]


    def insert(self,key,value):#1
        self.root=self.insertsubtree(self.root,key,value)
    def insertsubtree(self,node,key,value):
        if node==None:
            return TNode(key,value)
        elif key<node.key:
            node.left=self.insertsubtree(node.left,key,value)
        elif key>node.key:
            node.right=self.insertsubtree(node.right,key,value)
        else:
            pass
        return node

    def search(self,key):#1,2
        node=self.root
        while node is not None:
            if key==node.key:
                return node
            elif key<node.key:
                node=node.left
            else:
                node=node.right
        return None

    def minnode(self,node):
        if node.left==None:
            return node
        else:
            return self.minnode(node.left)
    def delete(self,key):#3
        self.root=self.deletesubtree(self.root,key)
    def deletesubtree(self,node,key):
        if node==None:
            return None
        if key<node.key:
            node.left=self.deletesubtree(node.left,key)
            return node
        elif key>node.key:
            node.right=self.deletesubtree(node.right,key)
            return node
        else:
            if node.right==None:
                return node.left
            if node.left==None:
                return node.right
            rightminnode=self.minnode(node.right)
            node.key=rightminnode.key
            node.value=rightminnode.value
            node.right=self.deletesubtree(node.right,rightminnode.key)
            return node

    def inorder(self):
        self.printlist=[]
        self.subtreeinorder(self.root)
    def subtreeinorder(self,p):
        if p is not None:
            self.subtreeinorder(p.left)
            self.printlist.append(p)
            self.subtreeinorder(p.right)
            


    def new(self,number,name,major,grade):#1
        stu=Student(number,name,major,grade)
        if self.search(number) is None:
            self.insert(number,stu)
        else:
            print('error1')

    def scorein(self,number,score):#2
        node=self.search(number)
        if node is not None:
            node.value.stu_score=score
        else:
            print('error2')

    def cancel(self,number):
        if self.search(number) is not None:
            self.delete(number)
        else:
            print('error2')
    
    def rshow(self,number):
        if self.search(number) is not None:
            node=self.search(number)
            print(node.value.stu_number+' '+node.value.stu_name+' '+node.value.stu_major+' '+node.value.stu_grade+' '+node.value.stu_score)
        else:
            print('error2')


    def majorshow(self,major):
        self.inorder()
        result=[]
        for i in range(len(self.printlist)):
            if self.printlist[i].value.stu_major==major:
                node=self.printlist[i]
                result.append(node)
        print(len(result))
        for i in range(len(result)):
            node=result[i]
            print(node.value.stu_number+' '+node.value.stu_name+' '+node.value.stu_major+' '+node.value.stu_grade+' '+node.value.stu_score)
    
    def printout(self):
        self.inorder()
        print(len(self.printlist))
        for i in range(len(self.printlist)):
            node=self.printlist[i]
            print(node.value.stu_number+' '+node.value.stu_name+' '+node.value.stu_major+' '+node.value.stu_grade+' '+node.value.stu_score)
    

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

