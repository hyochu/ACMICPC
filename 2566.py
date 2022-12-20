maxVal, idx_i, idx_j = 0, 0, 0
for i in range(9):
  a = list(map(int, input().split()))
  for j in range(9):
    if max(a) >= maxVal:
      maxVal = max(a)
      idx_i = i+1
      idx_j = a.index(maxVal)+1
print(maxVal)
print(idx_i, idx_j)
