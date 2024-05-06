#include <stdio.h>
#include <stdlib.h>

int N, D, T[4], out;
int *Time;

int main(void){
    printf("N, D:");
    scanf("%d %d", &N, &D);
    printf("N:%d, D:%d\n", N, D);

    Time = (int *)malloc(sizeof(int)*N);

    printf("N=%d, Tの入力：",N);
    for(int i=0; i<N; i++){
        scanf("%d", &Time[i]);
    }
    for(int i=0; i<N ;i++){
        printf("Time%d:%d", i+1, Time[i]);
    }
    printf("\n");

    // printf("T:");
    // scanf("%d %d %d %d", &T[0], &T[1], &T[2], &T[3]);
    // printf("T1:%d, T2:%d, T3:%d, T4:%d\n", T[0], T[1], T[2], T[3]);

    out = -1;

    for(int i=0; i<N; i++){
        if(Time[i+1]-Time[i] <= D){
            out = Time[i+1];
            break;
        }
    }
    printf("%d\n", out);

    free(Time);
    return out;

}
