import sys
N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
dp = [[0 for i in range(1001)] for j in range(1001)]
dp[0][0] = 1
dp[1][0] = 1
dp[1][1] = 1
for i in range(2,1001):
    for j in range(i//2+1):
        dp[i][j] = (dp[i-2][j-1] + dp[i-1][j])%1000000003
print(dp[N][K]%1000000003)
