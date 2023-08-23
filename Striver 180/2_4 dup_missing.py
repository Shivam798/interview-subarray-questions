def findduplicate_missing_1(arr):
    n=len(arr)
    hash=[0]*(n+1)
    for i in range(n):
        hash[arr[i]]+=1
    rep=-1
    dupl=-1
    for i in range(1,n+1):
        if hash[i]>1:
            rep=i
        elif hash[i]==0:
            dupl=i
    return [rep,dupl]

def findduplicate_missing_2(arr):
    x=-1 #duplicate
    y=-1 #missing
    n=len(arr)
    s=sum(arr)
    sn=n*(n+1)/2
    # s-sn=x-y
    val1=s-sn

    snn=(n * (n + 1) * (2 * n + 1)) // 6
    s2=0
    for i in arr:
        s2+=i*i
    # s2-snn=x^2-y^2
    val2=s2-snn

    # x+y = val2//val1
    val3=val2//val1
    x=(val1+val3)//2
    y=x-val1

    return [int(x),int(y)]
arr=[3, 1, 2, 5, 4, 6, 7, 5]
print(findduplicate_missing_2(arr))