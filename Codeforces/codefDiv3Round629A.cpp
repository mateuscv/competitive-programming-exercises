#include<iostream>
using namespace std;

int main(){
    int N, A, B, number_of_steps;
    cin >> N;
    for (size_t i = 0; i < N; i++){
        cin >> A >> B;
        if (A%B != 0){
            number_of_steps = (B - (A%B));
            cout << number_of_steps << "\n";
        }
        else cout << 0 << "\n";
    }
    
    return 0;
}
