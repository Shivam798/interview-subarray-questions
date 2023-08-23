arr1 = [1, 56, 58, 57, 90, 92, 94, 93, 91, 45]
arr = [10, 12, 12, 10, 10, 11, 10]


# sol = work with non 
def sol(arr):
    maxlength=1
    for i in range(len(arr)-1):
        maxx=arr[i]
        minn=arr[i]
        for j in range(i+1,len(arr)):
            maxx=max(maxx,arr[j])
            minn=min(minn,arr[j])
            if maxx-minn==j-i:
                maxlength=max(maxlength,j-i+1)
    return maxlength

def sol2(arr):
    maxlength=1
    s=set()
    for i in range(len(arr)-1):
        s.add(arr[0])

        mx=arr[i]
        mi=arr[i]
        for j in range(i+1,len(arr)):
            if arr[j] in s:
                break
            s.add(arr[j])
            

            mx=max(mx,arr[j])
            mi=min(mi,arr[j])
            if mx-mi==j-i:
                maxlength=max(maxlength,j-i+1)
    return maxlength

print(sol2(arr))