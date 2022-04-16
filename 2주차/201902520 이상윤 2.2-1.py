#정답과 배점이 주어지고 제출한 답안지의 점수를 계산하는 프로그램

score=0


answers=input().split()
answerslen=len(answers)         
for i in range(answerslen):     #입력한 정답을 정수형으로 바꿔줌
    answers[i]=int(answers[i])

points=input().split()
pointslen=len(points)  
for i in range(pointslen):      #입력한 배점을 정수형으로 바꿔줌
    points[i]=int(points[i])
    
myanswers=input().split()
myanswerslen=len(myanswers)
for i in range(myanswerslen):       #입력한 답안지를 정수형으로 바꿔줌
    myanswers[i]=int(myanswers[i])
    
for i in range(answerslen):
    if myanswers[i]==answers[i]:  #정답과 답안지가 일치하면 배점을 점수에 더함
        score=score+points[i]

        
print("%d" %(score))
        