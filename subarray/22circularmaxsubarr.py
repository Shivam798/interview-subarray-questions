arr=[2, 1, -5, 4, -3, 1, -3, 4, -1]
arr=[-1,-4,-5,-2,-1]
arr=[-2,-3,-1]
# sol=can print array and sum
# sol1=only sum

def sol(arr):
    newarr=arr+arr
    maxx=0
    maxfar=-float('inf')
    beg=0
    end=0
    for i in range(len(newarr)):
        maxx+=newarr[i]
        if maxx<newarr[i]:
            maxx=newarr[i]
            beg=i
        if maxx>maxfar:
            maxfar=maxx
            end=i
    print(newarr[beg:end+1],maxfar)

def sol1(arr):
    # newarr=arr+arr
    maxx=0
    maxfar=-float('inf')
    beg=0
    end=0
    n=len(arr)
    for i in range(n+n):
        maxx+=arr[i%n]
        if maxx<arr[i%n]:
            maxx=arr[i%n]
            beg=i
        if maxx>maxfar:
            maxfar=maxx
            end=i
    print(maxfar)

print(sol1(arr))