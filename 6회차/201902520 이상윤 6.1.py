class Student:
    def __init__(self,number,name):
        self.stu_num=number
        self.stu_name=name

class Course:
    def __init__(self):
        self.stu_list=[]

    def resister(self,number,name):
        Student(number,name)
        
        
