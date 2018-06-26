def binary_search(list, item):
	begin = 0
	end = len(list) - 1
	

	while begin <= end:
		mid = int((end + begin) / 2)
		guess = list[mid]
		if guess == item:
			return mid
		if guess < item:
			begin = mid + 1
		else:
			end = mid - 1
	
	return None

l = [1, 3, 5, 7, 9]
print binary_search(l, 4)