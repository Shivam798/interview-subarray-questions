from collections import Counter
arr=[1, 8, 7, 4, 1, 2, 2, 2, 2, 2, 2]
d=Counter(arr)
for k,v in d.items():
    if v>len(arr)/2:
        print(k)