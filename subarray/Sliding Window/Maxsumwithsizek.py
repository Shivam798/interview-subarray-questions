arr=[3, 5, 2, 1, 7]
k=2 
# arr=[4, 2, 3, 5, 1, 2]
# k=3
def maxsumwithksize(arr,k):
    windsum=sum(arr[:k])
    maxsum=windsum
    for i in range(len(arr)-k):
        windsum=windsum-arr[i]+arr[i+k]
        if maxsum<windsum:
            maxsum=windsum
    return maxsum
# print(maxsumwithksize(arr,k))

# aditya verma solution
def solve2(arr,k):
    i=j=0
    summ=0
    maxsum=0
    while j<len(arr):
        summ+=arr[j]
        if j-i+1<k:
            j+=1
        elif j-i+1==k:
            maxsum=max(maxsum,summ)
            summ-=arr[i]
            i+=1
            j+=1
        
            
    return maxsum
print(solve2(arr,k))