#첫번째 시도
def solve(a,b):
    #a를 b만큼 거듭제곱 한 뒤, 맨 마지막 숫자(1의 자리)
    re = int(a)**int(b)
    one = len(str(re))
    print(one)

t = input()

for i in range(int(t)):
    a = input()
    b = input()
    solve(a,b)
-> one = re[len(str(re))] 해당 부분이 틀렸음을 인지

#두번째 시도
def solve(a,b):
    re = int(a)**int(b)
    re = str(re)
    one = re[len(re)-1]
    print(one)

t = input()

for i in range(int(t)):
    a = input()
    b = input()
    solve(a,b)
-> 런타임 에러


#세번째 시도
def solve(a,b):
    arr = [a%10] #1의 자리 수만 남긴다.
    temp = a%10 # 초기값 대입 용도 

    for i in range(b - 1):
        temp = (temp * a) % 10
        
        if temp in arr:
            break #이미 담겨 있는 값은 체크할 필요가 없다.
        else:
            arr.append(temp)
    ans = arr[b%len(arr)-1]
    if ans == 0:
        ans = 10 #0번째 컴퓨터는 없기 때문에, 0번째라면 10번째 컴퓨터를 의미한다.
    print(ans)
    
#t에 반복 횟수 input을 담아, 반복문을 돌린다.
#이 때, 요건 충족을 위해 map(int, input().split(" ")) 사용하여, 두 가지 input 값을 동시에 받는다.
t = input()
for i in range(int(t)):
    a,b = map(int, input().split(" "))
    
    solve(a,b)
-> 해석
ex) a = 7,  b = 100
    : b번 곱한다 = for문
        7 * 7 => 49 % 10 => 9
        9 * 7 => 63 % 10 => 3
        3 * 7 => 21 % 10 => 1
        1 * 7 => 7 % 10 => 7
        => [7 9 3 1] 7 9 3 1 .....와 같이, 끝 자리 수가 반복됨을 알 수 있다.
ex) a = 2  ,  b = 100
   : [2 4 8 6] 2 4 8 6
    
    # a = 100
    
