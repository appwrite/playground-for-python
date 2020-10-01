import sys
#function to print the minimum of array.
def min_of_array(arr,min_so_far=sys.maxsize):
	if len(l)==0:
		print(min_so_far)
		return
	new_min=min(min_so_far,l[0])
	min_of_array(l[1:],new_min)

arr=list(map(int, input().split()))
min_of_array(arr)
