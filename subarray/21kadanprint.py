arr=[-2, 1, -3, 4, -1, 2, 1, -5, 4]
def sol(arr):
    maxupto=0
    maxspfar=0
    beg=0
    for i in range(len(arr)):
        maxupto+=arr[i]
        if maxupto<arr[i]:
            maxupto=arr[i]
            beg=i
        if maxspfar<maxupto:
            maxspfar=maxupto
            start=beg
            end=i
    return arr[start:end+1]
print(sol(arr))