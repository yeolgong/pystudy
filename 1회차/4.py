year1,year2=input().split()
year1,year2=int(year1),int(year2)
day=input()
days=0
for i in range(0,year2-year1):		#윤년구하는 알고리즘 윤년은 1년이 366일이다
	if (year1+i)%400 ==0:
		days=days+366
	elif (year1+i)%100 ==0:
		days=days+365
	elif (year1+i)%4 ==0:
		days=days+366
	else:
		days=days+365
#print(days)
if day=="일":				#입력받은 요일을 일요일 기준으로 0~6분류
	standard=0
elif day=="월":
	standard=1
elif day=="화":
	standard=2
elif day=="수":
	standard=3
elif day=="목":
	standard=4
elif day=="금":
	standard=5
elif day=="토":
	standard=6
remain=(days+standard)%7

#print("%d %d"%(standard,remain))
if remain==0:			#입력받은 요일과 총날짜를 더하여 7로나누고 나머지로 요일결정
	print("일")
elif remain==1:
	print("월")
elif remain==2:
	print("화")
elif remain==3:
	print("수")
elif remain==4:
	print("목")
elif remain==5:
	print("금")
elif remain==6:
	print("토")
