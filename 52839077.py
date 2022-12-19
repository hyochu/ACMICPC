n = int(input())
result = 0
val = 0
for i in range(1, n+1):
  parse = list(map(int, str(i)))
  result = i + sum(parse)
  if result == n:
    val = i
    break
  else:
    val = 0

print(val)
