#include<iostream>
using namespace std;

int main(){
    int N, temp1, temp2, sum = 0;
    cin >> N;
    for (int i = 0; i < N; i++){
        cin >> temp1 >> temp2;
        if (temp1 > temp2)
            sum += temp2;
    }
    cout<<sum;
    
    return 0;
}