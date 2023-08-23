from collections import defaultdict
arr=[1,2,3,4,5,6]
def two_sum(arr,target):
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            summ=arr[i]+arr[j]
            if summ==target:
                return [arr[i],arr[j]]
    return [-1]
def solve(arr,target):
    d=defaultdict(int)
    for i in arr:
        rem=target-i
        if rem in d:
            return [i,rem]
        d[i]+=1
    return [-1]
def solve2(arr,t):
    arr.sort()
    l=0
    r=len(arr)-1
    while l<r:
        summ=arr[l]+arr[r]
        if t==summ:
            return [arr[l],arr[r]]
        elif summ<t:
            l+=1
        else:
            r-=1
    return [-1]
print(solve2(arr,7))