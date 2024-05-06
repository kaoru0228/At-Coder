//D - Bitmask
//0:48

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>

// double log_2(int x);
int change_2to10(char *s, int l);
int ruijou(int x, int n);

int i, j;
int N, l=0, k, check=0;
char *S;

int main(){
    //  scanf("%d", &N);
    S = (char *)malloc(sizeof(char)*60);
    scanf("%s", S); scanf("%d", &N);

    for(i=0; i<60; i++){
        if(S[i]=='\0') break;
        l++;
    }

    k = (int)log2(N);

    printf("S:%s N:%d 文字列の長さ:%d log2 N:%d\n", S, N, l, k);

    

    for(i=0; i<l; i++){
        if(S[i]=='?'){
            if(i<l-(k+1)+1){  //N=2^k.~より、系列において右から(k+1)桁までにしか1は来ない。
                S[i]='0';
            }
            else{
                S[i]='1'; check++;
                if(change_2to10(S, l)>N){
                    S[i]='0'; check--;
                }
            }
        }
    }
    printf("%s\n", S);
    if(change_2to10(S, l)<=N) printf("N以下で最大の数:%d\n", change_2to10(S, l));
    else printf("-1\n");

    return 0;
}

// double log_2(int x){
//     return log(x) / log(2);
// }

int change_2to10(char *s, int l){  //s:2進数の系列　l:系列長
    int ans=0;
    for(int i=0; i<l; i++){
        if(s[i]=='1') ans+=ruijou(2, l-i-1);
    }
    return ans;
}

int ruijou(int x, int n){  //x^nの計算用関数
    int ans=1;
    for(int i=0; i<n; i++){
        ans *= x;
    }
    return ans;
}