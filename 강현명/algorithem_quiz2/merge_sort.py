
def merge( list ):
    list_length = len(list)

    print( list )
    if list_length > 2:
        divide_index = int( list_length/2 )
        print("dividing!")
        half_list = merge( list[:divide_index] )
        half_list2 = merge( list[divide_index:] )
        
        print("sorting! & merge!")
        sort_list = []
        while len(half_list) != 0 and len(half_list2) != 0:
            if half_list[0] > half_list2[0]:
                sort_list.append(half_list2[0])
                del half_list2[0]
            else:
                sort_list.append(half_list[0])
                del half_list[0]

            if len(half_list) == 0:
                sort_list += half_list2
            if len(half_list2) == 0:
                sort_list += half_list

        
        return sort_list

    else:
        return_list = []
        if len(list) == 1:
            return list
        if list[0] > list[1]:
            return_list.append(list[1])
            return_list.append(list[0])
            return return_list
        else:
            return_list.append(list[0])
            return_list.append(list[1])
            return return_list


num_list = [ 29, 23, 2, 5, 74, 12, 99]

print( merge(num_list) )
