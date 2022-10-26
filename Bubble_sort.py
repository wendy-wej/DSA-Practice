from csv import list_dialects
from platform import java_ver

############################ BUBBLE SORT ###############

def bubble(list_a):
    indexing_length = len(list_a) -1
    sorted = False
    swaps = 0

    while not sorted:
        sorted = True
        for i in range(0, indexing_length):
            if list_a[i] > list_a[i+1]:
                sorted = False
                list_a[i], list_a[i+1] = list_a[i+1], list_a[i]
        swaps +=1
    print("swaps: ", swaps)   
    print("YT guy bubble sort:", list_a)
    return list_a

bubble([4,6,8,3,2,5,7,8,9])


def g4g_bubble_sort(arr):
    n = len(arr) -1
    for i in range(n):
        for j in range(0, n-i-1):

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print("Geeks for Geeks bubble sort:", arr)
    return(arr)

g4g_bubble_sort( [4,6,8,3,2,5,7,8,9])




##########################  SELECTION SORT ##############################

def selection_sort(list_b):
    indexing_length = range(0, len(list_b)-1)

    for i in indexing_length:
        min_value = i
        print("min_val", min_value)

        for j in range(i+1, len(list_b)):
            if list_b[j] < list_b[min_value]:
                min_value = j

        if min_value != i:
            list_b[min_value], list_b[i] = list_b[i], list_b[min_value] 
        print("YT guy selection sort:", list_b)
    return list_b
selection_sort([64, 25, 12, 22, 11])



def g4g_selection_sort(arr_x):
    for i in range(len(arr_x)-1):
        min_value = i

        for j in range(1, len(arr_x)-1 ):
            if arr_x[min_value] > arr_x[j]:
                min_value = j

        arr_x[i], arr_x[min_value] = arr_x[min_value], arr_x[i]

    print("Geeks for Geeks selection sort:", arr_x)
    return(arr_x)

g4g_selection_sort( [4,6,8,3,2,5,7,8,9])


###################### INSERTION SORT #################

def my_insertion_sort(list_c):
    sorted_list = []

    sorted_list.append(list_c[0])

    for i in range(1, len(list_c)):
        sorted_list.append(list_c[i])
        print("Sorted List:", sorted_list)

        for j in range(1, len(sorted_list)):
            if sorted_list[-j] < sorted_list[-j-1]:
                sorted_list[-j], sorted_list[-j-1] = sorted_list[-j-1], sorted_list[-j]
    
    print("MY Sorted List:", sorted_list)
    return sorted_list
my_insertion_sort([3,1,8,4,9,3,5,6,2])


def his_insertion_sort(list_d):
    for i in range(1, len(list_d)):
        value_to_sort = list_d[i]

        while list_d[i-1] > value_to_sort and i>0:
            list_d[i], list_d[i-1] = list_d[i-1], list_d[i]
            i = i-1

    print("MY Sorted List:", list_d)
    return list_d
his_insertion_sort([3,1,8,4,9,3,5,6,2])

###################### QUICK SORT ##############

def quick_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()

    greater_items =[]
    lesser_items =[]
    
    for item in sequence:
        if item > pivot:
            greater_items.append(item)
        else:
            lesser_items.append(item)

    return quick_sort(lesser_items) + [pivot] + quick_sort(greater_items)
print(quick_sort([5,6,7,8,9,8,13 ,6,5,6,7,2,1,0]))

################## BINARY SEARCH ###########################
def binary_search(sequence, item):
    begin_index = 0
    end_index = len(sequence) -1

    while begin_index <= end_index:
        midpoint = begin_index + (end_index - begin_index) // 2
        midpoint_value = sequence[midpoint]
        if midpoint_value == item:
            return midpoint

        elif item < midpoint_value:
            end_index = midpoint - 1

        else:
            begin_index = midpoint +  1

    return None
sequence_a = [0,1,3,4,7,8,9,12]
item_a = 8    

print(binary_search(sequence_a, item_a))