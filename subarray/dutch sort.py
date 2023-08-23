arr=[0, 1, 2, 2, 1, 0, 0, 2, 0, 1, 1, 0 ]
def swap(arr,mid,start):
    arr[mid],arr[start]=arr[start],arr[mid]
def sol(arr):
    start=0
    end=len(arr)-1
    mid=0
    pivot=1
    while mid<=end:
        if arr[mid]<pivot:
            swap(arr,mid,start)
            start+=1
            mid+=1
        elif arr[mid]>pivot:
            swap(arr,mid,end)
            end-=1
            # now we dont know that the swapped element is ont or zero so that's why we don't increase mid
        else:
            mid+=1
    return arr
print(sol(arr))