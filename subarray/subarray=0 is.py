# nums = [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]

nums = [5, 6, -5, 5, 3, 5, 3, -2, 0]

# solv1= subarray have 0 or not
# solv2= all subarray have 0 print or not 

def solv1(nums):
    s=set()
    total=0
    
    for idn,i in enumerate(nums):
        total+=i
        if total in s:
            return True
            
            
            
        s.add(total)
    return 

def solv2(nums):
    d={}
    total=0
    d.setdefault(total,[]).append(-1)
    for i in range(len(nums)):
        total+=nums[i]
        
        if total in d: #condition for zero sum 
            listt= d.get(total)
            for item in listt:
                print(item+1,i)
        d.setdefault(total,[]).append(i)
    

print(solv2(nums))