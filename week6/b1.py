#Create a function that sorts an array by using selection sort.
def sortArr(arr):
	for i in range(len(arr)):
		min=i
		temp=0
		for j in range(i+1,len(arr)):
			if arr[min] > arr[j]:
				min = j
		temp = arr[min]
		arr[min]=arr[i]
		arr[i]=temp
	return arr
arr=[12,98,65,41,76,89,100]
print(sortArr(arr))

#Create a function that multiplies two arrays.
def array_multiply(arr1,arr2):
	resArr=[]
	for i,j in zip(arr1,arr2):
		resArr.append(i*j)
	return resArr
arr1 = [1, 2, 3]
arr2 = [4, 5, 6]
print(array_multiply(arr1,arr2))
