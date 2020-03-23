#include<iostream>
#include<iomanip>
#include<cmath>
using namespace std;

int main(){
    double N, M;
    cin >> N;
    cin >> M;
    cout << fixed;
    cout << setprecision(4);
    cout << pow(N, M) << "\n";
	return 0;
}