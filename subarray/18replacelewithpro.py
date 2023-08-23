arr = [5, 3, 4, 2, 6, 8]
def sol(arr):
    n=len(arr)
    left=[None]*n
    right=[None]*n
    left[0]=1
    right[n-1]=1
    for i in range(1,n):
        left[i]=arr[i-1]*left[i-1]
    for i in reversed(range(n-1)):
        right[i]=arr[i+1]*right[i+1]

    for i in range(n):
        arr[i]=left[i]*right[i]
    return arr
print(sol(arr))