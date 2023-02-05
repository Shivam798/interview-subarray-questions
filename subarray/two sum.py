nums = [8, 7, 2, 5, 3, 1]
target = 10

# solve1=brute force
# solve2=sort then two pointer
# solv3 = using set

def solve1(n,arr):

    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if target==nums[i]+nums[j]:
                print(nums[i],nums[j])

def solve2(nums,t):
    arr=sorted(nums)
    l=0
    r=len(arr)-1
    while l<r:
        summ=arr[l]+arr[r]
        if t==summ:
            print(arr[l],arr[r])
            l+=1
            
        elif t>summ:
            l+=1
        elif t<summ:
            r-=1

def solve3(nums,t):
    mapp=set()
    for k,v in enumerate(nums):
        rem=t-v
        if rem in mapp:
            print(v,rem)
        mapp.add(v)

print(solve3(nums,target))
