#include<vector>
#include <string>
#include<iostream>
using namespace std;

int main(){

    // naipes: P, O, C, E --> 1 2 3 4

    int P_num_jogadores, M_num_cartas_mao, N_num_cartas_baralho, temp;
    string naipe;
    cin >> P_num_jogadores >> M_num_cartas_mao >> N_num_cartas_baralho;
    vector<int> baralho;
    vector<int> numeros;
    vector<int> naipes;
    vector<int> roda_jogadores;

    while((P_num_jogadores!=0) || (M_num_cartas_mao!=0) || (N_num_cartas_baralho!=0)){

        // input for:
        for (size_t i = 0; i < N_num_cartas_baralho; i++){
            cin >> temp;
            baralho.push_back(temp);
            cin >> naipe;
            if (naipe.compare("C") == 0){
                baralho.push_back(1);
            } else if (naipe.compare("D") == 0){
                baralho.push_back(2);
            } else if (naipe.compare("H") == 0){
                baralho.push_back(3);
            } else {
                baralho.push_back(4);
            }
        }

        // numeros:
        for (size_t i = 0; i < N_num_cartas_baralho; i = i+2){
            numeros.push_back(baralho[i]);
        }
        
        // naipes:
        for (size_t i = 1; i < N_num_cartas_baralho; i = i+2){
            naipes.push_back(baralho[i]);
        }

        //rodinha dos jogadores
        for (size_t i = 0; i < P_num_jogadores; i++){
            roda_jogadores.push_back(i+1);
        }
        

        cin >> P_num_jogadores >> M_num_cartas_mao >> N_num_cartas_baralho;
        baralho.clear();    

    }


    return 0;
}