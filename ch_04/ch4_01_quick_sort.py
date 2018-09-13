import random

lst = [random.randint(0, 99) for x in range(10)]

def quick_sort(lst):
    if len(lst) == 0 or len(lst) == 1:
        return lst

    pivot = lst[0]
    left = []
    right = []


    for item in lst[1:]:
        if item < pivot:
            left.append(item)
        else:
            right.append(item)

    return quick_sort(left) + [pivot] + quick_sort(right)

print(lst)
print(quick_sort(lst))
