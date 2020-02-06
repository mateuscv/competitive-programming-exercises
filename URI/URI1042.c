#include <stdio.h>

int main(){
    int a, b, c, i, aux;
    int A[3], B[3];
    scanf("%d%d%d", &A[0], &A[1], &A[2]);

    for (i = 0; i < 3; i++){
        B[i] = A[i];
    }
    

    if (A[0] > A[1]){
        if (A[0] > A[2]){
            if (A[1] > A[2]){
                aux = A[0];
                A[0] = A[2];
                A[2] = aux;
            } else {
                aux = A[1];
                A[1] = A[0];
                A[0] = aux;
                aux = A[2];
                A[2] = A[1];
                A[1] = aux;
            }
        } else {
            aux = A[1];
            A[1] = A[0];
            A[0] = aux;
        }
    } else {
        if (A[0] > A[2]){
            aux = A[2];
            A[2] = A[0];
            A[0] = aux;
        }
        if (A[1] > A[2]){
            if(A[0] > A[1]){
                aux = A[1];
                A[1] = A[0];
                A[0] = aux;
            } else {
                aux = A[1];
                A[1] = A[2];
                A[2] = aux;
            }
        }
    }

    for (i = 0; i < 3; i++){
        printf("%d\n", A[i]);
    }

    printf("\n");

    for (i = 0; i < 3; i++){
        printf("%d\n", B[i]);
    }

    return 0;
}
