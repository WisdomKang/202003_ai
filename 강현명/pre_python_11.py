"""11. 최대공약수를 구하는 함수를 구현하시오"""

num_1 = int( input("첫번쨰 수"))
num_2 = int( input("두번째 수"))

def GCD(num1 , num2):
    min = num1 if num1 > num2 else num2
    gcd = 0
    for i in range(1, min):
        print(i)
        if (num1 % i) == 0 and (num2 % i) == 0:
            print(i)
            if gcd < i: gcd=i
            
    return gcd


print( "최대공약수는:",GCD(num_1, num_2))