l = [1, 4, 5, 6, 16, 18, 20, 78, 78, 78, 78, 78, 78, 78, 78, 120, 1000, 2000, 3200]

num = 79

start = 0
end = len(l) - 1

def binary_search():
    global start
    global end
    while True:
        mid = (start + end) // 2
        if num > l[mid]:
            start = mid + 1
        else:
            end = mid
        if start == end:
            if l[start] == num:
                print("index:", start)
                return
            else:
                print("index:", None)
                return

binary_search()