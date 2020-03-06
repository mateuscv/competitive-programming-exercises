#include<stdio.h>
using namespace std;

int main(){
    int K, N, M, X, Y, stop = 1;

    scanf("%d", &K);

    while(stop){
        if (K == 0){
            stop = 0;
        }
        
        scanf("%d %d", &N, &M);
        
        for (size_t i = 0; i < K; i++){
            scanf("%d %d", &X, &Y);
            if (X == N || Y == M){
                printf("divisa\n");
                continue;
            }
            if (X > N){
                if (Y > M){
                    printf("NE\n");
                } else {
                    printf("SE\n");
                }
            } else {
                if (Y > M){
                    printf("NO\n");
                } else {
                    printf("SO\n");
                }

            }   
        }
        scanf("%d", &K);
    }

    return 0;
}