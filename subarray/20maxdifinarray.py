arr= [2, 7, 9, 5, 1, 3, 5]
arr1=[9,8,7,6,5,4,3,2,1]
def sol(arr):
    diff=0
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[j]>arr[i]:
                diff=max(diff,arr[j]-arr[i])

    return diff

def sol1(arr):
    minfar=arr[0]
    diff=-float('inf')
    for i in range(1,len(arr)):
        if arr[i]>=minfar:
            if diff<arr[i]-minfar:
                diff=arr[i]-minfar
        else:
            minfar=arr[i]
    return diff if diff != -float('inf') else 0

print(sol1(arr))
print(sol1(arr1))