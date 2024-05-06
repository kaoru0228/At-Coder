#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

int N, *A, i;
unsigned long long int K, *payment, count, j;

int main(){
    printf("N, K の入力：");
    scanf("%d %llu", &N, &K);
    printf("N : %d, K : %llu\n", N, K);

    A = (int *)malloc(sizeof(int)*N);

    printf("Ai の入力：");
    for(i=0; i<N; i++){
        scanf("%d", &A[i]);
    }

    for(i=0; i<N; i++){
        printf("A%d:%d ", i+1, A[i]);
    }
    printf("\n");

    payment = (unsigned long long int *)malloc(sizeof(unsigned long long int)*K);
    for(i=0; i<K; i++) payment[i]=0;  //初期化（0を代入）

    count=0;  //ループでpayment[count]の値を決定させる。（countは0 ~ K-1）
    while(count!=K){
        //初期値
        if(count!=0) payment[count] = payment[count-1]+A[0];
        else payment[count] = A[0];

        for(i=0; i<N; i++){

            if(count==0) {
                if(payment[count]>A[i]) payment[count] = A[i];
            }

            else{  //count!=0
                if(payment[count]>A[i] && payment[count-1]<A[i]) payment[count] = A[i];
                
                for(j=0; j<count; j++){
                    if(payment[count]>payment[j]+A[i] && payment[count-1]<payment[j]+A[i]) payment[count] = payment[j]+A[i];
                }

            }
            
        }

        count++;
    }
    printf("%llu番目に安い金額 : %llu\n", K, payment[K-1]);

    // for(i=0; i<K; i++){
    //     printf("%llu\n", payment[i]);
    // }

    free(A);
    free(payment);
    return 0;
    

}