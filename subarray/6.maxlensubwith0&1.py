arr=[0, 0, 1, 0, 1, 0, 0]
def solv(arr):
    d={}
    d[0]=-1
    endidn=-1
    sum=0
    length=0
    for i in range(len(arr)):
        sum+=-1 if arr[i]==0 else 1
        if sum in d and length<i-d[sum]:
            length=i-d[sum]
            endidn=i
        if sum not in d:
            d[sum]=i
    if endidn!=-1:
        print(endidn-length+1,endidn)

    
print(solv(arr))  