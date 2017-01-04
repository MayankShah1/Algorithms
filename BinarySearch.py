def binary_search(numbers, key):

	'''(list of int, int) -> int

	Returns the position of key in number

	>>> binary_search([1,5,6,8,2,4,10],4)
	3
	'''

	numbers.sort();

	low = 0
	high = len(numbers)

	while low <= high:
		mid = low + (high - low) // 2
		if numbers[mid] == key:
			return mid + 1
		elif numbers[mid] < key:
			low = mid + 1
		else :
			high = mid - 1
	
	return 0
