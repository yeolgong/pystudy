
from platform import node


class Student:
    def __init__(self,number,name,major,grade,score=''):
        self.stu_number=number
        self.stu_name=name
        self.stu_major=major
        self.stu_grade=grade
        self.stu_score=score

class TNode:
    def __init__(self,key,value,left=None,right=None):
        stu=Student(Student.stu_number,Student.stu_name,Student.stu_major,Student.stu_grade,Student.stu_score)
        self.key=key
        self.value=value
        self.left=left
        self.right=right

class Course:
    def __init__(self):
        self.root=None

    def insert(self,key,value):#1
        self.root=self.insertsubtree(self.root,key,value)
    def insertsubtree(self,node,key,value):
        if node==None:
            return TNode(key,value)
        elif key<node.key:
            node.left=self.insertsubtree(node.left,key,value)
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
        self.root=self.deletestubree(self.root,key)
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
            #return node




    def new(self,number,name,major,grade):#1
        stu=Student(number,name,major,grade)
        TNode(stu.stu_number,stu)
        if self.search(number) is None:
            self.insert(name,stu)
        else:
            print('error1')

    def grade(self,number,score):#2
        node=self.search(number)
        node.value.score=score

    def cancel(self,number)






