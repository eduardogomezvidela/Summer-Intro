def find_outlier(integers):
    new_list= []
    
    for num in integers:
    
        new_list = new_list + [num % 2]

    print(new_list)

    if new_list.count(0) > 1:
        position = new_list.index(1)
        return integers[position]

    elif new_list.count(1) > 1:
        position = new_list.index(0)
        return integers[position]




list = [2,4, 8 ,16, 3, 14, 20]

print(find_outlier(list))
