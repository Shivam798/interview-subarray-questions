arr=[100,80,60,70,60,75,85]
# Next smallest right

# def firt_nearest_element(arr):
#     n=len(arr)
#     res=[-1]*n
#     st=[]
#     for i in range(n):
#         while st and arr[i]<arr[st[-1]]:
#             index=st.pop()
#             res[i]=index 
#         st.append(i)

# Next greater right

# def firt_nearest_element(arr):
#     n=len(arr)
#     res=[-1]*n
#     st=[]
#     for i in range(n):
#         while st and arr[i]>arr[st[-1]]:
#             index=st.pop()
#             res[i]=index 
#         st.append(i)

#     return res

# Next smaller left

# def firt_nearest_element(arr):
#     n=len(arr)
#     res=[-1]*n
#     st=[]
#     for i in range(n)[::-1]:
#         while st and arr[i]<arr[st[-1]]:
#             index=st.pop()
#             res[i]=index 
#         st.append(i)

#     return res

# Next greater left

# def firt_nearest_element(arr):
#     n=len(arr)
#     res=[-1]*n
#     st=[]
#     for i in range(n)[::-1]:
#         while st and arr[i]>arr[st[-1]]:
#             index=st.pop()
#             res[i]=index 
#         st.append(i)

#     return res


# NGL-i
def stock_span(arr):
    stack = []
    result = [-1] * len(arr)  # Initialize the result array with -1
    
    for i in range(len(arr)-1,-1,-1):
        while stack and arr[i] > arr[stack[-1]]:
            index = stack.pop()
            result[index] =i
        stack.append(i)
    ans=[0]*len(arr)
    for i in range(len(arr)):
        ans[i]=i-result[i]

    return ans

print(stock_span(arr))