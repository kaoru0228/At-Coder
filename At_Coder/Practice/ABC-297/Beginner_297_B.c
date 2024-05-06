#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int b1, b2, r1, r2, k, count=0;
char S[9];

int main(){
    scanf("%s", S);
    printf("%s\n", S);

    for(int i=0; i < strlen(S); i++){
        if(S[i]=='B' && count == 0){
            b1=i+1;
            count++;
        }
        if(S[i]=='B' && count == 1){
            b2=i+1;
            break;
        }
    }
    if( (b1 + b2)%2 ==0 ){
        printf("No\n");
        return 0;
    }

    count=0;
    for(int i=0; i < strlen(S); i++){
        if(S[i]=='R' && count == 0){
            r1=i+1;
            count++;
        }
        if(S[i]=='R' && count == 1){
            r2=i+1;
        }
        if(S[i]=='K'){
            k=i+1;
        }
    }

    if(r1 < k && k < r2) printf("Yes\n");
    else printf("No\n");

    return 0;

    // int a = 'A' +2 ;
    // char c = a;
    // printf("%d\n", a);
    // printf("%c\n", c);
}