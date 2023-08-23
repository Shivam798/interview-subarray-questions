arr = [6, 0, 8, 2, 3, 0, 4, 0, 1]

def sol(arr):
    k=0
    for i in range(len(arr)):
        if arr[i]:
            arr[k],arr[i]=arr[i],arr[k]
            k+=1
    return arr


print(sol(arr))