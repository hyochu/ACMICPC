#1차
n = int(input())
primeArr = list(map(int,input().split()))
count = 0
for i in primeArr:
  #소수 판별용
  comNum = 0
  if i > 1:
    for j in range(2, i+1):
      if i%j == 0:
        comNum += 1
        #print('comNum : ', comNum)
    if(comNum == 1):
      count += 1
print(count)

#그 외
def isPrime(num):
    if num == 1:
        return False
    for i in range(2,num):
        if num%i == 0:
            return False
    return True


n = int(input())
arr = list(map(int,input().split(" ")))
c = 0
for n in arr:
    if isPrime(n):
        c += 1
        
print(c)
