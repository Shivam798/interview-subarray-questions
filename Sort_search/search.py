arr=[4,5,6,7,2,3,1,8]
def linear(arr,tar):
    for i in arr:
        if i==tar:
            return True
    return False

def binary(arr,tar):
    l=0
    r=len(arr)-1
    while l<=r:
        mid=(l+r)//2
        if arr[mid]>tar:
            r-=1
        elif arr[mid]<tar:
            l+=1
        else:
            return True
    return False
arr.sort()
print(binary(arr,5))
print(binary(arr,8))