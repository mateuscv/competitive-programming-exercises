#include<iostream>
using namespace std;

int main(){
    int A, B;
    cin >> A;
    cin >> B;
    if (A+B <= 50){
        cout << "S";
    } else {
        cout << "N";
    }
    return 0;
}