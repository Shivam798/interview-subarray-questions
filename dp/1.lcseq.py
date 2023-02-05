
s1 = 'ABCBDAB'
s2 = 'BDCABA'
n1=len(s1)
n2=len(s2)
dp=[[0 for i in range(n2+1)] for j in range(n1+1)]

# lcs1 = simple recursion
# lcs2 = simple recursion wtih memoization (tb algo)
# lcs3 =  dp with 2-d arr (bu algo)
# lcs4 =  print  lcs
# lcs5 =  print  all lcs

def lcs1(s1,s2,n1,n2):
    # t.c=2^(n1+n2)
    # s.c=len(n1+n2) in stack
    if n1==0 or n2==0:
        return 0
    if s1[n1-1]==s2[n2-1]:
        return lcs1(s1,s2,n1-1,n2-1) + 1
    return max(lcs1(s1,s2,n1,n2-1),lcs1(s1,s2,n1-1,n2))

def lcs2(s1,s2,n1,n2,cache):
    # t.c=O(n1.n2)
    # s.c=O(n1.n2)
    if n1==0 or n2==0:
        return 0
    if (n1,n2) in cache:
        return cache[(n1,n2)]
    if s1[n1-1]==s2[n2-1]:
        cache[(n1,n2)] = lcs2(s1,s2,n1-1,n2-1,cache) + 1
    else:
        cache[(n1,n2)] = max(lcs2(s1,s2,n1,n2-1,cache),lcs2(s1,s2,n1-1,n2,cache))
    return cache[(n1,n2)] 

def lcs3(s1,s2,n1,n2,dp):
    # t.c=O(n1.n2)
    # s.c=O(n1.n2)
    
    for i in range(1,n1+1):
        for j in range(1,n2+1):
            if s1[i-1]==s2[j-1]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i][j-1],dp[i-1][j])
    return dp[-1][-1]

def lcs4(s1,s2,n1,n2):
    # to fill the dp 
    lcslength=lcs3(s1,s2,n1,n2,dp)
    # to get a lcs with length of lcslength(we didn't need this variable)
    def lcsone(s1,s2,n1,n2,dp):
        if n1==0 or n2==0:
            return ""
        if s1[n1-1]==s2[n2-1]:
            return lcsone(s1,s2,n1-1,n2-1,dp) + s1[n1-1]
        # if not match
        if dp[n1-1][n2] > dp[n1][n2-1]:
            return lcsone(s1,s2,n1-1,n2,dp)
        else:
            return lcsone(s1,s2,n1,n2-1,dp)

    result = lcsone(s1,s2,n1,n2,dp)
    return result


def lcs5(s1,s2,n1,n2):
    length=lcs3(s1,s2,n1,n2,dp)
   
    def lcsall(s1,s2,n1,n2,dp):
        if n1==0 or n2==0:
            return [""]
        if s1[n1-1]==s2[n2-1]:
            lcs=lcsall(s1,s2,n1-1,n2-1,dp)
            for i in range(len(lcs)):
                lcs[i]=lcs[i]+s1[n1-1]
            return lcs
        if dp[n1-1][n2]>dp[n1][n2-1]:
            return lcsall(s1,s2,n1-1,n2,dp)
                
        if dp[n1][n2-1]>dp[n1-1][n2]:
            return lcsall(s1,s2,n1,n2-1,dp)
        top=lcsall(s1,s2,n1-1,n2,dp)
        left=lcsall(s1,s2,n1,n2-1,dp)
        return top+left

    lcs_list = lcsall(s1,s2,n1,n2,dp)
    return lcs_list


print(lcs5(s1,s2,len(s1),len(s2)))