arr=[4,3,2,1,4]

def water(arr):
    left=0
    right=len(arr)-1
    ans=0
    while left<right:
        if arr[left]<=arr[right]:
            res=arr[left]*(right-left)
            left+=1
        else:
            res=arr[right]*(right-left)
            right-=1
        if res>ans:
            ans=res

    return ans 
print(water(arr))