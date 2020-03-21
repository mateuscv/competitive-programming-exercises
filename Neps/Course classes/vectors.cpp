#include<vector>
#include<iostream>
using namespace std;

int main(){
    vector<int> V;
    V.push_back(10);
    V.push_back(8);
    V.push_back(156);

    for (size_t i = 0; i < V.size(); i++){
        cout << V[i] << '\n';
    }
    
    V.resize(4); //aumenta o tamanho do vetor e se necessário enche de zeros.
    V.pop_back(); //apaga ultimo elemento

    //ordenar:
    sort(V.begin(), V.end()) // inplace

    V.clear(); //limpa o vetor; fica vazio



    return 0;
}