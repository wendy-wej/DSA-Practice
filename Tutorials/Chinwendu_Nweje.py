##QUESTION 1
def return_list(arr):
    i = 0
    my_list = []
    while i < len(arr):
        my_list.append(arr[i])
        i +=2
    return my_list
print("Question 1 solution:", return_list([54, 26, 93, 17, 77, 31, 44, 55, 20]))


##QUESTION 2
def descend_sorter(arr):
    my_dict = {
        '9aa': 1,
        '7a' : 2,
        '67u':3,
        'jh4':4,
        'i234':5
    }

    for i in range(1, len(arr)):
        value_to_sort = arr[i]

        while my_dict[arr[i-1]] < my_dict[value_to_sort] and i>0:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i = i-1

    
    
    return arr

print("Question 2 solution:", descend_sorter(['7a', '9aa', 'i234', 'jh4', '67u']))
