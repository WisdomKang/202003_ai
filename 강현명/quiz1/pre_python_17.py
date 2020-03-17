"""17. 1988년 ~ 2060년까지 중 월드컵이 개최되는 연도를 출력하시오"""

first_world_cup_year = 1930

step = 4

for i in range( first_world_cup_year, 2060, step):
    if i > 1988: print( i )
