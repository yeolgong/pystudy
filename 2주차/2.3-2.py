#문자열의 가장 긴 회문을 사전순서대로 출력하는 프로그램(대소문자 구별x)

string=input()

realstring=string.lower()
realstring=realstring.replace(" ","")
realstring=realstring.strip()#입력받은 문자열을 소문자로 변환
restring=realstring[::-1]   #비교를 위해 문자열을 뒤집어서 하나 만듬

pal=[]      #부분 회문을 저장하게위해 만듬
lenth=len(realstring)

        

for i in range(len(realstring)):  #부분부분을 비교해야하므로 for문 2개사용 예) list[i:j]
    for j in range(i+1,len(realstring)+1):
        palindrome=False
    #a    print(realstring[i:j+1])
        #print(restring[lenth-j:lenth-i])
        if realstring[i:j]==restring[lenth-j:lenth-i]:#부분이 일치한지 뒤집어본거랑 비교
            palindrome=True
        if palindrome:
            pal.append(realstring[i:j]) #일치할경우 리스트에 추가
#print(pal)

longpallen=0           
for i in range(len(pal)):   #리스트중 길이가 가장 긴 회문길이 찾기
    if len(pal[i])>longpallen:
        longpallen=len(pal[i])
        
answer=[]        
for i in range(len(pal)):   #길이가 가장 긴 회문을 answer리스트에 삽입
    if len(pal[i])==longpallen:
        answer.append(pal[i])
panswer=[]          # 중복검사. 새 리스트에 같은값이 없을경우 append함으로써 중복제거
for i in answer:
    if i not in panswer:
        panswer.append(i)
panswer.sort()   #사전순으로 정렬

for i in range(len(panswer)):        
    print("%s" %(panswer[i]) , end=' ')  #답을 한줄로 출력