# a good question
arr=[0,0,1,0,1,1,1,0,1,1]
def sol(arr):
    count=0
    maxcount=0
    prezero=-1
    maxind=-1
    for i in range(len(arr)):
        if arr[i]==1:
            count+=1
        else:
            count=i-prezero
            prezero=i
        if count>maxcount:
            maxcount=count
            maxind=prezero
    return maxind
print(sol(arr))