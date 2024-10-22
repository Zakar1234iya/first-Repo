def bubble_sort(arr):
    n = len(arr)
    count =0
    for n in range(n): 
        for i in range( 0 , len(arr)-1 , 1 ): 
            count = count+ 1
            if arr[i] > arr[i+1]:
                temp= arr[i+1]
                arr[i+1]=arr[i]
                arr[i]=temp
                print(arr)
    print(count)

arr = [2, 10, 4, 5, 11]
arr2 = [39, 12, 18, 72, 10, 2, 85 ,18 , 0]
print(arr)
bubble_sort(arr)
bubble_sort(arr2)


