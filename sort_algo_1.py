#Selection sort
def selectionSort(arr):
	n = len(arr)
	for i in range(n):
		min_index = i
		for j in range(i+1, n):
			if arr[j] < arr[min_index]:
				min_index = j
		arr[i], arr[min_val] = arr[min_index], arr[i]
	print(arr)

selectionSort([4,3,5,2,1])