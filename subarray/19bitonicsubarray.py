arr = [3, 5, 8, 4, 5, 9, 10, 8, 5, 3, 4]

def sol(arr):
    if arr==[]:
        return 0
    n=len(arr)
    I=[1]*n
    D=[1]*n
    
    for i in range(1,n):
        if arr[i-1]<arr[i]:
            I[i]=I[i-1]+1
    for i in reversed(range(n-1)):
        if arr[i+1]<arr[i]:
            D[i]=D[i+1]+1
    length=0
    midpoint=0
    for i in range(n):
        if length<I[i]+D[i]-1:
            length=I[i]+D[i]-1
            beg=i-I[i]+1
            end=i+D[i]+1
            midpoint=i
        
    return length,arr[beg:end+1]

def sol2(arr):
    i=0
    n=len(arr)
    l=0
    endidn=0
    while i+1<n:
        length=1
        while i+1 < n and arr[i]<arr[i+1]:
            length+=1
            i+=1
        
        while i+1 < n and arr[i] > arr[i+1]:
            length+=1
            i+=1
        
        while i+1 < n and arr[i+1]==arr[i]:
            # length+=1
            i+=1
        if l<length:
            l=length
            endidn=i

    return arr[endidn-l+1:endidn+1] 

    
print(sol2(arr))