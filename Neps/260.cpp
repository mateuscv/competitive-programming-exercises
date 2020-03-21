#include<iostream>
using namespace std;

int main(){
    int P_1, C_1, P_2, C_2, left, right;
    cin >> P_1  >> C_1  >> P_2  >> C_2;
    left = P_1*C_1;
    right = P_2*C_2;

    if (left > right){
        cout << -1;
    } else if (right > left) {
        cout << 1;
    } else {
        cout << 0;
    }

    return 0;
}