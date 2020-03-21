#include<iostream>
using namespace std;

int main(){
    double A, B, media;
    cin >> A >> B;
    media = ((A+B)/2);
    if (media >= 7.0)
        cout << "Aprovado";
    else if (media >= 4) cout << "Recuperacao";
    else cout << "Reprovado";
    return 0;
}