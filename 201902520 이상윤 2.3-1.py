#문자열이 회문이면 yes를 출력하고 아니면 no를 출력하는 프로그램(대소문자 구별x)

string=input()  #문자열 입력받음

realstring=string.lower()   #모든문자를 소문자로 변경(대소문자 구별없기때문)

palindrome=True     #기존문자의 앞에서부터와 뒤에서부터 한글자식 비교
for i in range(len(realstring)//2):
    if realstring[i]!=realstring[-1-i]:
        palindrome=False
        break
    
if palindrome==True:
    print("yes")
else:
    print("no")