""""2.if문을 이용해 첫번째와 두번 수, 연산기호를 입력하게 하여 계산값이 나오는 계산기를 만드시오"""

num_1 = int(input())
num_2 = int(input())

symbol = input()

output = 0

if symbol == "+":
    output = num_1+ num_2
elif symbol == "-":
    output = num_1 - num_2
elif symbol == "*":
    output = num_1 * num_2
elif symbol == "/":
    output = num_1 / num_2
else:
    print("Error : wrong symbol?")

print( output )
