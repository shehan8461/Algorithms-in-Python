def selectionsort(arr):
    n=len(arr)
    for i in range(n):
        min_index=i
        for j in range (i+1,n):
            if arr[min_index]>arr[j]:
                min_index=j

        arr[i],arr[min_index]=arr[min_index],arr[i]
        
arr=[12,6,7,8,10,2,9]
print("before sorting :{}".format(arr))
selectionsort(arr)
print('after sorting :{}'.format(arr))

