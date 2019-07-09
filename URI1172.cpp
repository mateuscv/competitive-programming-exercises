#include <bits/stdc++.h> 
#define tamanho 10

using namespace std;

int main(){
    int var, i, j;
    vector<int> X;
    X.reserve(tamanho);
    for (i = 0; i < tamanho; i++){
        cin >> var;
        if (var<=0){
            var=1;
        } 
        X.push_back(var);
    }
    for (i = 0; i < tamanho; i++){
        cout << "X[" << i << "] = " << X.at(i) << "\n";
    }
    return 0;
}