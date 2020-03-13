#include<vector>
#include<iostream>
#include <algorithm>
#include<iterator>
using namespace std;

int main(){
    int N, M;
    vector<int> Fila;
    vector<int> Sairam;
    bool saiu = false;

    cin >> N;
    Fila.resize(N);
    
    for (size_t i = 0; i < N; i++){
        cin >> Fila[i];
    }
    
    cin >> M;
    Sairam.resize(M);

    for (size_t i = 0; i < M; i++){
        cin >> Sairam[i];
    }

    for (size_t i = 0; i < Fila.size(); i++){
        saiu = false;
        for (size_t j = 0; j < Sairam.size(); j++){
            if(Fila[i] == Sairam[j]){
                saiu = true;
                break;
            }
        }
        if (saiu == true){
            Fila[i] = 0;
        }
    }
    

    for (size_t i = 0; i < Fila.size()-1; i++){
        if (Fila[i] != 0){
            cout << Fila[i] << " ";
        }
        
    }
    
    if (Fila.back() != 0){
        cout << Fila.back() << '\n';
    }
    
    return 0;
}