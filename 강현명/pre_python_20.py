"""20. 1부터 100까지 369 게임을 하려고 한다.
3,6,9가 들어가는 부분에는 '짝' 을 출력하고, 
5의 배수에는 '아자' 를 출력,
그외에는 수를 출력하는 프로그램을 만드시오."""


for i in range(1, 101):
    num_str = str(i)
    if num_str.find('3') != -1 or num_str.find('9') != -1 or num_str.find('6') != -1 :
        print("짝", end="\t")
    elif (i % 5) == 0:
        print("아자", end="\t")
    else:
        print(i, end="\t")

    if i % 10 == 0 :
        print()
