#include<iostream>
using namespace std;
int main(){
	int A, B;
    cin >> A;
    cin >> B;
    if ((A == B) || ((A%2==0) && (B%2==0)) || ((A%2==1) && (B%2==1))){
    	cout << 1;
    } else {
        cout << 0;
    }
	return 0;
}