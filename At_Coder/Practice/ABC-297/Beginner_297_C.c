#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int H, W, i, j;
char **S;

int main(){
    printf("H, W の入力:");
    scanf("%d %d", &H, &W);
    printf("H : %d, W : %d\n", H, W);
    printf("Si の入力:");

    S = (char **)malloc(sizeof(char *)*H);
    for(i=0; i<H; i++) S[i] = NULL;

    for(i=0; i<H; i++){
        S[i] = (char *)malloc(sizeof(char)*W);
        scanf("%s", S[i]);
        printf("%s\n", S[i]);
    }

    for(i=0; i<H; i++){
        for(j=0; j<W; j++){
            if(S[i][j]=='T' && S[i][j+1]=='T'){
                S[i][j] = 'P';
                S[i][j+1] = 'C';
            }
        }
    }

    printf("\n");

    for(i=0; i<H; i++){
        printf("%s\n", S[i]);
    }

    for(i=0; i<H; i++){
        free(S[i]);
    }
    free(S);
    
    return 0;
}