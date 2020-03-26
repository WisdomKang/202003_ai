#요번것은 구글링으로 참고해서 작성하였습니다.

def top_of_hanoi(floor, from_pos="1", to_pos="3", aux_pos="2"):
     if floor == 1:
         print("{}번째 원반을 {}번째에서 {}번째 기둥으로 옮깁니다.".format(floor, from_pos, to_pos))
         return

     top_of_hanoi(floor-1,from_pos, aux_pos,to_pos)
     print("{}번째 원반을 {}번째에서 {}번째 기둥으로 옮깁니다.".format(floor, from_pos, to_pos))
     top_of_hanoi(floor-1, aux_pos, to_pos, from_pos)

    

top_of_hanoi(4)
     
