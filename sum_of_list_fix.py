def sum_of_list(lst):
    sum = 0
    for i in range(lst):
        if i.isnumeric():
            sum = sum + i
        else:
            pass
    return sum 