def bubblesort(arr):
    n=len(arr)
    for k in range (0, n):
        for j in range (0, n-k-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                
arr=[12,6,7,8,10,2,9]
print("before sorting : {}". format(arr)) 
bubblesort(arr)
print("after sorting :{}".format(arr))





