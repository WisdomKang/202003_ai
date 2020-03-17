'''
2.
년, 월, 일을 입력하면 그 날이 무슨 요일인지 출력하는 함수를 만드세요.


테스트코드
<입력>
print("%d년 %d월 %d일은 %s 입니다." % (myYear, myMonth, myDay, printDayOfTheWeek(myYear, myMonth, myDay)))

<출력>
연도를 입력하시오 : 2020
월을 입력하시오 : 3
일을 입력하시오 : 13
2020년 3월 13일은 금요일 입니다.

'''

import datetime

year = int( input("년도를 입력하세요."))
month = int( input("달을 입력하세요."))
day= int( input("날짜를 입력하세요."))

week_num = datetime.date(year, month, day).isocalendar()[2]

week_text = ""

if week_num == 1: week_text="월"
elif week_num == 2: week_text="화"
elif week_num == 3: week_text="수"
elif week_num == 4: week_text="목"
elif week_num == 5: week_text="금"
elif week_num == 6: week_text="토"
elif week_num == 7: week_text="일"

print( week_text )