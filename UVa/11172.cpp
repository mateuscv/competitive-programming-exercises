#include<iostream>
using namespace std;

int main(){
    int lineNumber = 0;
    int op1, op2;
    cin >> lineNumber;
    for (size_t i = 0; i < lineNumber; i++){
        cin >> op1 >> op2;
        if (op1>op2){
            cout << ">\n";
        } else if (op2>op1){
            cout << "<\n";
        } else {
            cout << "=\n";
        }
        
    }
    
}