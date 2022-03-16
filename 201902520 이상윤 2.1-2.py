#입력받은 수보다 작거나 같은 완전수 개수 구하는 문제
a=int(input())		
count=0

for i in range(1,a+1):
    num=0
    pnum=False
    for j in range(1,i//2+1):    #i를 j로나눠 나머지가 0이면 약수고 약수를 더함
        if i % j==0:            #테스트케이스중 타임아웃인 문제가 있어 자신의 절반까지만 계산
            num=num+j
    if num==i:
        pnum=True
    if pnum is True:    
        count=count+1

print("%d" %(count))

