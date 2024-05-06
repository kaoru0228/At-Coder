#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

 
// 縦　H 行、横  W 列のグリッドがあります。
// このグリッドから一様ランダムに K 個のマスを選びます。選んだマスを全て含むような（グリッドの軸に辺が平行な）最小の長方形に含まれるマスの個数がスコアとなります。

// 考察
// 長方形は、選んだ点、( i , j )において、(iの最小値, jの最小値)と(iの最大値, jの最大値)で作る長方形と考えられる。
//計算のオーダーは O( (H*W)^K )

int factorial(int a);
int extendedEuclidean(int a, int m);

int H, W, K, *Hi, *Wj, score, total=0, count=0;
int under;
int i, j, s, t, l;
int minH, minW, maxH, maxW;
int mod = 998244353, inv, ans=0;  //mod計算用

//mod 998244353で取る。※intは21億まで行ける
int main(){

    printf("H, W, K の入力：");
    scanf("%d %d %d", &H, &W, &K);
    printf("H:%d W:%d K:%d \n", H, W, K);

    under = factorial(H*W)/(factorial(K)*factorial((H*W)-K));  //期待値の分母 H*W C K の計算
    //under = (H*W)/(K!*(H*W-K)! );
    
    printf("H*W_C_K : %d\n", under);

    Hi = (int *)malloc(sizeof(int)*K);
    Wj = (int *)malloc(sizeof(int)*K);

    // for(l=0, l<K, l++){
    //     for(i=0; i<H; i++){
    //         for(j=0; j<W; j++){

    //         }
    //     }
    // }

    for(i=0; i<H; i++){
        Hi[0] = i+1;
        for(j=0; j<W; j++){
            Wj[0] = j+1;

            for(s=0; s<H; s++){
                Hi[1] = s+1;
                for(t=0; t<W; t++){
                    Wj[1] = t+1;
                    if (Hi[1]!=Hi[0] | Wj[1]!=Wj[0]){
                        
                        for(l=1; l<K; l++){
                            maxH=Hi[0];  maxW=Wj[0]; minH=Hi[0];  minW=Wj[0];
                            if(maxH<Hi[l]) maxH = Hi[l];
                            if(maxW<Wj[l]) maxW = Wj[l];
                            if(minH>Hi[l]) minH = Hi[l];
                            if(minW>Wj[l]) minW = Wj[l];
                        }
                        score = ( (maxW - minW +1) * (maxH - minH +1) );
                        total += score;
                        printf("(%d, %d), (%d, %d)score : %d\n", Hi[0], Wj[0], Hi[1], Wj[1], score);
                        count++;
                    }
                }
            }
        }
    }
    total = total / factorial(K);
    printf("total : %d, count : %d\n", total, count);

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
