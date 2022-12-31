// 1932: 정수 삼각형

#include <stdio.h>

int dp[501][501];

int max(int a, int b)
{
    if(a > b) return a;
    else return b;
}

int main(void)
{
    int n, maxi = 0;
    scanf("%d", &n);

    for(int i = 0; i < n; i ++){
        for(int j = 0; j <= i; j++){
            scanf("%d", &dp[i][j]);
        }
    }

    for(int i = 1; i < n; i ++){
        for(int j = 0; j <= i; j++){
            if(j == 0) dp[i][j] += dp[i - 1][j];
            else if(j == i) dp[i][j] += dp[i - 1][j - 1];
            else dp[i][j] += max(dp[i - 1][j - 1], dp[i - 1][j]);
        }
    }

    for(int i = 0; i < n; i ++){
        maxi = max(maxi, dp[n - 1][i]);
    }

    printf("%d\n", maxi);

    return 0;
}