A = [0, 0, 1, 0, 1, 1, 0, 1, 0, 0]
for i in A:
    if i == 1:
        A.remove(1)
        A.append(1)
print(A)