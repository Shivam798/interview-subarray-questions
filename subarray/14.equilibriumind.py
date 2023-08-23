arr=[0, -3, 5, -4, -2, 3, 1, 0]

def sol(arr):
    
    left=[0]*len(arr)
    ans=[]
    for i in range(1,len(arr)):
        left[i]=left[i-1] + arr[i-1]
    right=0
    for i in reversed(range(len(arr))):
        if left[i]==right:
            ans.append(i)
        right+=arr[i]
    return ans
    
def sol1(arr):
    total=sum(arr)
    ans=[]
    right=0
    for i in range(len(arr)):
        if right==total-right-arr[i]:
            ans.append(i)
        right+=arr[i]
    return ans

print(sol1(arr))