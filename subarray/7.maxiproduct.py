arr=[-10, -3, 5, 6, -2]
def sol1(arr):
    ans=-float('inf')
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            ans=max(ans,arr[i]*arr[j])
    return ans

def sol2(arr):
    
print(sol1(arr))