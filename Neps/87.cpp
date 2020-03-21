#include<iostream>
using namespace std;

int main(){
    int P,R;
    cin >> P >> R;
    if (P){
        if (R){
            cout<<"A";
        } else {
            cout<<"B";
        }
    } else {
        cout << "C";
    }
    return 0;
}