def Occurence(arr, n):
    visited = [False] * n
    # loop through the each element in the array
    for i in range(n):
        # if the current element is already counted , skip it 
        if(visited[i]) == True:
            continue
        count = 1 # for the current element 
        for j in range(i+1, n):
            if(arr[i] == arr[j]):
                visited[i] = True
                count += 1
        print(arr[i], count)        


if __name__ == "__main__":
    arr = [10,20,30,40 ,50 , 60, 70,10 ]
    n = len(arr)
    Occurence(arr, n)

