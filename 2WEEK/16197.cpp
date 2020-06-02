#include <iostream>
#include <queue>
#include <climits>
#include <vector>
using namespace std;

char arr[21][21];
int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};
int N, M;
int ans = INT_MAX;
void DFS(int x1, int y1, int x2, int y2, int cnt)
{
    if (cnt > 10)
    {
        return;
    }
    for (int i = 0; i < 4; i++)
    {
        bool out1 = false, out2 = false;
        int mx1 = x1 + dx[i];
        int my1 = y1 + dy[i];
        int mx2 = x2 + dx[i];
        int my2 = y2 + dy[i];
        if (x1 < 1 || x1 > N || y1 < 1 || y1 > M)
            out1 = true;
        if (x2 < 1 || x2 > N || y2 < 1 || y2 > M)
            out2 = true;
        if (out1 && out2)
            continue;
        if (out1 || out2)
        {
            ans = min(ans, cnt);
            return;
        }
        if (arr[mx1][my1] == '#')
        {
            mx1 = x1;
            my1 = y1;
        }
        if (arr[mx2][my2] == '#')
        {
            mx2 = x2;
            my2 = y2;
        }
        DFS(mx1, my1, mx2, my2, cnt + 1);
    }
}
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> N >> M;
    vector<pair<int, int>> v;
    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j <= M; j++)
        {
            cin >> arr[i][j];
            if (arr[i][j] == 'o')
            {
                v.push_back({i, j});
            }
        }
    }
    DFS(v[0].first, v[0].second, v[1].first, v[1].second, 0);
    if (ans == INT_MAX)
    {
        cout << -1;
    }
    else
    {
        cout << ans;
    }
}