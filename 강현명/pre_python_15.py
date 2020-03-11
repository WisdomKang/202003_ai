"""15. 주민등록번호를 입력하면 남자인지 여자인지 알려주는 프로그램을 작성하시오. 
(리스트 split 과 슬라이싱 활용) """
 

id_num = input("주민번호를 입력하세요.")

gender_num = id_num.split("-")[1][0]

print( gender_num)


if gender_num == '1' or gender_num == '3':
    print("you ara man")
elif gender_num == '2' or gender_num =='4' :
    print("you ara woman")
else:
    print("who ara you?")