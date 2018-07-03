def find_smallest(arr):
    smallest = arr[0]
    index_of_smallest = 0
    for i in xrange(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            index_of_smallest = i
    return [smallest, index_of_smallest]



def selection_sort(arr):
    new_arr = []
    # at first, I think use pop method will chenge the arr and
    # it will affect the length of arr, but this line acts as the 
    # fact that I need to loop as many times as the number of items
    # in a lists
    for i in xrange(len(arr)):
        index_of_smallest = find_smallest(arr)[1]
        new_arr.append(arr.pop(index_of_smallest))
    return new_arr

print selection_sort([1, 4, 4, 5, 8, 8, -1])