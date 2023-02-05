arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]

# lis1= recursion method
# lis2= bottom up method
# lis3= sort the given arr and use lcseq concept
# lis3= print lis

def lis1(arr,i,n,prev):
    if i==n:
        return 0
    nottake= lis1(arr,i+1,n,prev)
    take=0
    if arr[i]>prev:
        take =1+ lis1(arr,i+1,n,arr[i])
    return max(take,nottake)

def lis2(arr,n):
    dp=[1]*n
    for i in range(n):
        for j in range(i):
            if arr[j]<arr[i]:
                dp[i]=max(dp[i],dp[j]+1)
            
    return max(dp)

def lis3(arr):
    s2=sorted(arr)
    s1=arr
    n=len(s1)
    dp=[[0 for j in range(n+1)]for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            if s1[i-1]==s2[j-1]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    return dp[-1][-1]

def lis4 (arr):
    n=len(arr)
    dp=[1]*n
    def lislen(arr,n):
        for i in range(n):
            for j in range(i):
                if arr[j]<arr[i]:
                    dp[i]=max(dp[i],dp[j]+1)

        return max(dp)
    
    # main log for printing the lis
    length=lislen(arr,len(arr))
    print(arr)
    print(dp)
    res=[]
    curr_len=length
    next_ind=0
    for i in reversed(range(n)):
        if dp[i]==curr_len and (curr_len==length or arr[i]<arr[next_ind]):
            res.append(arr[i])
            curr_len-=1
            next_ind=i
    print(list(reversed(res)))
    


print(lis4(arr))