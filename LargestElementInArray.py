def largest(arr, n):
	max = arr[0]
	for i in range(n):
		if n==1:
			max = arr[0]
		if arr[i] > max:
			max = arr[i]
	print(max)

arr = [1,3,4,5,45,76,89,1111,44,2245,22,31,56]
n = len(arr)

largest(arr, n)

