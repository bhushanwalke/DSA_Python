def fib(tmp, n):
    print(tmp, " ",n)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else: return fib("1st", n-1)+fib("2nd", n-2)

def fib_dp(n):
    dp = [0,1]
    for i in range(2,n+1):
        dp.append(dp[i-1] + dp[i-2])
    return dp[n]

dp = {1:1, 2:1}
def fib_dp2(n):
    global dp
    if n <=2: return 1
    if n in dp:
        return dp[n]
    else:
        dp[n] = fib_dp2(n-1)+fib_dp2(n-2)
    return dp[n]



print fib("initial", 5)
print fib_dp(5)
print fib_dp2(5)
