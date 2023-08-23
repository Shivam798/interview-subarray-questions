X = [1, 4, 7, 8, 10]
Y = [2, 3, 9]

def sol(x,y):
    m=len(x)
    n=len(y)

    for i in range(m):
        if x[i]>y[0]:
            x[i],y[0]=y[0],x[i]
            first=y[0]
            k=1
            while k<n and y[k]<first:
                y[k-1]=y[k]
                k+=1
            y[k-1]=first
    print(x,y)


print(sol(X,Y))