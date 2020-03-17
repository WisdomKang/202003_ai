"""6. 아래와 같이 별이 찍히게 출력하시오.
숫자를 입력하세요 : 5
    ★
   ★★
  ★★★
 ★★★★
★★★★★
 ★★★★
  ★★★
   ★★
    ★
"""


N = int( input("숫자를 입력하세요:"))

space = N - 1

str_list = []
for i in range(N):
    star_str = ""
    for j in range(N):
        if j < space:
            star_str += " "
        else:
            star_str += "★"
    
    str_list.append(star_str)
    space -= 1


print( str_list )

for i in range(N):
    print(str_list[i])

for i in range(N-2, -1 , -1):
    print(str_list[i])