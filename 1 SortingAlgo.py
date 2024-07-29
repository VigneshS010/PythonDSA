a = [5,4,7,6,1,2,0,3,8]

# Bubble sort Algorithm
# It itterate through the list , it compares the 2 numvers j and j+1 if the j is bigger,
# It change their position , it runs in 5 times reverse order

def bubble_sort(a):
    for i in range(len(a)-1, 0, -1):
        for j in range(i):
            if a[j] > a[j+1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp

# bubble_sort(a)
# print(a)


# Selection Sort

# the selection sort uses the index
# first it iterate through the list and find min value and store theri index
# store index in min_index
# After the first loop it changes the min_index value to the 0th index and so on
# It have a special case when there is no changes

def selection_sort(a):
    # THere is no need to check last value
    for i in range(len(a)-1):
        min_index = i
        for j in range(i+1, len(a)):
            if a[j] < a[min_index]:
                min_index = j
        # THis to check there is any change
        if i != min_index:
            temp = a[i]
            a[i] = a[min_index]
            a[min_index] = temp
    print(a)

# selection_sort(a)



# Insertion Sort
# This sorting algorithm is good for almost sorted list
# The insertion sort iterate through the loop
# It always compares it value with it prev num , so it starts with index 1
# It changes the value until it reaches their smaller position

def insertion_sort(a):
    for i in range(1,len(a)):
        temp = a[i]
        j = i-1

        # this while 2nd condition used so prevent the index goes to -1
        while temp < a[j] and j > -1:
            a[j+1] = a[j]
            a[j] = temp
            j -= 1

    print(a)

# insertion_sort(a)



# Merge Sort Algorithm
# this algorithm splits data until it single
# Menging 2 , 2 .... then merge the merged soort so now it have 4 , 4...
# merging and solrting them simultaneously from bottom up

# HELPER FUNCTION
def merge(list1, list2):
    combined = []
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j +=1
    while i < len(list1):
        combined.append(list1[i])
        i+=1
    while j < len(list2):
        combined.append(list2[j])
        j+=1

    return combined

# Merge sort function

def merge_sort(a):
    if len(a) == 1:
        return a
    mid_index = int(len(a) / 2)
    left = merge_sort(a[:mid_index])
    right = merge_sort(a[mid_index:])

    return merge(left, right)

print(merge_sort(a))