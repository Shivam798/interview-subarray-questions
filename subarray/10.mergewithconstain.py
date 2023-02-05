X = [0, 2, 0, 3, 0, 5, 6, 0, 0]
Y = [1, 8, 9, 10, 15]


def merge(x,y,m,n):
    k=m+n+1
    while m>=0 and n>=0:
        if x[m]>y[n]:
            x[k]=x[m]
            m-=1
            k-=1
        else:
            x[k]=y[n]
            n-=1
            k-=1
    while n>=0:
        x[k]=y[n]
        n-=1
        k-=1
    return x


def rearrange(x,y):
    k=0
    for i in range(len(x)):
        if x[i]:
            x[k],x[i]=x[i],x[k]
            k+=1
    print(x,k)

    return merge(x,y,k-1,len(y)-1)
print(rearrange(X,Y))

