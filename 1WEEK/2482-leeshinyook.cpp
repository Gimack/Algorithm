#include <iostream>
#include <vector>
#include <queue>
#include <climits>
#include <cstring>
#include <algorithm>
#include <math.h>
#include <map>
#include <set>
const int mod = 1000000003;
using namespace std;

int dp[1001][1001];
int N, K;
int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cin >> N;
    cin >> K;
    for(int i = 0; i <= N; i++) {
        dp[i][0] = 0;
        dp[i][1] = i;
    }
    for(int i = 2; i <= N; i++) {
        for(int j = 2; j <= K; j++) {
            dp[i][j] = (dp[i - 1][j] + dp[i - 2][j - 1]) % mod;
        }
    }
    int answer = (dp[N - 3][K - 1] + dp[N - 1][K]) % mod;
    cout << answer;

}

