def solve(n):
    count = 0
    coin_type = [500, 100, 50, 10, 5, 1]
        
    for coin in coin_type:
        count += n // coin
        n %= coin
            
    print(count)

n = input()
solve(1000-int(n))
