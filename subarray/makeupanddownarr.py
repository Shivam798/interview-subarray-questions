arr = [9, 6, 8, 3, 7]

def sol(arr):
    for i in range(1,len(arr),2):
        if arr[i-1]>arr[i]:
            arr[i-1],arr[i]=arr[i],arr[i-1]
        if i+1<len(arr) and arr[i+1]>arr[i]:
            arr[i+1],arr[i]=arr[i],arr[i+1]
    return arr
print(sol(arr))