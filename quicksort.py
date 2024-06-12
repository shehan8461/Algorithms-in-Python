def partition(array,lb,ub):
    pivot=array[lb]
    start=lb+1
    end=ub

    while True:
        while array[start] <= pivot and start <=end:
            start=start+1
        while array[end] > pivot and start <=end:
            end=end-1

        if start < end:
            array[start],array[end]=array[end],array[start]
        else:
            break

    array[lb],array[end]=array[end],array[lb]
    return end 




def quicksort(array,start,end):
    if start >=end:
        return
    
    k=partition(array,start,end)
    quicksort(array,start,k-1)
    quicksort(array,k+1,end)

data=[10,6,11,8,12,2,9,15]  
print("before sorting :{}".format(data)) 


lb=0
ub=len(data)-1
quicksort(data,lb,ub)
print("after sorting :{}".format(data))