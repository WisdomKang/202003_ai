

def fibonacci( n , start=0, before=1, before2=0):
    start += 1
    if n == 1 or n == 2 : return 1

    if start == n:
        return before
    else:
        next_num = before + before2
        next_num2 = before
        print("{}번째 항:".format(start) , before )
        return fibonacci( n , start, next_num, next_num2)

print( fibonacci( 10))