#include<iostream>
#include <string> 
using namespace std;

int main(){
    int N;
    int A, B;
    char op;
    cin >> N;
    cin >> A >> op >> B;

    if (op == '*'){
        if (A*B <= N) cout << "OK";
        else cout << "OVERFLOW";
    } else if (op == '+') {
        if (A+B <= N) cout << "OK";
        else cout << "OVERFLOW";
    }

    return 0;
}