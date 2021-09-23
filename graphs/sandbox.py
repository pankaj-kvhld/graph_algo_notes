

def fib_mem(n: int, memo={}) -> int:
    if n <= 2:
        return 1
    if n in memo:
        return memo.get(n)
    memo[n] = fib_mem(n - 1, memo) + fib_mem(n - 2, memo)
    return memo[n]


res = fib_mem(10)
print(res)