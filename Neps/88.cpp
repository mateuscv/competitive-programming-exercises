#include<iostream>
using namespace std;

int main(){
    int A, B, C;
    cin >> A >> B >> C;
    if (A == B && B == C)
        cout<<"*";
    else if (A == B && B != C)
        cout<<"C";
    else if (A != B && A == C)
        cout<<"B";
    else if (A != B && A != C)
        cout<<"A";
	return 0;    
}
