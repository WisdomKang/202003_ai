"""5. N을 입력 받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오(format 활용)"""

N = int( input("단수를 입력하세요."))

for i in range(1,10):
    print( "{0} X {1} = {2}".format(N, i , N*i))