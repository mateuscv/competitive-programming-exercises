#include<iostream>
#include<vector>
using namespace std;

int main(){
    int list_size, temp;
    int sum = 0;
    vector<int> dias;

    cin >> list_size;

    for (size_t i = 0; i < list_size; i++){
        cin >> temp;
        dias.push_back(temp);
    }

    for (size_t i = 0; i < list_size; i++){
        sum = sum + dias[i];
        if (sum >= 1000000){
            cout << i+1;
            break;
        }
    }
    
    

    return 0;
}