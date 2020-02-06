#include<stdio.h>

int GCD(int x, int y){

    int status = 0;
    int gcd = 0;
    int mod = 1;

    while (mod != 0){
        if ((x > y) || (x == y)){
            status = 0;
            mod = x%y;
            if (mod == 0){
                break;
            }
            x = y;
            y = mod; 
        }
        else if (y > x){
            status = 1;
            mod = y%x;
            if (mod == 0){
                break;
            }
            y = x;
            x = mod; 
        }
    }

    if (status == 0){
        gcd = y;
    }
    else if (status == 1){
        gcd = x;
    }

    return gcd;
}

int main(){

    int i, maxPile = 0;
    int numberOfCases = 0;
    int traderA, traderB = 0;
    scanf("%d", &numberOfCases);
    
    for (i = 0; i < numberOfCases; i++){
        scanf("%d%d", &traderA, &traderB);
        maxPile = GCD(traderA, traderB);
        printf("%d\n", maxPile);
    }
    
    return 0;
}   
