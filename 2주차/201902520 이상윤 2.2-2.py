#정답과 배점이 주어질때, 제출한답안지(id,답)을 입력받고 최고성적 출력하는 프로그램
getscore=[]     #획득점수와,가장높은 점수를 받은 id를 저장하기 위해 빈 list생성
maxscoreid=[]
maxscore=0

answers=input().split()
answerslen=len(answers)
for i in range(answerslen): #정답을 정수형으로 바꿔줌
    answers[i]=int(answers[i])

points=input().split()
pointslen=len(points)
for i in range(pointslen):  #배점을 정수형으로 바꿔줌
    points[i]=int(points[i])
    
people=int(input()) 


list=[[int(i) for i in input().split()]for j in range(people)]
#인원을 입력받아 인원만큼 루프를 돌면서 답안지를 입력받아 2차원 리스트에 저장

for i in range(people): #정답과 답안지가 일치하면 점수획득
    score=0 #점수를 0으로 초기화
    for j in range(answerslen):
        if answers[j]==list[i][j+1]:
            score=score+points[j]
    getscore.append(score) #getscore 리스트에 획득점수 저장

for i in range(len(getscore)):  #획득점수가 최고점수보다 높으면 최고점수 변경
    if getscore[i]>maxscore:
        maxscore=getscore[i]
        
for i in range(len(getscore)): #최고점수와 획득점수가 같은 사람의 id를 maxscoreid 리스트에 저장
    if getscore[i]==maxscore:
        maxscoreid.append(list[i][0])


print("%d" %(maxscore)) #최고점수를 출력
'''
maxscoreid.sort()
for i in range(len(maxscoreid)):
    print(maxscoreid[i], end=' ')
'''


#list.append(int(x) for x in input().split())
'''
stuanswer=input().split()
    stuanswerlen=len(stuanswer)
    for i in range(stuanswerlen):
        stuanswer[i]=int(stuanswer[i])
    
for i in range(people):
    score=0
    for j in range(answers):
        if answers[i]== stuanswer[i+1]:
            score=score+points[j]
        getscore.append(score)


for i in range(getscore):
    if getscore[i]>maxscore:
        maxscore=getscore[i]

for i in range(getscore):
    if getscore==maxscore:
        maxscoreid.append()    
'''