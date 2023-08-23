arr=[2,1,5,6,2,3]

def largestRectangleArea(arr):
        st=[]
        res=0
        for i in arr+[-1]:
            step=0
            while st and st[-1][1]>=i:
                w,h=st.pop()
                step+=w
                res=max(res,step*h)
            st.append((step+1,i))
        return res

def largestRectangleArea2(heights) :
        heights.append(0)
        stack=[-1]
        
        area, i = 0,0
        while i < len(heights):
            last_h = heights[stack[-1]] if i>0 else 0
            
            if heights[i]>=last_h:
                stack.append(i)
                i+=1
            else:
                height = heights[stack.pop()]
                left = stack[-1]
                width = i-left-1
                
                #print(f"right={i} h={h} | left={left}, height={height}, area={a}")
                area = max(area, width * height)
        return area
print(largestRectangleArea2(arr))