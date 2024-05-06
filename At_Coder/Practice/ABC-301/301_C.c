//C - AtCoder Cards
//0:56

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

int i, j;
int n=0, countS=0, countT=0, answer=1, breaker;
char *S, *T;

int main(){
    //  scanf("%d", &N);
    S = (char *)malloc(sizeof(char)*200000);
    T = (char *)malloc(sizeof(char)*200000);
    scanf("%s", S);
    scanf("%s", T);
    printf("S:%s\n", S);
    printf("T:%s\n", T);

    for(i=0; i<200000; i++){
        if(S[i]=='\0') break;
        n++;
    }
    printf("文字数 : %d\n", n);

    for(i=0; i<n; i++){
        if(S[i]=='@'){
                S[i]='1'; countS++;
                continue;
            }

        for(j=0; j<n; j++){
            if(T[j]=='@'){
                T[j]='1'; countT++;
                continue;
            }
            if(S[i] == T[j]){
                S[i]='1'; T[j]='1';
                break;
            }
        }
    }
    printf("S:%s, @:%d\n", S, countS);
    printf("T:%s, @:%d\n", T, countT);

    for(i=0; i<n; i++){
        if(S[i]=='1') continue;
        else if(S[i]=='a' | S[i]=='t' | S[i]=='c' | S[i]=='o' | S[i]=='d' | S[i]=='e' | S[i]=='r'){
            if(countT>0){
                S[i]='1'; countT--;
                continue;
            }
            else{
                answer = 0;
                break;
            }
        }
        else{
            answer = 0;
            break;
        }        
        for(j=0; j<n; j++){
            if(T[j]=='1') continue;
            else if(T[j]=='a' | T[j]=='t' | T[j]=='c' | T[j]=='o' | T[j]=='d' | T[j]=='e' | T[j]=='r'){
                if(countS>0){
                    T[j]='1'; countS--;
                    continue;
                }
                else{
                    answer = 0; breaker=1;
                    break;
                }
            }
            else{
                answer = 0; breaker=1;
                break;
            }
        }
        if(breaker==1) break;
    }
    if(answer==0) printf("No\n");
    else printf("Yes\n");

    printf("S:%s, @:%d\n", S, countS);
    printf("T:%s, @:%d\n", T, countT);


    return 0;
}