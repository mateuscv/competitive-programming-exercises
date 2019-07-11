#include<stdio.h>
int main(){
    double M[12][12], res;
    int col, i, j;
    char somaOUmedia;
    scanf("%d", &col);
    scanf(" %c", &somaOUmedia);
    for (i = 0; i < 12; i++){
        for(j = 0; j < 12; j++)
            scanf("%lf", &M[i][j]);
    }
    res = 0.0;
    if (somaOUmedia == 'S'){
        for (i = 0; i < 12; i++){
            res = res + M[i][col];
        }
    } else {
        for (i = 0; i<12; i++){
            res = res + M[i][col];
        }
        res = res/12.0;
    }
    printf("%.1lf\n", res);
    return 0;
}