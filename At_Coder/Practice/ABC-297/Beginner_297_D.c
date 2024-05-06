#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

unsigned long long int A, B;
int count=0;


int main(){
    // time_t start = time(NULL);
    clock_t start = clock();

    printf("A, B の入力");
    scanf("%llu %llu", &A, &B);
    printf("A : %llu, B : %llu\n", A, B);

    while(A!=B){
        if(A>B) A = A-B;
        else if(A<B) B = B-A;
        count++;
    }
    printf("試行回数：%d\n", count);


    // time_t finish = time(NULL);
    // printf("経過時間：%ld\n",finish-start );
    clock_t end = clock();
    double sec = (double)(end - start) / CLOCKS_PER_SEC;
    printf("経過時間：%f秒\n", sec);


    return 0;
}