#include<iostream>
#include<iomanip>
#include<cmath>
using namespace std;

int main(){
    int N;
	double temp;
    cin >> N;
    for (int i = 0; i<N; i++){
    	cin >> temp;
        cout << fixed;
        cout << setprecision(4);
        cout << sqrt(temp) << "\n";
    }
	return 0;
}