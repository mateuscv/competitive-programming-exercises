#include<iostream>
#include<vector>
using namespace std;

int main(){
    
    int N, temp;
    bool lampada1 = false, lampada2 = false;
    vector<int> apertos;
    cin >> N;

    for (size_t i = 0; i < N; i++){
        cin >> temp;
        apertos.push_back(temp);
    }
    
    for (size_t i = 0; i < N; i++){
        if (apertos[i] == 1){
            lampada1 = !lampada1;
        } else {
            lampada1 = !lampada1;
            lampada2 = !lampada2;
        }
    }
    
    if (lampada1){
        cout << 1 << "\n";
    } else{
        cout << 0<< "\n";
    }


    if (lampada2){
        cout << 1<< "\n";
    } else{
        cout << 0<< "\n";
    }

    return 0;
}