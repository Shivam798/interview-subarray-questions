def solve(s):
    start=0
    end=len(s)-1
    res=0
    while start<end:
        if s[start]==s[end]:
            start+=1
            end-=1
        else:
            res+=1
            start=0
            end=len(s)-res-1
    return res


if __name__=='__main__':
    string='AACECAAAA'
    print(solve(string))