"""3.Enter key를 눌러 주사위를 던지게 한 후, 주사위의 눈이 높은 사람이 승리하는
간단한 주사위 게임을 만드세요"""

import random

input("사작하려면 Enter를 누르세용")
player1 =random.randint(1, 6)
player2 =random.randint(1, 6)


print( "player1:", player1 )
print("player2:", player2)

if player1 > player2:
    print("player1 승!")
elif player1 < player2:
    print("player2 승!")
else:
    print("무승부!")