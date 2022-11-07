import sys

if n == 0:
    print(0)
elif n == 1:
    print(1)

dp = [0, 1, 2]
for i in range(2+1, n+1):
    dp.append(dp[i - 1] + dp[i - 2])
    
print(dp[n])