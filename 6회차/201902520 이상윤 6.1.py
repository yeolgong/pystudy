class Student:
    def __init__(self,number,name):
        self.stu_num=number #학번
        self.stu_name=name  #이름

class Course:
    def __init__(self): #학생을 관리하는 리스트 생성
        self.stu_list=[]

#명령어들
    def new(self,number,name):  #입력받은 학번의 학생이 수강 신청
        stu=Student(number,name)
        self.stu_list.append(stu.stu_num+' '+stu.stu_name)

    def cancel(self,number):    #입력받은 학번의 학생이 수강 취소
        for i in range(len(self.stu_list)):
            innumber,inname=self.stu_list[i].split()
            if innumber==number:
                index=i
                break
        del self.stu_list[index]

    def rshow(self,number): #입력받은 학번의 학생의 정보를 출력
        for i in range(len(self.stu_list)):
            innumber,inname=self.stu_list[i].split()
            if innumber==number:
                print(self.stu_list[i])
                break

    def print(self):    #수강생들의 수와 학생들의 정보 출력(학번 오름차순)
        self.stu_list.sort()
        print(len(self.stu_list))
        for i in self.stu_list:
            print(i)

soogang=Course()
while True:         #명령어에 따른 기능 실행
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
