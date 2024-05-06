#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

 
// 縦　H 行、横  W 列のグリッドがあります。
// このグリッドから一様ランダムに K 個のマスを選びます。選んだマスを全て含むような（グリッドの軸に辺が平行な）最小の長方形に含まれるマスの個数がスコアとなります。

// 考察
// あり得る長方形をすべて数え上げ、各長方形においてK個のグリッドでそれぞれ何パターンずつ存在するかを数える。

int factorial(int a);
int extendedEuclidean(int a, int m);
int combination(int n, int r);

int H, W, K;
int area, count, cou=0, score, total=0;
int under;
int i, j;
int mod = 998244353, inv, ans=0;  //mod計算用

//mod 998244353で取る。※intは21億まで行ける
int main(){

    printf("H, W, K の入力：");
    scanf("%d %d %d", &H, &W, &K);
    printf("H:%d W:%d K:%d \n", H, W, K);

    under = combination(H*W, K);   //期待値の分母 H*W C K の計算
    printf("H*W_C_K : %d\n", under);

    for(i=1; i<=H; i++){
        for(j=1; j<=W ;j++){
            if( (i*j)>=K ){
                area = i*j;
                //count = combination(area, K);
                //count = factorial(area) / ( factorial(K) * factorial( area - K ) );
                score = area*count;
                total += score;
                cou++;
                printf("score: %d\n", score);
                printf("area: %d\n", area);
                printf("i, j : %d, %d\n", i, j);
            }
        }
    }

    printf("total : %d, count : %d\n", total, cou);



    //mod

    inv = extendedEuclidean(under, mod);
    for(i=0; i<total; i++){
        ans = (ans + inv) % mod;
    }

    printf("answer : %d\n", ans);

    return 0;
}

int factorial(int a){  //階乗計算用関数
    int k=1;
    for(i=1; i<=a; i++){
        k = k*i;
    }
    return k;
}

int combination(int n, int r){  //nCr計算用
    return factorial(n)/( factorial(r)*factorial(n-r) );
}

int extendedEuclidean(int a, int m){  //逆元を求める関数
    int m0 = m, t, q;
    int x0 = 0, x1 =1;
    if(m ==1) return 0;

    //拡張ユークリッド
    while(a>1){
        q = a/m;
        t = m;

        m = a%m;
        a = t;

        t = x0;
        x0 = x1 - q*x0;
        x1 = t;
    }
    // x1が逆元となる
    if(x1<0) x1 += m0;
    return x1;
}

//このプログラムだと、2×2(H, Wが2, 2)の時しか対応できない