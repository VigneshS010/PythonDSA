from array import *
def find_max(arr):
    # Your code here
    a = 0
    for i in arr:
        if i>a:
            a=i
    print(a)
arr1 = array('i',[0,0,1,2,3,10,4,5,5,6,7,25])
find_max(arr)

####Reverse
def reverse_array(arr):
    # Your code
    val =  len(arr)-1
    rev = []
    for i in range(0,len(arr)):
        rev.append(arr[val-i])
    print(rev)

reverse_array(arr)


def remove_duplicates(arr):
    # Your code here
    lst = array('i',[])
    for i in arr:
        if i in lst:
            continue
        else:
            lst.append(i)
    print(lst)
remove_duplicates(arr)


def move_zeros(arr):
    # Your code here
    lst = len(arr)-1
    for i in range(0,len(arr)-1):
        if arr[i] == 0:
            arr[lst] , arr[i] = arr[i] , arr[lst]
            lst-=1
        if i == lst:
            break


    print(arr)
move_zeros(arr)

# i can't understand this sum
def two_sum(arr, target):
    num_to_index = {}
    for i, num in enumerate(arr):
        if target - num in num_to_index:
            return [num_to_index[target - num], i]
        num_to_index[num] = i
    return []

print(two_sum(arr, 5))


def rotate_array(arr, k):
    # Your code here
    pivot = 0
    for i in range(0,len(arr)-1):
        if arr[i] == k:
            pivot = i
    print(arr[pivot:] + arr[:pivot])

rotate_array(arr , 10)


#Missing value
def find_missing_number(arr):
    # Your code here
    mi = min(arr)
    ma = max(arr)

    for i in range(mi , ma-1):
        if i not in arr:
            print(i,end=" ")

find_missing_number(arr)


arr2 = array('i',[8,9,11,12,13,14,15])
def merge_sorted_arrays(arr1, arr2):
    merged = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    merged.extend(arr1[i:])
    merged.extend(arr2[j:])
    print( merged )


merge_sorted_arrays(arr1,arr2)














