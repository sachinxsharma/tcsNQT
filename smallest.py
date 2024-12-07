# Find the smallest number in an array
def smallestnum(arr):
    # initialize the minimum with the first element 
    min_element = arr[0];
# iterate through the array
    for num in arr:
        if num < min_element:
            min_element = num;
    return min_element

arr1 = [2,5,1,3,0,6,7,8];
print("the smallest element in the array is: ", smallestnum(arr1))


# dry code
# define function 
# initialize min values with the first array arr[0]
# iterate through each element in the array 
# if num < minValue:
# minValue = num;
# return min_element 