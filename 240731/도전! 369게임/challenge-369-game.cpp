#include <iostream>
#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

const long long mod=1000000007;

int memo[100001][3][2][2];

int dp(const string &s, int x, int sum, bool f, bool over)
{
    if(s[x]==0){
        return (f || sum==0);
    }
    if(memo[x][sum][f][over]!=-1){ return memo[x][sum][f][over]; }
    memo[x][sum][f][over]=0;
    if(over==1){
        for(char i='0'; i<=s[x]; i++){
            int val=i-'0';
            memo[x][sum][f][over]=(memo[x][sum][f][over]+dp(s, x+1, (sum+val)%3, f||(val%3==0 && val!=0), i==s[x]))%mod;
        }
    }
    else{
        for(char i='0'; i<='9'; i++){
            int val=i-'0';
            memo[x][sum][f][over]=(memo[x][sum][f][over]+dp(s, x+1, (sum+val)%3, f||(val%3==0 && val!=0), 0))%mod;
        }
    }
    return memo[x][sum][f][over];
}


int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
    string a, b;
    string n;
    cin >> n;
    a = 1;
    b = n;
    memset(memo, -1, sizeof(memo));
    int ans=dp(b, 0, 0, 0, 1);
    memset(memo, -1, sizeof(memo));
    ans-=dp(a, 0, 0, 0, 1);
    int sum=0, f=0;
    for(int i=0; i<a.size(); i++){
        sum=(sum+a[i]-'0')%3;
        f=f||(a[i]-'0'!=0 && (a[i]-'0')%3==0);
    }
    ans+=(sum==0 || f);
    cout << (ans+mod)%mod - 1 << "\n";
    return 0;
}