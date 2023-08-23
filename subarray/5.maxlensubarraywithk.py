arr1 = [5, 6, -5, 5, 3, 5, 3, -2, 0]
t1= 8

arr2=[1,2,3,4,5,6,7,8,9,10]
t2= 15

t3=15
arr3=[-13 ,0 ,6 ,15 ,16 ,2 ,15 ,-12 ,17 ,-16 ,0 ,-3 ,19 ,-3 ,2 ,-9,-6]

# maxisub = hashing 
# solv3 = two pointer with starting and ending points of subarray


def maxisub(arr,t):
    d={}
    d[0]=-1
    endidn=-1
    presum=0
    length=0

    for i in range(len(arr)):
        presum+=arr[i]
        rem=presum-t
        if rem in d and length<i-d[rem]:
            length=i-d[rem]
            endidn=i
        if presum not in d:
            d[presum]=i
    return length,endidn-length+1,endidn

def solv3(arr,t):
    i,j,sum,maxlength=0,0,0,0
    while j<len(arr):
        sum+=arr[j]
        if sum==t:
            maxlength=max(maxlength,j-i+1)
        elif sum>t:
            while sum>t:
                sum-=arr[i]
                i+=1
        j+=1
    return maxlength 


print(maxisub(arr2,t2))


