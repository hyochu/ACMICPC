#1번 해
# 카드 개수 : N
# 필요 도달 : M
# N개 중 3개를 골라 최대한 M에 가깝게 만들기

n, m = map(int, input().split(" "))
cardDummy = list(map(int, input().split(" ")))
summary = 0
temp = 0

#range(시작, 끝)
for i  in range(n):
  for j in range(i+1, n):
    for k in range(j+1, n):
      summary = cardDummy[i] + cardDummy[j] + cardDummy[k]
      if summary > m :
        continue
      else:
        #temp = max(temp, summary)
        if summary > temp:
          temp = summary
        
print(temp)

#2번 해
# 카드 개수 : N
# 필요 도달 : M
# N개 중 3개를 골라 최대한 M에 가깝게 만들기

n, m = map(int, input().split(" "))
cardDummy = list(map(int, input().split(" ")))
summary = 0
temp = 0

#range(시작, 끝)
for i  in range(n):
  for j in range(i+1, n):
    for k in range(j+1, n):
      summary = cardDummy[i] + cardDummy[j] + cardDummy[k]
      if summary > m :
        continue
      else:
        temp = max(temp, summary)
        
print(temp)
