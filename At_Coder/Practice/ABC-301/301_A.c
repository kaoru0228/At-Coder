//A - Overall Winner 
//0:19

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

int N, i, countT, countA;
char *S, winner, later;

int main(){
    scanf("%d", &N);
    S = (char *)malloc(sizeof(char)*N);
    scanf("%s", S);
    
    for(i=0; i<N; i++){
        if(S[i]== 'T') countT ++;
        if(S[i]== 'A') countA ++;
        if(i== N-1){
            if(S[i]=='T') later='T';
            else if(S[i]=='A') later='A';
        }
    }
    if(countT>countA) printf("T\n");
    else if(countT<countA) printf("A\n");
    else if(countT==countA){
        if(later=='T') printf("A\n");
        else printf("T\n");
    }
    //printf("%d\n", winner);

    return 0;
}