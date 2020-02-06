#include<bits/stdc++.h>
#define tamanho 20
using namespace std;

int main(){
    int var, cont = 0, descont = tamanho-1;
    vector<int> N;
    N.reserve(tamanho);
    for (size_t i = 0; i < tamanho; i++){
        cin >> var;
        N.push_back(var);
    }
    while (cont != 10){
        var = N.at(cont);
        N.at(cont) = N.at(descont);
        N.at(descont) = var;
        cont++;
        descont--;
    }
    for (size_t i = 0; i < tamanho; i++){
        cout << "N[" << i << "] = " << N.at(i) << "\n";
    }
    
    return 0;
}