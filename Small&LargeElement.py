# second smallest and second largest element in an array 
def secondSmallest(arr, n):
    if n < 2:    #if array has less than 2 element , return -1
        return -1
    small = float('inf') #intialize the smallest to infinity
    second_small= float('inf') # initialize the second smallest to infinity

    for i in range(n):
        if arr[i] < small:
            second_small = small #update second smallest 
            small = arr[i] # update smallest 
        elif arr[i] < second_small and arr[i] != small:
            second_small = arr[i] #update second smallest if the current element is smaller 
    return second_small
            

def secondLargest(arr,n):
    if n < 2:
        return -1
    large = float('-inf') # Initialize the largest to negative infinity
    second_large = float('-inf') # initialize the second largest to negative infinity

    for i in range(n):
        if arr[i] > second_large: #update second largest
            large = arr[i] #update largest
            second_large = large #update the second largest
        elif arr[i] > second_large and arr[i] != large:
            second_large = arr[i]
    return second_large


if __name__ == "__main__":
    arr1 = [6,2,4,57,8,4,2,1,]
    n = len(arr1)

    # second smallest element in array
    sS = secondSmallest(arr1, n)
    # second largest element in the array
    sL = secondLargest(arr1, n)

    print("second smallest is : ", sS)
    print("second largest is: ", sL)
 
