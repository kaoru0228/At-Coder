//B - Fill the Gaps
//1:26

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

int N, *A, *B, test=0, count1=0, count2=0, diff;
int i, j;

int main(){
    scanf("%d", &N);
    A = (int *)malloc(sizeof(int)*N);
    B = (int *)malloc(sizeof(int)*N*100);
    for(i=0; i<N; i++){
        scanf("%d", &A[i]);
    }
    for(i=0; i<N; i++){
        B[i]=A[i];
    }


    for(i=0; i < N-1; i++){
        if(A[i]>A[i+1] && A[i]-A[i+1]>1){
            printf("i:%d, i+1:%d\n", A[i], A[i+1]);
            diff = A[i]-A[i+1];
            count1 += diff-1;
            //ずらす
            for(j = N + count1 - 1; j>= i+count2+diff ; j--){
                B[j] = B[j - diff+1];
            }

            // for(int k=0;k<N+count1;k++){
            //     printf("%d, ",B[k]);
            // }
            // printf("\n");

            //挿入
            for(j=i+count2 +1; j<= i+count2 +diff-1; j++){
                B[j] = B[j-1]-1;
            }
             count2 += diff-1;
        }

        if(A[i]<A[i+1] && A[i+1]-A[i]>1){
            printf("i:%d, i+1:%d\n", A[i], A[i+1]);
            diff = A[i+1]-A[i];
            count1 += diff-1;
            //ずらす
            for(j = N + count1 - 1; j>= i+count2+diff ; j--){
                B[j] = B[j - diff+1];
            }

            //挿入
            for(j=i+count2 +1; j<= i+count2 +diff-1; j++){
                B[j] = B[j-1]+1;
            }
             count2 += diff-1;
        }
        
    }
    for(i=0;i<N+count1;i++){
        printf("%d, ",B[i]);
    }
    printf("\n");

    return 0;
}