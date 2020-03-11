"""10. 팩토리얼을 구하는 함수를 작성하시오.
ex ) 5! = 5x4x3x2x1
  print(factoral(5)) -> 120 출력"""

def factorial(n):
  output = n
  for i in range(n-1):
    output = output * (i+1)

  return output

print( factorial(4) )