# Function to reverse the array using recursion

def reverseArray(arr, start, end):
    # base case : stop when  the start is not less than end 
    if start >= end:
        return 
    # swap element at start and end
    arr[start], arr[end] = arr[end], arr[start]

    reverseArray(arr, start + 1, end -1)

# function to print an array 
def printArray(arr, n):
    print("the reversed array is :- ")
    for i in range(n):
        print(arr[i], end=" ")
    print()    

if __name__ == "__main__":
    arr = [3,2,1,5,3,2,7,8]
    n = len(arr)
    reverseArray(arr, 0, n-1)
    printArray(arr,n)