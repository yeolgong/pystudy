class Student:
    def __init__(self,number,name):
        self.stu_num=number
        self.stu_name=name

class Course:
    def __init__(self):
        self.stu_list=[]

    def new(self,number,name):
        stu=Student(number,name)
        self.stu_list.append(stu.stu_num+' '+stu.stu_name)

    def cancel(self,number):
        for i in range(len(self.stu_list)):
            innumber,inname=self.stu_list[i].split()
            if innumber==number:
                index=i
                break
        del self.stu_list[index]

    def rshow(self,number):
        for i in range(len(self.stu_list)):
            innumber,inname=self.stu_list[i].split()
            if innumber==number:
                print(self.stu_list[i])
                break

    def print(self):
        self.stu_list.sort()
        print(len(self.stu_list))
        for i in self.stu_list:
            print(i)
'''
    def quit(self):
        exit()
'''
soogang=Course()
while True:
    command=input()

    if command[0]=='N':
        do,number,name=command.split()
        soogang.new(number,name)
    elif command[0]=='C':
        do,number=command.split()
        soogang.cancel(number)
    elif command[0]=='R':
        do,number=command.split()
        soogang.rshow(number)
    elif command[0]=='P':
        soogang.print()
    elif command[0]=='Q':
        break
