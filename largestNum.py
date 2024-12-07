def findlargestNum(arr, n):
    max = arr[0]
    for i in range(0,n):
        if(max < arr[i]):
            max = arr[i]
    return max

if __name__ =="__main__":
    arr1 = [3,4,2,1,5,6,32,1,4,54,22,53]
    n = len(arr1)
    print("the length of the array is: ", n)
    max = findlargestNum(arr1, n)
    print("the largest element in the array: ", max)