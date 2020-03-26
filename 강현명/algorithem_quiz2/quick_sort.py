

def quick_sort(list:list):
    

    if len(list) == 0 :
        return []
        
    pivot = list.pop(0)

    if len(list) == 0 :
        return [pivot]
        
    front_list = []
    back_list = []

    for i in range(len(list)):
        if list[i] > pivot:
            back_list.append(list[i])
        else : 
            front_list.append(list[i])

    return quick_sort(front_list) + [pivot] + quick_sort(back_list)

num_list = [ 5, 7, 33, 22, 41, 12, 3, 87, 1]

print( num_list )
print( quick_sort(num_list) )
            